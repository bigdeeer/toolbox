BORDER_COLOR = 'rgb(96,96,96)'
DEFAULT_BG = 'rgb(54,57,63)'

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
    pre{{
        color:{CODE_COLOR};
        background-color: {CODE_BG};
        font-family: JetBrains Mono,consolas;
    }}
    .bp {{ color: rgb(255, 198, 0); }}   
    .k {{ color: rgb(130, 177, 255); }}  
    .kn {{ color: rgb(214, 112, 214); }}    
    .kc {{ color: rgb(181, 244, 165);  }} 
    .s2 {{ color: rgb(156, 205, 254); }}   
    .n {{color: rgb(212, 212, 212); }}     
    .nn {{ color: rgb(78, 201, 176); }}      
    .c1 {{ color: rgb(106, 153, 85); }}  
    .o {{color: rgb(206, 145, 120);  }}     
    .nf {{color: rgb(197, 134, 192);}}     
    .sd {{ color: rgb(215, 186, 125); }}
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


