import mistune
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer

class MyRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
        else:
            lexer = guess_lexer(code)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


def markdown_to_html(md):
    """
    将Markdown文本转换为HTML格式。

    :param md: 要转换的Markdown字符串。
    :return: 格式化后的HTML字符串。
    """
    markdown = mistune.Markdown(renderer=MyRenderer())
    ht = markdown(md)

    # 对特定的HTML标签进行自定义替换，以匹配期望的样式。
    ht = ht.replace('\n</code>', '</code>')
    return ht
