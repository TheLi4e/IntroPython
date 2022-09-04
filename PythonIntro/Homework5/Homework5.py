
namesn = ["Свято", "Яро", "Влади", "Изя", "Вяче", "Мечи", "Бори", "Гори", "Бого", 
          "Любо","Мило","Свето","Миро","Добро","Брони"]
namesk = ["слав", "мир", "полк", "люб", "рад", "мил", "зар",
          "мысл", "дан", "гор", "яр", "вед", "бор", "мысл", "свет"]

#Task1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def Task1(string):
    return ' '.join((filter(lambda s:'абв' not in s, string.lower().split())))


#Task2. Создайте программу для игры с конфетами человек против человека/против бота.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#Все конфеты оппонента достаются сделавшему последний ход. 
import random
# Функция, описывающая логику приложения против игрока, возвращает победившего игрока.
def Task2 (candies, players, candiesForTake):
    print(f"На столе лежит {candies} конфет. Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {candiesForTake} конфет.\n Все конфеты оппонента достаются сделавшему последний ход.")
    turn = random.choice(players)
    print(f"Первый ходит {turn}")
    count = 0
    while candies > 0:
        print(f"{players[count%2]}, твой ход.")
        userChoice = int(input('Сколько конфет хотите взять? '))
        if candiesForTake >= userChoice and userChoice <= candies:
            candies = candies - userChoice
            print(f'Осталось {candies} конфет.')
            count +=1
        elif candiesForTake < userChoice or candiesForTake == 0 or candiesForTake > candies:
            print("Вы ввели некорректное число конфет. Попробуйте снова.")
    if candies == 0:
        return players[not count%2]


#Генерация имени бота.
def botName (namesn, namesk):
    n = random.choice(namesn)
    k = random.choice(namesk)
    botName = str(n+k)
    return botName
    

# Функция, описывающая логику приложения против бота, возвращает победившего игрока.
def Task2A (candies, players, candiesForTake):
    print(f"На столе лежит {candies} конфет. Играют два игрока делая ход друг после друга.\n Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {candiesForTake} конфет.\n Все конфеты оппонента достаются сделавшему последний ход.")
    turn = random.choice(players)
    print(f"Первый ходит {turn}")
    if turn == players[0]:
        count = 0
    else:
        count = 1
    while candies > 0:
        if count%2 == 0:
            print(f"{players[count%2]}, твой ход.")
            userChoice = int(input('Сколько конфет хотите взять? '))
            if candiesForTake >= userChoice and userChoice <= candies:
                candies = candies - userChoice
                print(f'Осталось {candies} конфет.')
                count +=1
            elif candiesForTake < userChoice or candiesForTake == 0 or candiesForTake > candies:
                print("Вы ввели некорректное число конфет. Попробуйте снова.")
        else:
            userChoice = random.randint(1,candiesForTake)
            if candiesForTake >= userChoice and userChoice <= candies:
                print(f"{players[1]} забрал {userChoice} конфет")
                candies = candies - userChoice
                print(f'Осталось {candies} конфет.')
                count +=1
            
    if candies == 0:
        return players[not count%2]


#Task3. Создайте программу для игры в ""Крестики-нолики"".
def DrawPlayground(board):
    print("_____________")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("_____________")


def check(board):
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

# Функция, описывающая логику приложения против бота, возвращает победившего игрока.
def Task3(board, players):
    turn = random.choice(players)
    if turn == players[0]:
        count = 0
    else:
        count = 1
    win = False
    while not win:
        DrawPlayground(board)
        if count % 2 == 0:
            playerChoice = "X"
            playerPlace = int(input(f"В какую ячейку хотите поставить {playerChoice}? "))
            if playerPlace>=1 and playerPlace<=9:
                if (str(board[playerPlace-1]) not in "XO"):
                    board[playerPlace-1] = playerChoice
                    count += 1
                else:
                    print("Эта клетка занята.")
            else:
                print('Неверный ввод. Укажите число от 1 до 9. ')

        else:
            playerChoice = "O"
            playerPlace = random.randint(1,9)
            if playerPlace>=1 and playerPlace<=9:
                if (str(board[playerPlace-1]) not in "XO"):
                    board[playerPlace-1] = playerChoice
                    print(f'{players[1]} поставил {playerChoice} в клетку {playerPlace}')
                    count += 1
        if count > 4:
            tmp = check(board)
            if tmp:
                win = True
                return players[not count%2]
        if count == 9:
            win = True
            print("Ничья!")
            return None
