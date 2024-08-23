import yaml
import os

"""
用于各类格式文件的读取和写入
"""


class Settings:
    """用于程序的配置/设置的类

    读取和写入配置文件
    """

    def __init__(self):
        # 配置文件名称及路径
        self.items = {}
        self.private_items = {}

        self.file_name = "settings.yaml"
        self.file_path = os.path.join(os.path.dirname(__file__), self.file_name)

        # 检查配置文件是否存在，不存在就新建文件
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding="utf-8") as f:
                pass
        self.load()

    def load(self):
        """
        加载yaml文件::
        """
        with open(self.file_path, 'r', encoding="utf-8") as f:
            self.items = yaml.safe_load(f)

    def save(self, params):
        """
        保存配置文件:
        :param width
        :param height
        :param top
        :param left
        :param name
        :return:
        """
        with open(self.file_path, 'w', encoding="utf-8") as f:
            yaml.dump(params, f, allow_unicode=True)


setting = Settings()
