import copy
import os
import datetime
from json import load, dump
from functools import partial
# pyside6
from PySide6.QtCore import QSize
from PySide6.QtGui import QShortcut, QKeySequence, QTextCursor
from PySide6.QtWidgets import QListWidgetItem
# custom
from func.layout_func import restrain_height, expand_height
from func.workers import LLMWorker
# UI
from windows.borderless_window import BorderLessWindow

# 异步线程
worker = LLMWorker()


class ChatForm(BorderLessWindow):
    """ AI 工具主界面"""

    dialogs = []  # 对话列表
    current_i = -1  # 当前对话编号
    dialog_path = 'dialog_history/'  # 历史对话路径

    def __init__(self):
        super().__init__()

        # 初始化三个布局的比例
        self.ui_load_initial_layout_ratio()
        # 加载样式
        self.load_style()  # 样式
        self.connect_signals()
        self.dialog_list_load()

    def connect_signals(self):
        """ 初始化信号 """

        # 对话按钮
        self.send_btn.clicked.connect(self.dialog_send_question)
        self.input_size_btn.clicked.connect(partial(self.ui_size_switched, 'input'))
        self.system_size_btn.clicked.connect(partial(self.ui_size_switched, 'system'))

        # 对话列表按钮
        self.new_dialog_btn.clicked.connect(self.dialog_create_new)
        self.del_dialog_btn.clicked.connect(self.dialog_delete)

        # 键盘快捷键
        QShortcut(QKeySequence("Ctrl+Return"), self, self.dialog_send_question)
        QShortcut(QKeySequence("Ctrl+Up"), self, self.input_size_btn.click)
        QShortcut(QKeySequence("Ctrl+Down"), self, self.system_size_btn.click)

        # 左侧对话列表的当前选择项变化
        self.dialog_list_widget.itemClicked.connect(self.dialog_params_load)

        self.param_name_lineedit.textEdited.connect(self.dialog_name_changed)

        # 异步线程收到回答后的处理
        worker.answer_received.connect(self.dialog_receive_answer)  # updateUI是一个更新UI的函数

    def dialog_list_load(self):
        """ 加载菜单对话 """

        # 遍历对话文件夹内所有json文件
        dialog_files = os.listdir(self.dialog_path)

        for file_name in dialog_files:
            if not file_name.endswith('.json'):
                continue

            # 获取对话文件路径称
            file_path = os.path.join(self.dialog_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as load_f:
                dialog_obj = load(load_f)

            self.dialogs.append(dialog_obj)

            dialog_name = dialog_obj['name']

            dialog_item = QListWidgetItem(dialog_name)
            dialog_item.setSizeHint(QSize(0, 30))
            self.dialog_list_widget.addItem(dialog_item)

        i = self.setting_params['prev_dialog_index']
        if i >= 0:
            self.dialog_list_widget.setCurrentRow(i)
            self.dialog_params_load(save=False)

    def dialog_append_message(self, message_obj):
        """ 将消息存入对话 """

        current_dialog: dict = self.dialogs[self.current_i]
        current_dialog['messages'].append(message_obj)
        self.dialog_widget.add_item(message_obj)

    def dialog_create_new(self):

        # 给定日志默认名称
        create_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S%f")

        if self.dialog_list_widget.count() > 0:
            prev_dialog = self.dialogs[self.current_i]
            new_dialog = copy.deepcopy(prev_dialog)
        else:
            new_dialog = {
                'sys': {
                    'role': 'system',
                    'content': ''
                },
                'model': 'qwen-turbo',
                'temp': 0.2,
                'topp': 0.2,
                'topk': 20,
            }
        new_dialog_update = {
            'messages': [],
            'input': "",
            'name': create_time,
            'time': create_time,
            'fee': 0,
            'in_tokens': 0,
            'out_tokens': 0,
            'in_tokens_fee': 0,
            'out_tokens_fee': 0
        }
        new_dialog.update(new_dialog_update)

        dialog_item = QListWidgetItem(create_time)
        dialog_item.setSizeHint(QSize(0, 30))
        self.dialog_list_widget.addItem(dialog_item)

        self.dialogs.append(new_dialog)

        i = self.dialog_list_widget.count() - 1
        self.dialog_list_widget.setCurrentRow(i)
        self.dialog_params_load()

    def dialog_delete(self):

        dialog_time = self.dialogs[self.current_i]['time']
        self.file_remove(dialog_time)

        self.item_is_deleting = True
        self.dialogs.pop(self.current_i)
        self.dialog_list_widget.takeItem(self.current_i)

        if self.dialog_list_widget.count() == 0:
            self.current_i = -1
            return

        i = max(0, self.current_i - 1)
        self.dialog_list_widget.setCurrentRow(i)
        self.dialog_params_load(save=False)

    def dialog_send_question(self):
        """ 发送问题 """
        self.dialog_params_save()

        self.input_edit.clear()

        # 刷新问题框状态
        self.ui_size_switched('input', checked=False)
        self.ui_size_switched('system', checked=False)

        current_dialog = self.dialogs[self.current_i]

        dialog_obj = {'role': 'user', 'content': current_dialog['input']}
        self.dialog_append_message(dialog_obj)

        # 启动回答进程
        worker.dialogs = current_dialog
        worker.start()

        self.input_edit.setPlainText(f"等待回答...")

    def dialog_receive_answer(self, answer_obj):
        """ 接收回答 """

        # 关闭回答进程
        worker.quit()

        answer = answer_obj['answer']

        message_obj = {'role': 'assistant', 'content': answer}
        self.dialog_append_message(message_obj)

        self.input_edit.setPlainText("")

        if not answer_obj['success']:
            return

        del answer_obj['answer']
        del answer_obj['success']

        current_dialog = self.dialogs[self.current_i]
        current_dialog.update(answer_obj)

        self.dialog_token_update()

    def dialog_params_load(self, item=None, save=True):
        """ 切换对话 """
        if save:
            self.dialog_params_save()

        self.current_i = self.dialog_list_widget.currentRow()

        current_dialog: dict = self.dialogs[self.current_i]

        # 参数加载
        self.param_temp_spin.setValue(current_dialog['temp'])
        self.param_topp_spin.setValue(current_dialog['topp'])
        self.param_topk_spin.setValue(current_dialog['topk'])
        self.param_model_combo.setCurrentText(current_dialog['model'])
        self.param_name_lineedit.setText(current_dialog['name'])

        # 输入框加载
        self.system_edit.setPlainText(current_dialog['sys']['content'])
        self.input_edit.setPlainText(current_dialog['input'])

        # 对话加载
        self.dialog_widget.clear()
        for dialog in current_dialog['messages']:
            self.dialog_widget.add_item(dialog)

        self.dialog_token_update()

    def dialog_params_save(self):
        if self.current_i == -1:
            return

        dialog_params = {
            'temp': self.param_temp_spin.value(),
            'topp': self.param_topp_spin.value(),
            'topk': int(self.param_topk_spin.value()),
            'model': self.param_model_combo.currentText(),
            'name': self.param_name_lineedit.text(),
            'sys': {
                'role': 'system',
                'content': self.system_edit.toPlainText()
            },
            'input': self.input_edit.toPlainText()
        }
        current_dialog = self.dialogs[self.current_i]
        current_dialog.update(dialog_params)

    def dialog_token_update(self):
        current_dialog = self.dialogs[self.current_i]
        in_tokens = current_dialog.get('in_tokens', 0)
        out_tokens = current_dialog.get('out_tokens', 0)
        in_tokens_fee = current_dialog.get('in_tokens_fee', 0)
        out_tokens_fee = current_dialog.get('out_tokens_fee', 0)
        total = current_dialog['fee']

        token_str = (f"上一次提问{in_tokens_fee:6f}({in_tokens})---"
                     f"上一次回答{out_tokens_fee:6f}({out_tokens})---"
                     f"对话总计{total:6f}")
        self.dialog_token_label.setText(token_str)

    def dialog_name_changed(self):
        dialog_name = self.param_name_lineedit.text()
        self.dialog_list_widget.item(self.current_i).setText(dialog_name)

    def dialog_list_save(self):

        self.setting_params['prev_dialog_index'] = self.current_i

        for dialog_obj in self.dialogs:
            dialog_file_name = dialog_obj['time'] + '.json'
            dialog_path = os.path.join(self.dialog_path, dialog_file_name)

            with open(dialog_path, 'w', encoding='utf-8') as save_f:
                dump(dialog_obj, save_f)

    def file_remove(self, dialog_time):

        dialog_file_name = dialog_time + '.json'
        dialog_path = os.path.join(self.dialog_path, dialog_file_name)

        if os.path.exists(dialog_path):
            os.rename(dialog_path, dialog_path + '.bak')

    def ui_load_initial_layout_ratio(self):

        restrain_height(self.input_layout_w)
        restrain_height(self.system_layout_w)
        expand_height(self.dialog_widget)

    def ui_size_switched(self, button_name, checked=None):
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
            restrain_height(self.dialog_widget)

        else:
            expand_height(self.dialog_widget)
            restrain_height(parent)

        widget.setFocus()
        widget.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)

    def closeEvent(self, event):
        """
        退出，保存设置
        :param event:
        :return:
        """
        self.dialog_params_save()
        self.dialog_list_save()
        self.save_setting()
        event.accept()