# Функция, описывающая логику приложения против игрока, возвращает победившего игрока.
def Task3A(board, players):
    
    turn = random.choice(players)
    print(f"Первый ходит {turn}")
    if turn == players[0]:
        count = 0
    else:
        count = 1
    win = False
    while not win:
        DrawPlayground(board)
        print(f"{players[count%2]}, твой ход.")
        if count % 2 == 0:
            playerChoice = "X"
            playerPlace = int(input(f"В какую ячейку хотите поставить {playerChoice}? "))
            if playerPlace>=1 and playerPlace<=9:
                if (str(board[playerPlace-1]) not in "XO"):
                    board[playerPlace-1] = playerChoice
                    count += 1
                else:
                    print("Эта клетка занята.")
            else:
                print('Неверный ввод. Укажите число от 1 до 9. ')
        else:
            playerChoice = "O"
            playerPlace = int(input(f"В какую ячейку хотите поставить {playerChoice}? "))
            if playerPlace>=1 and playerPlace<=9:
                if (str(board[playerPlace-1]) not in "XO"):
                    board[playerPlace-1] = playerChoice
                    count += 1
                else:
                    print("Эта клетка занята.")
            else:
                print('Неверный ввод. Укажите число от 1 до 9. ')
        if count > 4:
            tmp = check(board)
            if tmp:
                win = True
                return players[not count%2]
        if count == 9:
            win = True
            print("Ничья!")
            return None

#Task4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def Task4Encode(data):
    encode = ''
    prevChar = ''
    count = 1
    if not data: 
        return ''
    for char in data:
        if char != prevChar:
            if prevChar:
               encode += str(count) + prevChar 
            count = 1 
            prevChar = char 
        else:
            count += 1
    else:
        encode += str(count) + prevChar 
        return encode

def Task4Decode(data):
    decode = '' 
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count) 
            count = '' 
    return decode


#UI приложения
chooseTask = input('Введите номер задания от 1 до 4.\nquit - для завершения работы приложения. ').lower()
match chooseTask:
    case "1":
        print('Задание № 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')
        print('Абвгдейка - словарь для тех, кто стоит на абвахте в городе Абвиль.')
        print(Task1("Абвгдейка - словарь для тех, кто стоит на абвахте в городе Абвиль."))
    case "2":
        while True:
            try:    
                command = input('Добро пожаловать в игру "Сладость или гадость". Выберите режим игры:\n1)Игра против бота.\n2)Игра против второго игрока.\nquit - завершить работу приложения.\n').lower()
                match command:
                    case '1':
                        players = [input('Введите имя игрока № 1: '), botName(namesn, namesk)]
                        candies = int(input('Введите количество конфет для игры: '))
                        candiesForTake = int(input('Введите максимальное количество конфет для взятия за ход: '))
                        if candies >= candiesForTake:
                            print(f'Победил {Task2A(candies, players, candiesForTake)}, поздравляю!')
                        else:
                            print ("Нельзя вять больше конфет, чем их есть.")
                    case '2':
                        players = [input('Введите имя игрока № 1: '), input ('Введите имя игрока № 2: ')]
                        candies = int(input('Введите количество конфет для игры: '))
                        candiesForTake = int(input('Введите максимальное количество конфет для взятия за ход: '))
                        if candies >= candiesForTake:
                            print(f'Победил {Task2(candies, players, candiesForTake)}, поздравляю!')
                        else:
                            print ("Нельзя вять больше конфет, чем их есть.")
                    case "quit":
                        print('Завершение работы приложения.')
                        break
                    case _:
                        print("Вы ввели неправильную команду.")
            except:
                print("Введены неправильные данные. Перезапуск приложения...")
    case "3":
        while True:
            try:
                command = input('Добро пожаловать в игру "Крестики-нолики". Выберите режим игры:\n1)Игра против бота.\n2)Игра против второго игрока.\nquit - завершить работу приложения.\n').lower()
                match command:
                    case '1':
                        board = list(range(1,10))
                        players = [input('Введите имя игрока № 1: '), botName(namesn, namesk)]
                        print(f'Победил {Task3(board, players)}, поздравляю!')   
                    case '2':
                        board = list(range(1,10))
                        players = [input('Введите имя игрока № 1: '), input('Введите имя игрока № 2: ')]
                        print(f'Победил {Task3A(board, players)}, поздравляю!')
                    case "quit":
                        print('Завершение работы приложения.')
                        break
                    case _:
                        print("Вы ввели неправильную команду.")
            except:
                print("Введены неправильные данные. Перезапуск приложения...")
    case "4":
        print('Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.')
        print('FFFFFFAAAAAAAAAFSSSSSSSSEEEEEEEESSSSSSFG')
        print(Task4Encode("FFFFFFAAAAAAAAAFSSSSSSSSEEEEEEEESSSSSSFG"))
        print(Task4Decode(Task4Encode("FFFFFFAAAAAAAAAFSSSSSSSSEEEEEEEESSSSSSFG")))
    case "quit":
        print("Завершение работы приложения...")
        exit()
    case _:
        print('Введен некоректный номер задания. Введите число от 1 до 4. ')