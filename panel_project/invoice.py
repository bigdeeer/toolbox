# code=UTF-8
import os
import xml.etree.ElementTree as ET
import shutil

folder_path = 'D:/Mega/fapiao/JD'  # Replace with the path to your folder
dest_path = 'D:/Mega/fapiao/JD2'  # Replace with the path to your folder
file_list = os.listdir(folder_path)
xml_set = set()
pdf_set = set()


for file in file_list:
    if ".xml" in file:
        xml_set.add(file)
    elif ".pdf" in file:
        pdf_set.add(file)

pdf_count = 0
print(len(pdf_set))
print(len(xml_set))
new_name_set = set()

for xml_file in xml_set:
    xml_path = os.path.join(folder_path, xml_file)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    total = root.find(".//TotalTax-includedAmount").text
    name = root.find(".//ItemName").text
    name = name.split("*", 1)[1]
    name = name.split("*", 1)[0]

    code_0 = xml_file.rsplit('.xml', 1)[0]
    code = code_0.rsplit('_', 1)[1]

    name_id = name + total
    if name_id in new_name_set:
        name += 'B'
    else:
        new_name_set.add(name_id)

    pdf_source_filename = f"digital_{code}.pdf"
    pdf_source_path = os.path.join(folder_path, pdf_source_filename)
    if os.path.exists(pdf_source_path):
        print('existed')
        pdf_count +=1
    else:
        print(f'no pdf found {pdf_source_filename}')
    pdf_dest_filename = name + total + ".pdf"
    pdf_dest_path = os.path.join(dest_path, pdf_dest_filename)
    shutil.copy(pdf_source_path, pdf_dest_path)

print(pdf_count)
