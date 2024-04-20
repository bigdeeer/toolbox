import datetime
import os.path

import tiktoken

from sys import argv
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QSizePolicy, QDoubleSpinBox, QWidget
from PySide6.QtCore import QSettings, QThread, Signal, Qt, QSize, QPoint
from PySide6.QtGui import QPainter, QIcon, QShortcut, QKeySequence, QTextCursor, QImage, QColor, QPixmap
from openai.lib.azure import AzureOpenAI

from ui.chatgpt_ui import Ui_MainWindow
from mistune import html
from json import load, dump
from util.STYLE_CSS import *


def markdown_to_html(md):
    ht = html(md)
    ht = html(md)
    ht = ht.replace('\n</code>', '</code>')
    ht = ht.replace('<pre>', CELL_CSS_BEGIN)
    ht = ht.replace('</pre>', CELL_CSS_END)
    return ht


class GptWorker(QThread):
    answerAvailable = Signal(str)  # 定义一个信号，用于传递结果
    message = []
    message_sys = ''
    temperature = 0.1
    top_p = 0.1
    model = ''

    def run(self):
        answer_str = get_gpt_answer(self.message, self.message_sys, self.temperature, self.top_p,
                                    self.model)  # 调用你的函数获取答案
        self.answerAvailable.emit(answer_str)  # 发送信号


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
        print(response.usage.prompt_tokens)
        print(response.usage.completion_tokens)
        print(response.usage.total_tokens)
        token_count = num_tokens_from_messages(full_message)
        print('-----')
        print(token_count)

    except Exception as e:
        answer_str = '请求回答时出现错误，错误内容为:\n' + str(e)
    return answer_str


role_dict = {'## Q:': 'user', '## A:': 'assistant'}
setting = QSettings('util/setting.ini', QSettings.Format.IniFormat)

with open('util/api_key.txt', 'r', encoding='utf-8') as f:
    azure_endpoint = f.readline().strip()
    api_key = f.readline().strip()

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    api_version="2023-05-15"
)


def num_tokens_from_messages(messages):
    """Return the number of tokens used by a list of messages."""

    encoding = tiktoken.get_encoding("cl100k_base")

    tokens_per_message = 3
    tokens_per_name = 1

    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


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


def change_size(widget: QWidget, width=-1, height=-1):
    if width != -1:
        widget.setMaximumWidth(width)
    if height != -1:
        widget.setMaximumHeight(height)


