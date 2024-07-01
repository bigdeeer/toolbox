# code=UTF-8
import os
import shutil

folder_path = 'D:/Mega/fapiao/3/original'  # Replace with the path to your folder
dest_folder_path = 'D:/send'
file_list = os.listdir(folder_path)
file_list = sorted(file_list)

effect_list = []
price = []
total = 0

for index, filename in enumerate(file_list):
    name, extension = os.path.splitext(filename)
    split_i = -1
    for i, letter in enumerate(name):
        if ord('0') <= ord(letter) <= ord('9'):
            split_i = i
            break

    number_str = f"【{index:03d}】"
    new_filename = number_str + filename

    cate = name[:split_i]
    amount = float(name[split_i:])
    total += amount
    effect_list.append(filename)
    price.append(amount)

effect_list = [y for x, y in sorted(zip(price, effect_list))]



with open('fapiao.csv', 'w') as f:
    total = 0

    for index, filename in enumerate(reversed(effect_list)):
        name, extension = os.path.splitext(filename)
        split_i = -1
        for i, letter in enumerate(name):
            if ord('0') <= ord(letter) <= ord('9'):
                split_i = i
                break

        number_str = f"【{index:03d}】"
        new_filename = number_str + filename

        cate = name[:split_i]
        amount = name[split_i:]
        total += float(amount)
        f.write(number_str + ',')
        f.write(cate + ',')
        f.write(amount + '\n')
        source_filepath = os.path.join(folder_path, filename)
        dest_filepath = os.path.join(dest_folder_path, new_filename)
        if total<8574:
            break
        shutil.copy(source_filepath, dest_filepath)

    total = round(total, 2)
    f.write(f"[],总计,{total}")
