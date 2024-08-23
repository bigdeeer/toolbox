from http import HTTPStatus

import dashscope
from PySide6.QtCore import QThread, Signal
from dashscope import Generation

with open('utility/api_key.txt', 'r', encoding='utf-8') as f:
    dashscope.api_key = f.readline().strip()

TOKEN_PRICE = {
    "qwen-turbo": {'in': 0.002, 'out': 0.006},
    "qwen-plus": {'in': 0.004, 'out': 0.012},
    "qwen-max": {'in': 0.04, 'out': 0.12}
}


class LLMWorker(QThread):
    dialogs = {}
    answer_received = Signal(dict)

    def run(self):
        self.get_qwen_answer()  # 使用通义千问获取答案

    def get_qwen_answer(self):
        """ 获取通义千问的回答 """

        response = Generation.call(
            model=self.dialogs['model'],
            messages=[self.dialogs['sys']] + self.dialogs['messages'],
            temperature=self.dialogs['temp'],
            top_p=self.dialogs['topp'],
            top_k=self.dialogs['topk'],
            enable_search=True,
            result_format="message"
        )

        if response.status_code == HTTPStatus.OK:

            in_tokens = response.usage.input_tokens
            out_tokens = response.usage.output_tokens

            in_tokens_fee = in_tokens * TOKEN_PRICE[self.dialogs['model']]['in'] / 1000
            out_tokens_fee = out_tokens * TOKEN_PRICE[self.dialogs['model']]['out'] / 1000
            total = self.dialogs['fee'] + in_tokens_fee + out_tokens_fee

            answer_obj = {
                'answer': response.output.choices[0].message.content,
                'success': True,
                'in_tokens': in_tokens,
                'out_tokens': out_tokens,
                'in_tokens_fee': in_tokens_fee,
                'out_tokens_fee': out_tokens_fee,
                'fee': total
            }

        else:
            answer_obj = {
                'answer': response.message,
                'success': False
            }

        self.answer_received.emit(answer_obj)
