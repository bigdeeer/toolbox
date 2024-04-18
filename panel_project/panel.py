# coding=utf8
import configparser
import os
import sys
import paramiko
from pygments import highlight
from pygments.lexers.shell import BashLexer
from pygments.formatters import HtmlFormatter
from PySide6.QtCore import QSettings, QThread, Signal
from PySide6.QtGui import QShortcut, QKeySequence, QTextCursor
from PySide6.QtWidgets import QPushButton, QMainWindow, QApplication, QPlainTextEdit, QLineEdit
from ui.panel_ui import Ui_MainWindow

if len(sys.argv) == 2:
    server_type = sys.argv[1]
    key_filename = f"utility/{server_type}.key"
    window_title = server_type
else:
    # master/dev配置文件的文件名
    master_key_file_name = f"utility/master.key"
    dev_key_file_name = e = f"utility/dev.key"

    if os.path.exists(master_key_file_name):
        key_filename = master_key_file_name
        window_title = "master"
    else:
        key_filename = dev_key_file_name
        window_title = "dev"

# 从配置文件读取数据库名称，用户名和密码
config = configparser.ConfigParser()
config.read(key_filename)

host = config['DEFAULT']['host']
username = config['DEFAULT']['username']
password = config['DEFAULT']['password']
port = 22

# 默认设置和本地设置
setting = QSettings('utility/setting.ini', QSettings.Format.IniFormat)

# 创建SSH客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, port=port, username=username, password=password)

# 打开一个交互式shell
shell = client.invoke_shell()


##
def highlighter(input_text):
    """
    使用Pygments对输入的文本进行高亮处理，返回HTML格式的字符串
    :param input_text: 输入的文本
    :return: HTML格式的字符串
    """
    highlighted_text = highlight(input_text, BashLexer(), HtmlFormatter())

    return '<html><head><style>{}</style></head><body>{}</body></html>'.format(
        HtmlFormatter().get_style_defs('.highlight'),
        highlighted_text
    )


class ReceiveStringThread(QThread):
    output_received = Signal(str)

    def __init__(self, shell):
        super().__init__()
        self.shell = shell

    def run(self):
        output = ''
        while True:
            # 读取数据
            data = self.shell.recv(1024).decode('utf-8')
            if data:
                self.output_received.emit(data)


class ControlForm(QMainWindow, Ui_MainWindow):
    console_text = ''

    def __init__(self):
        super().__init__()

        # 初始化所有控件
        self.setupUi(self)
        self.setWindowTitle(window_title)

        # 读取Qt设置文件
        self.load_setting()

        # 信号绑定
        self.signal_connection()

        self.receive_thread = ReceiveStringThread(shell)
        self.receive_thread.output_received.connect(self.update_console_text)
        self.receive_thread.start()

    def update_console_text(self, output):
        self.console_text += output
        self.console.setHtml(highlighter(self.console_text))
        cursor = self.console.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.console.setTextCursor(cursor)

    def load_setting(self):
        """
        从Qt设置文件中读取设置，设置窗口位置和大小，分割位置，以及各个控件的内容
        """
        # 窗体位置
        geo = self.geometry()
        geo.setLeft(int(setting.value('left')))
        geo.setTop(int(setting.value('top')))
        geo.setWidth(int(setting.value('width')))
        geo.setHeight(int(setting.value('height')))
        self.setGeometry(geo)

        # 分割位置
        state = setting.value('spliter')
        self.splitter.restoreState(state)
        self.splitter.setHandleWidth(15)

        # 设置各个控件的内容
        for textbox in self.findChildren(QPlainTextEdit):
            textbox: QPlainTextEdit
            textbox.setPlainText(setting.value(textbox.objectName()))

        for lineedit in self.findChildren(QLineEdit):
            lineedit: QLineEdit
            lineedit.setText(setting.value(lineedit.objectName()))

    def save_setting(self):
        """
        将设置保存到Qt设置文件中
        """
        setting.setValue('width', str(self.geometry().width()))
        setting.setValue('height', str(self.geometry().height()))
        setting.setValue('top', str(self.geometry().top()))
        setting.setValue('left', str(self.geometry().left()))
        setting.setValue('spliter', self.splitter.saveState())

        for textbox in self.findChildren(QPlainTextEdit):
            textbox: QPlainTextEdit
            setting.setValue(textbox.objectName(), textbox.toPlainText())

        for lineedit in self.findChildren(QLineEdit):
            lineedit: QLineEdit
            setting.setValue(lineedit.objectName(), lineedit.text())

    def signal_connection(self):
        """
        绑定各个控件的信号和槽函数
        """
        # 给筛选标签按钮绑定信号
        for btn in self.findChildren(QPushButton):
            btn: QPushButton
            if btn.text() == '发送':
                btn.clicked.connect(self.send_cmd)
            else:
                btn.clicked.connect(self.send_recorded_cmd)

        # 绑定快捷键
        QShortcut(QKeySequence("Ctrl+Return"), self, self.send_cmd)

    def send_cmd(self, cmd=None):
        """
        发送命令到远程主机，并显示输出到控制台
        :param cmd: 要发送的命令，如果为None则从命令输入框中获取
        """
        if not cmd:
            cmd = self.command_text.toPlainText()

        cmd += chr(13)

        # 执行多个命令
        shell.send(cmd)

        self.command_text.clear()
        if not cmd:
            self.command_text.clear()

    def send_recorded_cmd(self):
        """
        发送预定义的命令到远程主机
        """
        btn: QPushButton = self.sender()
        parent_layout = btn.parentWidget().parentWidget()
        textbox: QPlainTextEdit = parent_layout.findChildren(QPlainTextEdit)[0]
        self.send_cmd(textbox.toPlainText())

    def closeEvent(self, event):
        """
        窗口关闭事件，保存设置，关闭SSH连接
        """
        self.save_setting()
        client.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pyqt_form = ControlForm()
    my_pyqt_form.showNormal()

    app.exec()
