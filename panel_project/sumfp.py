# code=UTF-8
import os

folder_path = 'D:/send'  # Replace with the path to your folder
file_list = os.listdir(folder_path)
file_list = sorted(file_list)

with open('fapiao.csv', 'w') as f:
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
        amount = name[split_i:]
        total += float(amount)
        f.write(number_str + ',')
        f.write(cate + ',')
        f.write(amount + '\n')
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    total = round(total, 2)
    f.write(f"[],总计,{total}")