class ChatForm(QMainWindow, Ui_MainWindow):
    dialog = {}
    unit = 0
    size = 0
    gap_0 = 0
    gap_1 = 0
    geo = None

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setupUi(self)  # 初始化所有控件

        self.load_style()

        self.update_icon_color(BORDER_COLOR)

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

        # 键盘快捷键
        QShortcut(QKeySequence("Ctrl+Return"), self, self.send_question)
        QShortcut(QKeySequence("Ctrl+E"), self, self.edit_dialog)
        QShortcut(QKeySequence("Ctrl+S"), self, self.save_html)
        QShortcut(QKeySequence("Ctrl+Up"), self, self.input_size_btn.click)
        QShortcut(QKeySequence("Ctrl+Down"), self, self.system_size_btn.click)

        # 开启进程
        worker.answerAvailable.connect(self.receive_answer)  # updateUI是一个更新UI的函数

        self.load_layput_size()  # 修改布局尺寸

        self.init()

        # colorx = QColorDialog.getColor(0, None, "Select Color")
        # print(colorx)

    def load_style(self):
        self.setStyleSheet(WINDOW_STYLE)
        box_list = [self.log_name_edit, self.dialog_edit, self.system_edit, self.input_edit,self.token_disp]
        for box in box_list:
            box.setStyleSheet(DEFAULT_BOX_STYLE)

        for button in self.findChildren(QPushButton):
            button: QPushButton
            button.setStyleSheet(BUTTON_STYLE)

        for vbox in self.findChildren(QDoubleSpinBox):
            vbox: QDoubleSpinBox
            vbox.setStyleSheet(VBOX_STYLE)

        self.model_combo.setStyleSheet(VBOX_STYLE)

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
                    result.fill(QColor(200, 200, 200))
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

    def edit_dialog(self):
        if self.dialog_edit.isReadOnly():
            self.dialog_edit.setReadOnly(False)
            self.dialog_edit.setPlainText(self.dialog['md'])
        else:
            self.dialog_edit.setReadOnly(True)

            md = self.dialog_edit.toPlainText()
            self.dialog['md'] = md

            ht = markdown_to_html(md)
            self.dialog['ht'] = ht
            self.dialog_edit.setHtml(CSS_BEGIN + self.dialog['ht'] + "</body></html>")

            self.dialog['li'] = []
            role = ''
            content_list = []
            lines = md.splitlines()
            for line in lines:
                if line == '## Q:' or line == '## A:':
                    if content_list:
                        self.dialog['li'].append({'role': role, 'content': '\n'.join(content_list)})
                    role = role_dict[line]
                    content_list = []
                else:
                    content_list.append(line + '\n')
            self.dialog['li'].append({'role': role, 'content': '\n'.join(content_list)})

            # 保存日志
            self.save_log()

    def record_to_dialog(self, msg, role, save=True):

        # 存入字典列表
        di = {'role': role, 'content': msg}
        self.dialog['li'].append(di)

        # 存入md
        if role == 'user':
            md_div = '## Q:''\n'
        else:
            md_div = '## A:''\n'

        md = md_div + msg + '\n'
        self.dialog['md'] += md

        # 转为html
        ht = markdown_to_html(md)
        self.dialog['ht'] += ht
        self.dialog_edit.setHtml(CSS_BEGIN + self.dialog['ht'] + "</body></html>")
        self.dialog_edit.verticalScrollBar().setValue(self.dialog_edit.verticalScrollBar().maximum())

        if save:
            self.save_log()

    def sys_changed(self):
        self.dialog['sys']['content'] = self.system_edit.toPlainText()

    def send_question(self):
        # 获取问题
        question = self.input_edit.toPlainText()
        self.input_edit.clear()

        # 刷新问题框状态
        self.size_btn_switched('input', checked=False)
        self.size_btn_switched('system', checked=False)

        self.record_to_dialog(question, 'user')

        # 启动回答进程
        worker.message = self.dialog['li']
        worker.message_sys = self.dialog['sys']
        worker.temperature = self.temp_vbox.value()
        worker.top_p = self.topp_vbox.value()
        if self.model_combo.currentText() == '3.5-4k':
            worker.model = "deer-gpt-35-turbo"
        else:
            worker.model = "deer-gpt-35-turbo-16k"
        worker.start()

        self.input_edit.setPlainText("Waiting for answer...")

    def receive_answer(self, answer):

        self.record_to_dialog(answer, 'assistant')
        # 关闭回答进程
        worker.quit()

        self.input_edit.setPlainText("")

    def save_log(self):
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

    def save_html(self):
        name = self.log_name_edit.text()
        # 名称已经给定
        if name != '':
            log_path = 'named_log/'
        # 未给定名称，使用时间作为日志名称
        else:
            name = self.log_name_edit.placeholderText()
            log_path = 'log/'
        with open(log_path + name + '.html', 'w', encoding='utf-8') as save_f:
            save_f.write(self.dialog_edit.toHtml())

    def load_log(self):
        load_path = QFileDialog.getOpenFileName(dir='named_log/')[0]
        if load_path:
            self.init()
            self.log_name_edit.setText(os.path.basename(load_path).rsplit('.', 1)[0] + '_new')

            with open(load_path, 'r', encoding='utf-8') as load_f:
                list_to_load = load(load_f)
                self.dialog['sys'] = list_to_load[0]

            self.system_edit.setPlainText(self.dialog['sys']['content'])
            for dc in list_to_load[1:]:
                self.record_to_dialog(dc['content'], dc['role'], save=False)

    def init(self):
        # 清除对话记录
        self.dialog = {'md': '', 'ht': '', 'li': [],
                       'sys': {'role': 'system', 'content': self.system_edit.toPlainText()}}
        # 清除三个框
        self.dialog_edit.clear()
        self.input_edit.clear()
        self.log_name_edit.clear()
        self.dialog_edit.setReadOnly(True)
        # 给定日志默认名称
        self.log_name_edit.setPlaceholderText(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

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
        # 关闭窗口
        event.accept()

    def load_layput_size(self):
        # 设定字体
        font = self.input_edit.font()
        font.setPointSize(self.size)
        self.input_edit.setFont(font)
        self.system_edit.setFont(font)
        self.dialog_edit.setFont(font)
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
        self.dialog_layout_w.layout().setSpacing(self.gap_1)

        self.log_layout_w.setFixedHeight(self.unit)
        change_size(self.input_layout_w, height=self.unit * 3 + 4)
        change_size(self.system_layout_w, height=self.unit)

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

        self.widget_size_update(widget, checked)

    def widget_size_update(self, widget, checked):
        parent = widget.parent()
        if checked:
            self.old_box_height = parent.height()
            self.old_dialog_height = self.dialog_layout_w.height()
            change_size(self.dialog_layout_w, height=self.unit * 2)
            change_size(parent, height=self.height())



        else:
            change_size(self.dialog_layout_w, height=self.old_dialog_height)
            change_size(parent, height=self.old_box_height)

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
