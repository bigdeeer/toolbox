import os.path

import datetime

from sys import argv
from functools import partial
from PySide6.QtWidgets import QLabel, QApplication, QMainWindow, QPushButton, QFileDialog, QSizePolicy, QDoubleSpinBox, \
    QWidget
from PySide6.QtCore import QSettings, QThread, Signal, Qt, QSize, QPoint
from PySide6.QtGui import QPainter, QIcon, QShortcut, QKeySequence, QTextCursor, QImage, QColor, QPixmap
from openai.lib.azure import AzureOpenAI

from ui.chatgpt_ui import Ui_MainWindow
from json import load, dump
from util.STYLE_CSS import *

EXPAND = QSizePolicy.Policy.Expanding
FIXED = QSizePolicy.Policy.Fixed


class GptWorker(QThread):
    answerAvailable = Signal(str, list)  # 定义一个信号，用于传递结果
    message = []
    message_sys = ''
    temperature = 0.1
    top_p = 0.1
    model = ''

    def run(self):
        answer_str, tokens = get_gpt_answer(self.message, self.message_sys, self.temperature, self.top_p,
                                            self.model)  # 调用你的函数获取答案
        self.answerAvailable.emit(answer_str, tokens)  # 发送信号


def get_gpt_answer(message, message_sys, temperature, top_p, model):
    try:
        full_message = [message_sys] + message
        response = client.chat.completions.create(
            model=model,
            messages=full_message,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        answer_str = response.choices[0].message.content
        tokens = [response.usage.prompt_tokens, response.usage.completion_tokens]

    except Exception as e:
        answer_str = '请求回答时出现错误，错误内容为:\n' + str(e)
        tokens = [0, 0]
    return answer_str, tokens


setting = QSettings('util/setting.ini', QSettings.Format.IniFormat)

with open('util/api_key.txt', 'r', encoding='utf-8') as f:
    azure_endpoint = f.readline().strip()
    api_key = f.readline().strip()

with open('util/fee.txt', 'r', encoding='utf-8') as f:
    total_fee = float(f.readline().strip())
    print(total_fee)

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version="2023-05-15"
)




worker = GptWorker()

icon_dict = {"model_btn": [{'state': QIcon.State.On, 'file': "icon/gpt4.png"},
                           {'state': QIcon.State.Off, 'file': "icon/gpt35.png"}],
             "save_btn": [{'state': QIcon.State.Off, 'file': "icon/save.png"}],
             "load_btn": [{'state': QIcon.State.Off, 'file': "icon/load.png"}],
             "frame_btn": [{'state': QIcon.State.On, 'file': "icon/frame.png"},
                           {'state': QIcon.State.Off, 'file': "icon/frameless.png"}],
             "pin_btn": [{'state': QIcon.State.On, 'file': "icon/pin.png"},
                         {'state': QIcon.State.Off, 'file': "icon/pinoff.png"}],
             "min_btn": [{'state': QIcon.State.Off, 'file': "icon/min.png"}],
             "max_btn": [{'state': QIcon.State.On, 'file': "icon/mid.png"},
                         {'state': QIcon.State.Off, 'file': "icon/max.png"}],
             "close_btn": [{'state': QIcon.State.Off, 'file': "icon/close.png"}],
             "system_size_btn": [{'state': QIcon.State.On, 'file': "icon/down.png"},
                                 {'state': QIcon.State.Off, 'file': "icon/up.png"}],
             "input_size_btn": [{'state': QIcon.State.On, 'file': "icon/down.png"},
                                {'state': QIcon.State.Off, 'file': "icon/up.png"}],
             "send_btn": [{'state': QIcon.State.Off, 'file': "icon/send.png"}],
             "clear_btn": [{'state': QIcon.State.Off, 'file': "icon/clear.png"}]
             }


def restrain_height(widget: QWidget):
    height = widget.minimumHeight()
    widget.setMaximumHeight(height)
    widget.setSizePolicy(EXPAND, FIXED)


def expand_height(widget: QWidget):
    widget.setMaximumHeight(8000)
    widget.setSizePolicy(EXPAND, EXPAND)


