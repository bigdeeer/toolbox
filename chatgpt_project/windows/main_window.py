import os
import datetime
from json import load, dump
from functools import partial

from PySide6.QtCore import QSettings, Qt, QSize
from PySide6.QtGui import QPainter, QIcon, QShortcut, QKeySequence, QTextCursor, QImage, QColor, QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton, QFileDialog, QDoubleSpinBox, QListWidget, \
    QListWidgetItem

from func.layout_func import restrain_height, expand_height
from func.workers import GptWorker
from ui.chatgpt_ui import Ui_MainWindow

from utility.style import load_stylesheet

worker = GptWorker()
setting = QSettings('utility/setting.ini', QSettings.Format.IniFormat)

icon_dir = os.path.join(os.path.dirname(__file__), "..", "icon")  # 获取图标文件夹路径
icon_dict = {"model_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/gpt4.png"},
                           {'state': QIcon.State.Off, 'file': f"{icon_dir}/gpt35.png"}],
             "save_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/save.png"}],
             "load_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/load.png"}],
             "frame_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/frame.png"},
                           {'state': QIcon.State.Off, 'file': f"{icon_dir}/frameless.png"}],
             "pin_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/pin.png"},
                         {'state': QIcon.State.Off, 'file': f"{icon_dir}/pinoff.png"}],
             "min_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/min.png"}],
             "max_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/mid.png"},
                         {'state': QIcon.State.Off, 'file': f"{icon_dir}/max.png"}],
             "close_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/close.png"}],
             "system_size_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/down.png"},
                                 {'state': QIcon.State.Off, 'file': f"{icon_dir}/up.png"}],
             "input_size_btn": [{'state': QIcon.State.On, 'file': f"{icon_dir}/down.png"},
                                {'state': QIcon.State.Off, 'file': f"{icon_dir}/up.png"}],
             "send_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/send.png"}],
             "clear_btn": [{'state': QIcon.State.Off, 'file': f"{icon_dir}/clear.png"}]
             }


