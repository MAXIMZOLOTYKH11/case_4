import os

def acceptCommand(c):
    str_nam = [1, 2, 3, 4, 5, 6, 7]
    if c in str_nam:
        return c
    else:
        print('Ошибка запроса.')


def runCommand(command):
    if command == 1:
        list_cd = os.listdir(os.getcwd())
        for i in list_cd:
            print(i)
    elif command == 2:
        moveUp(os.getcwd())
    elif command == 3:
        moveDown(os.getcwd())
    elif command == 4:
        cd = os.getcwd()
        print('Количесвто файлов в текущем каталоге: ', countFiles1(cd))
    elif command == 5:
        print('Размер текущей директории: ', main_size())
    elif command == 6:
        main_search()


def moveUp(cd):
    cd1 = cd[::-1]
    cdf = cd1.find('\\')
    cd2 = cd1[cdf + 1:]
    cd3 = cd2[::-1]
    os.chdir(cd3)


def moveDown(cd):
    ud = input('Введите название подкаталога: ')
    nd = cd + '\\' + ud
    try:
        os.chdir(nd)
    except:
        print('Ошибка: некорректно указано название подкаталога')


def countFiles1(cd):
    amount = [0]


    def countFiles2(cd,amount):
        i_f = os.path.isfile(cd)
        if i_f == True:
            amount[0] += 0
        else:
            ld = os.listdir(cd)
            amount[0] += len(os.listdir(cd))
            for i in ld:
                e = cd + '\\' + i
                a = countFiles2(e, amount)
    countFiles2(cd, amount)
    return amount[0]


def main_size():


    def size(cd, s):
        i_f = os.path.isfile(cd)
        if i_f == True:
            s['s'] += os.path.getsize(cd)
        else:
            lst = []
            ld = os.listdir(cd)
            for i in ld:
                e = cd + '\\' + i
                a = size(e, s)
                lst.append(a)
            return lst

    cd = os.getcwd()
    s = {'s': 0}
    size(cd, s)
    return s['s']


def main_search():


    def search(cd, c, tg):
        i_f = os.path.isfile(cd)
        if i_f == True:
            cd1 = cd[::-1]
            cd1f1 = cd1.find('/')
            cd1f2 = cd1.find('\\')
            cd1f = min(cd1f1, cd1f2)
            cd2 = cd1[0:cd1f]
            cd2f = cd2.find('.')
            if cd2f != -1:
                cd2 = cd2[cd2f + 1]
            cd3 = cd2[::-1]
            tgf = cd3.find(tg)
            if tgf != -1:
                c['c'].append(cd)
        else:
            lst = []
            ld = os.listdir(cd)
            for i in ld:
                e = cd + '/' + i
                a = search(e, c, tg)
                lst.append(a)
            return lst
    tg = input('Введите ключевое слово для поиска: ')
    cd = os.getcwd()
    c = {'c': []}
    search(cd, c, tg)
    ls = c['c']
    if len(ls) == 0:
        print('Совпадений не найдено')
    else:
        print('Найдены следующие совпадения:')
        for i in ls:
            print(i)


def main():
    MENU = '1. Просмотр каталога\n' \
           '2. На уровень вверх\n' \
           '3. На уровень вниз\n' \
           '4. Количество файлов и каталогов\n' \
           '5. Размер текущего каталога (в байтах)\n' \
           '6. Поиск файла\n' \
           '7. Выход из программы\n' \
           'Выберите пункт меню: '
    QUIT = 7
    while True:
        print(MENU)
        nam_name = int(input())
        command = acceptCommand(nam_name)
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()