class ChatForm(QMainWindow, Ui_MainWindow):
    dialog = {}
    unit = 0
    size = 0
    gap_0 = 0
    gap_1 = 0
    geo = None
    dialog_fee = 0

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setupUi(self)  # 初始化所有控件

        self.load_style()

        self.update_icon_color(QColor(187, 206, 251))

        self.setWindowTitle('Azure-openAI-GPT创新研发部')
        self.setWindowIcon(QIcon('icon\logo.png'))

        self.load_settings()  # 读取布局参数

        # 根据历史纪录读取窗体位置和大小
        geo = self.geometry()
        geo.setLeft(int(setting.value('left')))
        geo.setTop(int(setting.value('top')))
        geo.setWidth(int(setting.value('width')))
        geo.setHeight(int(setting.value('height')))
        self.setGeometry(geo)

        # 五个按钮的信号
        self.send_btn.clicked.connect(self.send_question)
        self.clear_btn.clicked.connect(self.init)
        self.save_btn.clicked.connect(self.save_log)
        self.load_btn.clicked.connect(self.load_log)
        self.input_size_btn.clicked.connect(partial(self.size_btn_switched, 'input'))
        self.system_size_btn.clicked.connect(partial(self.size_btn_switched, 'system'))

        self.pin_btn.clicked.connect(self.pin_on_top)

        self.system_edit.textChanged.connect(self.sys_changed)
        self.input_edit.textChanged.connect(self.input_changed)

        # 键盘快捷键
        QShortcut(QKeySequence("Ctrl+Return"), self, self.send_question)
        QShortcut(QKeySequence("Ctrl+Up"), self, self.input_size_btn.click)
        QShortcut(QKeySequence("Ctrl+Down"), self, self.system_size_btn.click)

        # 开启进程
        worker.answerAvailable.connect(self.receive_answer)  # updateUI是一个更新UI的函数

        self.load_layput_size()  # 修改布局尺寸

        self.init()

    def load_style(self):
        self.setStyleSheet(WINDOW_STYLE)
        box_list = [self.log_name_edit, self.system_edit, self.input_edit]
        for box in box_list:
            box.setStyleSheet(DEFAULT_BOX_STYLE)

        for button in self.findChildren(QPushButton):
            button: QPushButton
            button.setStyleSheet(BUTTON_STYLE)

        for vbox in self.findChildren(QDoubleSpinBox):
            vbox: QDoubleSpinBox
            vbox.setStyleSheet(VBOX_STYLE)

        self.model_combo.setStyleSheet(VBOX_STYLE)
        for label in self.token_disp_layout_w.findChildren(QLabel):
            label.setStyleSheet(LABEL_STYLE)

        self.dialog_list.setStyleSheet(DIALOG_BOX_STYLE)

    def update_icon_color(self, color):
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

    def load_settings(self):
        self.size = int(setting.value('font'))
        self.gap_0 = int(setting.value('gap_0'))
        self.gap_1 = int(setting.value('gap_1'))
        self.temp_vbox.setValue(float(setting.value('temperature')))
        self.topp_vbox.setValue(float(setting.value('topp')))

    def record_to_dialog(self, dialog_obj, save=True):

        # 存入字典列表
        self.dialog['li'].append(dialog_obj)

        self.dialog_list.add_item(dialog_obj)

        if save:
            self.save_log()

    def input_changed(self):
        # 存入字典列表
        di = {'role': 'user', 'content': self.input_edit.toPlainText()}
        full_message = [self.dialog['sys']] + self.dialog['li'] + [di]

    def calculate_price(self, prompt=0, completion=0):
        if self.model_combo.currentText() == '3.5-4K':
            price_input = 0.5
            price_output = 1.5
        else:
            price_input = 5
            price_output = 15
        fee = (prompt * price_input + completion * price_output) * 7 / 1000000
        fee = round(fee, 5)
        count = prompt + completion
        txt = f"{fee:.4f}({count})"
        return txt, fee

    def token_status_update(self, tokens=None):

        if not tokens:
            prompt = completion = 0
        else:
            prompt, completion = tokens

        actual_txt = ""
        global total_fee

        feetxt, fee = self.calculate_price(prompt=prompt)
        total_fee += fee
        self.dialog_fee += fee
        actual_txt += f"[LastPrompt] = {feetxt}   "

        feetxt, fee = self.calculate_price(completion=completion)
        total_fee += fee
        self.dialog_fee += fee
        actual_txt += f"[LastAnswer] = {feetxt}"

        self.actual_token_disp.setText(actual_txt)

        fee = self.dialog_fee
        sum_txt = f"[DialogTotal] = {fee:.4f}   [UserTotal] = {total_fee:.4f}"
        self.sum_token_disp.setText(sum_txt)

    def sys_changed(self):
        self.dialog['sys']['content'] = self.system_edit.toPlainText()

    def send_question(self):
        # 获取问题
        question = self.input_edit.toPlainText()
        self.input_edit.clear()

        # 刷新问题框状态
        self.size_btn_switched('input', checked=False)
        self.size_btn_switched('system', checked=False)

        dialog_obj = {'role': 'user', 'content': question}
        self.record_to_dialog(dialog_obj)

        # 启动回答进程
        worker.message = self.dialog['li']
        worker.message_sys = self.dialog['sys']
        worker.temperature = self.temp_vbox.value()
        worker.top_p = self.topp_vbox.value()
        if self.model_combo.currentText() == '3.5-4k':
            worker.model = "deer-gpt-35-turbo"
        else:
            worker.model = "deer-gpt-4o"
        worker.start()

        self.input_edit.setPlainText(f"Waiting for answer ...")

    def receive_answer(self, answer, tokens):

        dialog_obj = {'role': 'assistant', 'content': answer}
        self.record_to_dialog(dialog_obj)

        # 关闭回答进程
        worker.quit()
        self.input_edit.setPlainText("")
        self.token_status_update(tokens=tokens)

    def save_log(self):
        pass
        # 尝试获取名称
        name = self.log_name_edit.text()
        # 名称已经给定
        if name != '':
            log_path = 'named_log/'
        # 未给定名称，使用时间作为日志名称
        else:
            name = self.log_name_edit.placeholderText()
            log_path = 'log/'
        # 写入日志
        with open(log_path + name + '.json', 'w', encoding='utf-8') as save_f:
            list_to_save = [self.dialog['sys']] + self.dialog['li']
            dump(list_to_save, save_f)

    def load_log(self):
        load_path = QFileDialog.getOpenFileName(dir='named_log/')[0]
        if load_path:
            self.init()
            self.log_name_edit.setText(os.path.basename(load_path).rsplit('.', 1)[0] + '_new')

            with open(load_path, 'r', encoding='utf-8') as load_f:
                list_to_load = load(load_f)
                self.dialog['sys'] = list_to_load[0]

            self.system_edit.setPlainText(self.dialog['sys']['content'])
            for obj in list_to_load[1:]:
                self.record_to_dialog(obj, save=False)

    def init(self):
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

    def close_window(self):
        self.close()

    def closeEvent(self, event):
        # 储存窗口大小和位置
        setting.setValue('width', str(self.geometry().width()))
        setting.setValue('height', str(self.geometry().height()))
        setting.setValue('top', str(self.geometry().top()))
        setting.setValue('left', str(self.geometry().left()))
        setting.setValue('temperature', str(self.temp_vbox.value()))
        setting.setValue('topp', str(self.topp_vbox.value()))
        with open('util/fee.txt', 'w', encoding='utf-8') as f:
            f.write(str(total_fee))
        # 关闭窗口
        event.accept()

    def load_layput_size(self):
        # 设定字体
        font = self.input_edit.font()
        font.setPointSize(self.size)
        self.input_edit.setFont(font)
        self.system_edit.setFont(font)

        self.log_name_edit.setFont(font)

        self.unit = max(self.size * 2 + 9, 24)
        for button in self.findChildren(QPushButton):
            button.setFixedWidth(self.unit)
            button.setFixedHeight(self.unit)

        self.centralwidget.layout().setSpacing(self.gap_0)
        self.centralwidget.setContentsMargins(self.gap_0, self.gap_0, self.gap_0, self.gap_0)
        self.log_layout_w.layout().setSpacing(self.gap_1)
        self.system_layout_w.layout().setSpacing(self.gap_1)
        self.input_layout_w.layout().setSpacing(self.gap_1)
        self.button_layout_w.layout().setSpacing(self.gap_1)

        self.log_layout_w.setFixedHeight(self.unit)
        self.token_disp_layout_w.setFixedHeight(self.unit)

        self.dialog_list.setMinimumHeight(self.unit * 2)
        self.input_layout_w.setMinimumHeight(self.unit * 3 + 8)
        self.system_layout_w.setMinimumHeight(self.unit)

        restrain_height(self.input_layout_w)
        restrain_height(self.system_layout_w)
        expand_height(self.dialog_list)

    def size_btn_switched(self, button_name, checked=None):  # 问题框尺寸改变
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
        btn = self.pin_btn
        if btn.isChecked():
            self.setWindowFlags(self.windowFlags() |
                                Qt.WindowType.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() &
                                ~Qt.WindowType.WindowStaysOnTopHint)
        self.show()


if __name__ == '__main__':
    app = QApplication(argv)
    my_pyqt_form = ChatForm()
    my_pyqt_form.show()
    app.exec()