class ChatForm(QMainWindow, Ui_MainWindow):
    """ AI 工具主界面"""

    dialog = {}
    dialog_fee = 0
    total_fee = 0
    model = "qwen-turbo"  # 默认模型
    dialog_path = 'dialogs/'

    def __init__(self):
        super().__init__()

        self._load_ui()
        self._connect_signals()
        self._load_dialogs()

    def _load_ui(self):
        """ 初始化UI """
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)  # 初始化所有控件

        self.load_window_geo()  # 上次关闭的窗体位置和大小
        self.load_initial_layout_ratio()  # 初始化三个布局的比例
        self.load_style()  # 样式

    def load_window_geo(self):
        geo = self.geometry()
        geo.setLeft(int(setting.value('left')))
        geo.setTop(int(setting.value('top')))
        geo.setWidth(int(setting.value('width')))
        geo.setHeight(int(setting.value('height')))
        self.setGeometry(geo)

    def _connect_signals(self):
        """ 初始化信号 """

        # 五个按钮的信号
        self.send_btn.clicked.connect(self.send_question)
        self.clear_btn.clicked.connect(self.clear_dialog)
        self.input_size_btn.clicked.connect(partial(self.size_btn_switched, 'input'))
        self.system_size_btn.clicked.connect(partial(self.size_btn_switched, 'system'))
        self.pin_btn.clicked.connect(self.pin_on_top)
        self.system_edit.textChanged.connect(self.sys_changed)

        # 键盘快捷键
        QShortcut(QKeySequence("Ctrl+Return"), self, self.send_question)
        QShortcut(QKeySequence("Ctrl+Up"), self, self.input_size_btn.click)
        QShortcut(QKeySequence("Ctrl+Down"), self, self.system_size_btn.click)

        self.dialog_names_list.itemClicked.connect(self.dialog_name_clicked)

        # 开启进程
        worker.answerAvailable.connect(self.receive_answer)  # updateUI是一个更新UI的函数

    def load_style(self):
        """ 加载样式 """

        self.setStyleSheet(load_stylesheet())

        box_list = [self.log_name_edit, self.system_edit, self.input_edit]
        for box in box_list:
            box.setProperty("style", "DEFAULT_BOX_STYLE")

        for button in self.content_wit.findChildren(QPushButton):
            button: QPushButton
            button.setProperty("style", "BUTTON_STYLE")

        for vbox in self.content_wit.findChildren(QDoubleSpinBox):
            vbox: QDoubleSpinBox
            vbox.setProperty("style", "VBOX_STYLE")

        self.model_combo.setProperty("style", "VBOX_STYLE")
        for label in self.token_disp_layout_w.findChildren(QLabel):
            label.setProperty("style", "LABEL_STYLE")

        self.dialog_list.setProperty("style", "DIALOG_BOX_STYLE")

        self.load_icon_color(QColor(187, 206, 251))

    def load_icon_color(self, color):
        """ 更新图标颜色 """

        for btn in self.findChildren(QPushButton):
            btn: QPushButton
            name = btn.objectName()
            if name in icon_dict:
                icon = QIcon()
                for item in icon_dict[name]:
                    mask = QImage(item['file'])
                    mask = mask.convertToFormat(QImage.Format_ARGB32)
                    result = QImage(QSize(30, 30), QImage.Format_ARGB32)
                    result.fill(color)
                    painter = QPainter(result)
                    painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationIn)
                    painter.drawImage(0, 0, mask)
                    painter.end()
                    pixmap = QPixmap.fromImage(result)  # Convert QImage to QPixmap
                    icon.addPixmap(pixmap, QIcon.Normal, item['state'])  # Use addPixmap instead of addFile
                btn.setIcon(icon)

    def _load_dialogs(self):
        """ 加载菜单对话 """

        dialogs = os.listdir(self.dialog_path)

        """ 更新菜单对话 """

        for file_name in dialogs:
            if file_name.endswith('.json'):
                dialog_name = file_name.rsplit('.', 1)[0]
                dialog_item = QListWidgetItem(dialog_name)
                self.dialog_names_list.addItem(dialog_item)

        self.clear_dialog()

    def add_to_dialog(self, dialog_obj):
        """ 将对话记录存入列表 """

        # 存入字典列表
        self.dialog['li'].append(dialog_obj)
        self.dialog_list.add_item(dialog_obj)

    def calculate_price(self, prompt=0, completion=0):
        """ 计算模型的使用费用 """

        if self.model == "qwen-turbo":
            price_input = 0.002
            price_output = 0.006
        elif self.model == "qwen-plus":
            price_input = 0.004
            price_output = 0.012
        elif self.model == "qwen-max":
            price_input = 0.04
            price_output = 0.12
        else:
            price_input = 0
            price_output = 0

        fee = (prompt * price_input + completion * price_output) / 1000
        fee = round(fee, 5)
        count = prompt + completion
        txt = f"{fee:.4f}({count})"
        return txt, fee

    def token_status_update(self, tokens=None):
        """ 更新token状态 """

        if not tokens:
            prompt = completion = 0
        else:
            prompt, completion = tokens

        actual_txt = ""

        feetxt, fee = self.calculate_price(prompt=prompt)
        self.total_fee += fee
        self.dialog_fee += fee
        actual_txt += f"[LastPrompt] = {feetxt}   "

        feetxt, fee = self.calculate_price(completion=completion)
        self.total_fee += fee
        self.dialog_fee += fee
        actual_txt += f"[LastAnswer] = {feetxt}"

        self.actual_token_disp.setText(actual_txt)

        fee = self.dialog_fee
        sum_txt = f"[DialogTotal] = {fee:.4f}   [UserTotal] = {self.total_fee:.4f}"
        self.sum_token_disp.setText(sum_txt)

    def sys_changed(self):
        """ 更改AI 工具的默认提示词 """
        self.dialog['sys']['content'] = self.system_edit.toPlainText()

    def send_question(self):
        """ 发送问题 """
        # 获取问题
        question = self.input_edit.toPlainText()
        self.input_edit.clear()

        # 刷新问题框状态
        self.size_btn_switched('input', checked=False)
        self.size_btn_switched('system', checked=False)

        dialog_obj = {'role': 'user', 'content': question}
        self.add_to_dialog(dialog_obj)

        # 启动回答进程
        worker.message = self.dialog['li']
        worker.message_sys = self.dialog['sys']
        worker.temperature = self.temp_vbox.value()
        worker.top_p = self.topp_vbox.value()

        model = self.model_combo.currentText()
        if model == '3.5-4K':
            model = "deer-gpt-35-turbo"
        self.model = worker.model = model

        worker.start()

        self.input_edit.setProperty("hold", "yes")
        self.input_edit.style().unpolish(self.input_edit)
        self.input_edit.style().polish(self.input_edit)

        self.input_edit.setPlainText(f"Waiting for answer ...")

        self.save_dialog()

    def receive_answer(self, answer, tokens):
        """ 接收回答 """

        dialog_obj = {'role': 'assistant', 'content': answer}
        self.add_to_dialog(dialog_obj)

        # 关闭回答进程
        worker.quit()
        self.input_edit.setProperty("hold", "no")
        self.input_edit.style().unpolish(self.input_edit)
        self.input_edit.style().polish(self.input_edit)

        self.input_edit.setPlainText("")
        self.token_status_update(tokens=tokens)

        self.save_dialog()

    def dialog_name_clicked(self):
        """ 左侧历史对话栏 中 listwidget的item点击事件 """
        dialog_name = self.sender().currentItem().text()

        file_name = dialog_name + '.json'
        file_path = os.path.join(self.dialog_path, file_name)

        self.clear_dialog()
        self.log_name_edit.setText(dialog_name)

        with open(file_path, 'r', encoding='utf-8') as load_f:
            dialog_obj = load(load_f)
            self.dialog = dialog_obj

        self.system_edit.setPlainText(self.dialog['sys']['content'])

        self.update_dialogs()

    def update_dialogs(self):
        self.dialog_list.clear()
        for dialog_obj in self.dialog['li']:
            self.dialog_list.add_item(dialog_obj)

    def clear_dialog(self):
        """ 初始化对话记录 """
        # 清除对话记录
        self.dialog = {'md': '', 'ht': '', 'li': [],
                       'sys': {'role': 'system', 'content': self.system_edit.toPlainText()}}
        # 清除三个框
        self.dialog_list.clear()
        self.input_edit.clear()
        self.log_name_edit.clear()
        # 给定日志默认名称
        self.log_name_edit.setPlaceholderText(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

        self.dialog_fee = 0
        self.token_status_update()

    def save_dialog(self):

        dialog_name = self.log_name_edit.text()
        if not dialog_name:
            dialog_name = self.log_name_edit.placeholderText()

        dialog_file = dialog_name + ".json"
        file_path = os.path.join(self.dialog_path, dialog_file)
        with open(file_path, 'w', encoding='utf-8') as save_f:
            dump(self.dialog, save_f)

    def closeEvent(self, event):
        # 储存窗口大小和位置
        setting.setValue('width', str(self.geometry().width()))
        setting.setValue('height', str(self.geometry().height()))
        setting.setValue('top', str(self.geometry().top()))
        setting.setValue('left', str(self.geometry().left()))
        with open('utility/fee.txt', 'w', encoding='utf-8') as f:
            f.write(str(self.total_fee))
        # 关闭窗口
        event.accept()

    def load_initial_layout_ratio(self):

        restrain_height(self.input_layout_w)
        restrain_height(self.system_layout_w)
        expand_height(self.dialog_list)

    def size_btn_switched(self, button_name, checked=None):
        """ 问题框尺寸改变 """

        if button_name == 'input':
            btn = self.input_size_btn
            widget = self.input_edit
        else:
            btn = self.system_size_btn
            widget = self.system_edit

        if checked is None:
            checked = btn.isChecked()
        else:
            btn.setChecked(checked)

        parent = widget.parent()
        if checked:
            expand_height(parent)
            restrain_height(self.dialog_list)

        else:
            expand_height(self.dialog_list)
            restrain_height(parent)

        widget.setFocus()
        widget.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)

    def pin_on_top(self):
        """ 置顶 """

        btn = self.pin_btn
        if btn.isChecked():
            self.setWindowFlags(self.windowFlags() |
                                Qt.WindowType.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() &
                                ~Qt.WindowType.WindowStaysOnTopHint)
        self.show()
