#manager defs
import os
import shutil
r00t = os.getcwd()+'\\root' #переменная пути к папке



def cwd (*arg): # текущее расположение

    return print("\\"+os.getcwd()[len(r00t)+1:])

def mkfol(*arg): #создание папки
    try:
        os.mkdir(arg[0][0])
        return 'Ok!'
    except TypeError:
        return print('Нет параметра')
    
def delfol(*arg):# удаление папки
    try:
        if arg == None: return print('Отсутствует параметр!')
        os.rmdir(arg[0][0])
        return 'ok' 
    except IndexError:
        return print('Нет параметра!')
    except OSError:
        return print('Папка не пуста')
    
def chfol(*arg):# перемещение из папки
    if arg[0][0] == '..' and os.getcwd()==r00t:
        return print('Запрещено')
    try:
        os.chdir(arg[0][0])
    except IndexError:
        return print('Нет параметра')
    except OSError:
        return print('Ошибка в параметре')

def mkfile(*arg):# создание файла
    try:
        if arg[0] == None: return print('Отсутствует параметр!')
        txt_file = open(arg[0][0],'w')
        txt_file.close()
        return 'ok'
    except IndexError:
        return print('Нет параметра!')
    
def wrfile(*arg):# запись в файл
    try:
        txt_file = open(arg[0][0])
        txt_file.close()
        txt_file = open(arg[0][0],'w')
        txt_file.write(input(':'))
        txt_file.close()
        return 'ok'
    except IndexError:
        return print('Нет параметра!')
    except FileNotFoundError:
        return print('Файл не найден!')
 
def rdfile(*arg):# просмотр содержимого файла
    try:
        txt_file = open(arg[0][0])
        print(*txt_file)
        txt_file.close()
        return 'ok'
    except IndexError:
        return print('Нет параметра!')
    except FileNotFoundError:
        return print('Файл не найден!')
    
def delfile(*arg):# удаление файла
    try:
        os.remove(arg[0][0])
        return 'ok'
    except IndexError:
        return print('Нет параметра!')
    except FileNotFoundError:
        return print('Файл не найден!')
 
def copy(*arg):
    try:
        shutil.copy(arg[0][0], r00t+'/'+arg[0][1])
        return 'ok'
    except OSError:
        return print('Директории или файла не существует, либо они не доступны')
    except IndexError:
        return print('Нет параметра!')
    
def move(*arg):# перемещение файла
    try:
        shutil.move(arg[0][0], r00t+'/'+arg[0][1])
        return 'ok'
        
    except FileNotFoundError:
        return print('Скорее всего в текущей директории нет такого файла')
    except Exception:
        return print('Возможно в директории есть такой файл')
    except OSError:
        return print('Запрещено')
    except IndexError:
        return print('Нет параметра!')
    
def rnmfile(*arg):# переименование файла
    try:
        os.rename(arg[0][0], arg[0][1])
        return 'ok'
    except IndexError:
        return print('Нет параметра!')
    except FileNotFoundError:
        return print('Скорее всего в текущей директории нет такого файла')
    except PermissionError:
        return print('Отказано в доступе')

def exitt(arg):
    return 'kaboom'

def helpp(arg):
    return print('''cwd - Показывает текущую рабочую директорию
mkfol *имя* - создает директорию
delfol *имя* - удаляет директорию
chfol *имя* - перемещает в указанную директорию (".." для возврата)
mkfile *имя* - создает файл 
wrfile *имя* - запись в файл
rdfile *имя* - содержимое файла
delfile *имя* - удаляет файл
copy *имя файла* *имя директории/файла* - копирует файл в директорию или создает новый файл с тем же содержимим
move *имя файла* *имя директории* - перемещает файл в директорию
rnmfile *имя файла* *новое имя* - меняет название файла
exit - выход из программы
help - помощь''')
 
listener = {
    "cwd":cwd,
    "mkfol": mkfol,
    "delfol":delfol,
    "chfol":chfol,
    "mkfile":mkfile,
    "wrfile":wrfile,
    "rdfile":rdfile,
    "delfile":delfile,
    "copy":copy,
    "move":move,
    "rnmfile":rnmfile,
    "exit":exitt,
    "help":helpp
    }



def listen():
    USR_CMMND = input('>').split(' ')
    try:
        return listener[USR_CMMND[0]](USR_CMMND[1:])
    except KeyError:
        return print('Неизвестная команда')
