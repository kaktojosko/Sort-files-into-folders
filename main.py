import shutil
import os
import datetime

date = str(datetime.date.today())

print(date)
print('The use of a prefix is necessary so that the program does not overwrite some files over others.')
print('Enter 1 if you want to use today\'s date as a prefix when renaming files. ')
rename = input('Enter your own prefix or 1: ')
my_path = input('Enter the absolute path to the folder to sort. Use two slashes instead of one everywhere  \n')

pdf = my_path + '\\PDF'
excel = my_path + '\\Excel'
word = my_path + '\\Word'
pics = my_path + '\\Images'
power_point = my_path + '\\PowerPoint'
other_stuff = my_path + '\\Other stuff'
dirs = ['Excel', 'PDF', 'Word', 'Images', 'PowerPoint', 'Other stuff']


def create_folders():
    try:
        os.mkdir(pdf)
        os.mkdir(excel)
        os.mkdir(word)
        os.mkdir(pics)
        os.mkdir(power_point)
        os.mkdir(other_stuff)
    except OSError:
        pass


def classification():
    folder = os.listdir(my_path)
    while len(folder) > 6:
        folder = os.listdir(my_path)
        try:
            for iterator in folder:
                if iterator.endswith('.pdf'):
                    shutil.move(my_path + '\\' + iterator, pdf + '\\' + iterator)
                elif iterator.endswith('.xlsx') or iterator.endswith('.xlsm') or iterator.endswith('.xls'):
                    shutil.move(my_path + '\\' + iterator, excel + '\\' + iterator)
                elif iterator.endswith('.docx') or iterator.endswith('.doc'):
                    shutil.move(my_path + '\\' + iterator, word + '\\' + iterator)
                elif iterator.endswith('.png') or iterator.endswith('.jpeg') or iterator.endswith('.jpg'):
                    shutil.move(my_path + '\\' + iterator, pics + '\\' + iterator)
                elif iterator.endswith('.pptx') or iterator.endswith('ppt'):
                    shutil.move(my_path + '\\' + iterator, power_point + '\\' + iterator)
                if iterator not in dirs:
                    shutil.move(my_path + '\\' + iterator, other_stuff + '\\' + iterator)
        except FileNotFoundError:
            pass


def renamer(prefix):
    func_folder = os.listdir(my_path)
    for iterator in func_folder:
        if iterator not in dirs and not iterator.startswith(prefix):
            shutil.move(my_path + '\\' + iterator, (my_path + '\\' + prefix + ' ' + iterator))
        else:
            pass

create_folders()

if rename == 1:
    renamer(date)
else:
    renamer(rename)

classification()
