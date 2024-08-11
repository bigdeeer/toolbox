from PySide6.QtCore import QThread, Signal
from openai import OpenAI
from openai.lib.azure import AzureOpenAI

with open('utility/api_key.txt', 'r', encoding='utf-8') as f:
    azure_endpoint = f.readline().strip()
    api_key = f.readline().strip()

with open('utility/fee.txt', 'r', encoding='utf-8') as f:
    total_fee = float(f.readline().strip())


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
    """ 获取GPT回答 """

    if model.startswith("qwen"):  # 使用阿里的模型
        client = OpenAI(
            api_key="sk-16435c32fce6449abe78bd13bfad3f64",  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务的base_url
        )
    else:  # 使用Azure的 openAI 模型
        client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version="2023-05-15"
        )
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

