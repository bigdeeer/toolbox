from utility.style import color_template

code_color = color_template.get_color('LIGHT','QSS')
code_bg_color = color_template.get_color('DARK_CODE','QSS')
border_color = color_template.get_color('LIGHT','QSS')

CSS_BEGIN = f'''
<!DOCTYPE html>
<html>
<head>
    <style>
    code{{
        color:{code_color};
        background-color: {code_bg_color};
        font-family: JetBrains Mono,consolas;
    }}    
    pre{{
        color:{code_color};
        background-color: {code_bg_color};
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
<td style="border:1px solid {border_color}">
<pre>
'''
CELL_CSS_END = "</pre></td></tr></table>"


