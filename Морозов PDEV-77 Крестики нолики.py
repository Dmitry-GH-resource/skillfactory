import random
import time


# Функция отрисовки игрового поля
def drawing_playing_field(playing_field_data: list) -> list:
    if playing_field_data == [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]:
        print(f'Правила игры:'
              f'\n  1. Два игрока совершают ходы по очереди'
              f'\n  2. Первый игрок(пользователь) играет за "1" и совершает первый ход'
              f'\n  3. Второй игрок(компьютер) играет за "0"'
              f'\n  4. Выигрывает игрок первым собравший ряд из 3х своих символов'
              f'\n  5. Если использовав все ячейки поля не выявлен победитель, игра считается законченой вничью'
              f'\n')
    print(
        f"№ _1_2_3\n1| {" ".join(playing_field_data[0])}\n2| {" ".join(playing_field_data[1])}\n3| {" ".join(playing_field_data[2])}")


# Функция получения координаты x или y для первого игрока
def xy_Player1(axis: str) -> int:
    while True:
        if axis == 'x':
            xy = input('Введите ось X: ')
        if axis == 'y':
            xy = input('Введите ось Y: ')

        try:
            xy = int(xy)
            if 1 <= xy <= 3:
                break
            else:
                print('\n--Ошибка!\n--Размер поля 3X3\n')
        except:
            print('\n--Ошибка!\n--Для ввода доступны только цифры\n')

    return xy - 1


# Функция получения координаты x или y для второго игрока
def xy_Player2() -> int:
    xy = random.randint(0, 2)
    return xy


# Функция определяет порядок ходов, заполненна ли клетка по координатам полученным с помощью функции xy_Player1 или xy_Player2 (если нет то заполняет)
def checking_cage(field_data: list, i: int) -> list:
    if i % 2 == 0:
        print('\nВаш ход')
    else:
        print('\nХод противника: Ожидайте...')
        time.sleep(random.randint(1, 3))

    while True:
        if i % 2 == 0:
            x = xy_Player1('x')
            y = xy_Player1('y')
        else:
            x = xy_Player2()
            y = xy_Player2()

        if field_data[x][y] == 'x' and i % 2 == 0:
            field_data[x][y] = '1'
            break
        elif field_data[x][y] == 'x' and i % 2 != 0:
            field_data[x][y] = '0'
            break

        if i % 2 == False:
            print('\n--Ошибка\n--Эта клетка занята\n')

    return field_data


# Функция определяет победителя
def Verification_of_victory(field_data: list) -> bool:
    winning_combination = ''

    for i in range(len(field_data)):
        for j in range(len(field_data)):
            winning_combination += field_data[i][j]
            if 'x' not in winning_combination and len(winning_combination) == 9:
                print('\n--Игра закончена вничью!')
                return True

    for winning_combination in field_data:
        if winning_combination == ['1', '1', '1']:
            print('\n--Игра завершилась победой пользователя!')
            return True
        elif winning_combination == ['1', '1', '1']:
            print('\n--Игра завершилась победой компьютера!')
            return True

    for i in range(3):
        winning_combination = field_data[0][i] + field_data[1][i] + field_data[2][i]
        if winning_combination == '111':
            print('\n--Игра завершилась победой пользователя!')
            return True
        elif winning_combination == '000':
            print('\n--Игра завершилась победой компьютера!')
            return True

    winning_combination = field_data[0][0] + field_data[1][1] + field_data[2][2]
    if winning_combination == '111':
        print('\n--Игра завершилась победой пользователя!')
        return True
    elif winning_combination == '000':
        print('\n--Игра завершилась победой компьютера!')
        return True

    winning_combination = field_data[2][0] + field_data[1][1] + field_data[0][2]
    if winning_combination == '111':
        print('\n--Игра завершилась победой пользователя!')
        return True
    elif winning_combination == '000':
        print('\n--Игра завершилась победой компьютера!')
        return True

    return False


# Основной код программы
playing_field_data = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
for turn in range(10):
    drawing_playing_field(playing_field_data)

    if Verification_of_victory(playing_field_data) == True:
        break

    playing_field_data = checking_cage(playing_field_data, turn)