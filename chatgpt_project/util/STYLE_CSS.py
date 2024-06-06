BORDER_COLOR = 'rgb(96,96,96)'
DEFAULT_BG = 'rgb(54,57,63)'

CHECKED_BG = 'rgb(78,81,87)'
HOVER_BG = 'rgb(130, 153, 206)'
PRESSED_BG = 'rgb(171, 105, 135)'

MASK_CELL = 'rgb(150, 128, 124)'
CODE_COLOR = 'rgb(192,192,192)'
CODE_BG = 'rgb(41,44,46)'
PRE_COLOR = 'rgb(238, 157, 56)'
PRE_BG = 'rgb(73,68,57)'

CSS_BEGIN = f'''
<!DOCTYPE html>
<html>
<head>
    <style>
    code{{
        color:{PRE_COLOR};
        background-color: {PRE_BG};
        font-family: JetBrains Mono,consolas;
    }}
    pre code{{
        color:{CODE_COLOR};
        background-color: {CODE_BG};
    }}
    table{{
        color:{CODE_COLOR};
        background-color: {CODE_BG};
    }}
    </style>
</head>
<body>
'''

CELL_CSS_BEGIN = f'''
<table border="0" cellspacing="0" cellpadding="10" style="margin-top:10px">
<tr>
<td style="border:1px solid {BORDER_COLOR}">
<pre>
'''
CELL_CSS_END = "</pre></td></tr></table>"

WINDOW_STYLE = f"""
background-color:{DEFAULT_BG};
border:1px solid {BORDER_COLOR};
"""

DEFAULT_BOX_STYLE = f"""background-color:{DEFAULT_BG};
                border:1px solid {BORDER_COLOR};
                color:white"""

BUTTON_STYLE = f"""
QPushButton:checked
{{
background-color: {CHECKED_BG}
}}
QPushButton
{{
background-color:{DEFAULT_BG};
border:1px solid {BORDER_COLOR};
color:white
}}
QPushButton:hover
{{
background-color: {HOVER_BG}
}}
QPushButton:pressed
{{
background-color: {PRESSED_BG};
}}
"""

BUTTON_STYLE_HIDDEN = f"""
QPushButton:checked
{{
background-color: {CHECKED_BG}
}}
QPushButton
{{
background-color:{DEFAULT_BG};
border:0px;
color:white
}}
QPushButton:hover
{{
background-color: {HOVER_BG}
}}
QPushButton:pressed
{{
background-color: {PRESSED_BG};
}}
"""

VBOX_STYLE =  f"""
background-color:{DEFAULT_BG};
border:1px solid {BORDER_COLOR};
color: white;
"""

VBOX_STYLE_MASK =  f"""
background-color:{MASK_CELL};
border:1px solid {BORDER_COLOR};
color: white;
"""

CELL_STYLE =  f"""
QWidget#dialog_item{{
background-color:{DEFAULT_BG};
border:1px solid {BORDER_COLOR};
color: white;
margin:10px;
}}
"""

LABEL_STYLE = f"""
QLabel{{
background-color:{DEFAULT_BG};
border:1px solid {BORDER_COLOR};
color: {PRESSED_BG};
}}
"""

LABEL_HIDDEN = f"""
QLabel{{
background-color:{DEFAULT_BG};
border:0px;
color: {PRESSED_BG};
}}
"""

DIALOG_BOX_STYLE =  f"""
background-color:{DEFAULT_BG};
border:0px;
color: white;
"""
