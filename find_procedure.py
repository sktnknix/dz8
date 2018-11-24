import os, win32api, platform, sys

def os_define():
    if platform.system() != 'Windows':
        print("Извините, данный 'шедевр' работает только на Windows")
        return False
    else:
        return True

def find_folders(drive, folder):
    res_folders_list = []
    for root in os.walk(drive):
        if folder.lower() in root[0].lower():
            res_folders_list.append(root[0])
    return res_folders_list

def find_folder_on_drives(folder):
    print('Поиск по всем найденным разделам ...\n')
    res = []
    dict = {}
    _path_to_find = ''
    for drive in win32api.GetLogicalDriveStrings().split('\x00')[:-1]:
        res_folders_list = find_folders(drive, folder)
        res += res_folders_list
    if len(res) != 0:
        _iter = 0
        for _path in res:
            print(str(_iter) + ': ' + _path)
            _iter += 1
    else:
        print('Указанная папка не найдена')
    for _iter in range(len(res)):
        dict[_iter] = res[_iter]
    while 1:
        ent = int(input('\nГде будем искать файлы ? необходимо ввести номер : '))
        if ent not in range(len(res)):
            print('Необходимо ввести номер найденного каталога')
        else:
            _path_to_find = dict[ent]
            break
    return _path_to_find

def find_string(path):
    string = input('Что ищем ? : ')
    found_files = 0
    found_list = []
    for file in os.listdir(path):
        if file.endswith('.sql'):
            found = 0
            with open(os.path.join(path, file), 'r') as sqlfile:
                text = [lines.strip("\n") for lines in sqlfile.readlines()]
                for line in text:
                    if string in line or string.lower() in line or string.upper() in line:
                        found += 1
                if found > 0:
                    found_files += 1
                    print(file)
                    found_list.append(file)
    print('Всего: ' + str(found_files))
    if found_list == []:
        find_string(path)
    else:
        find_in_list(found_list, path)

def find_in_list(found_list, path):
    while 1:
        string = input('Что ищем в полученном списке файлов ? : ')
        found_files = 0
        temp_list = []
        for file in found_list:
            found = 0
            with open(os.path.join(path, file), 'r') as sqlfile:
                text = [lines.strip("\n") for lines in sqlfile.readlines()]
                for line in text:
                    if string in line or string.lower() in line or string.upper() in line:
                        found += 1
                if found > 0:
                    found_files += 1
                    print(file)
                    temp_list.append(file)
        found_list = temp_list
        print('Всего: ' + str(found_files))

if __name__ == '__main__':
    os_def = os_define()
    if not os_def:
        print('Ничего не выйдет, поставьте Windows )))')
        sys.exit()
    else:
        folder = input('Введите папку для поиска (migrations): ')
        path = find_folder_on_drives(folder)
        find_string(path)