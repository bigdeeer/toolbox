import os

folder_path = 'D:/Mega/fapiao/new'  # Replace with the path to your folder
file_list = os.listdir(folder_path)
file_list = sorted(file_list)

with open('fapiao.csv','w') as f:

    for filename in file_list:
        name, extension = os.path.splitext(filename)
        split_i = -1
        for i,letter in enumerate(name):
            if ord('0') <= ord(letter) <= ord('9'):
                split_i = i
                break

        cate = name[:split_i]
        number = name[split_i:]
        f.write(cate + ',')
        f.write(number + '\n')


