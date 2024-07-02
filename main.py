import json
from random import randint


def word() -> str:
    # Вытаскиваем словарь из файла
    with open('sort_words.json', 'r') as reed_file:
        data = json.load(reed_file)
        reed_file.close

    # Получаем 'рандомное' слово
    all_num = len(data)
    random_num = randint(1, all_num)
    random_word = data[str(random_num)]

    return random_word


def question(word_: str, w: dict) -> None:
    # Фиксируем начальные значения
    len_6 = '______'
    len_8 = '________'
    count = 0

    # Выводим начальную модельку виселицы
    print(w[count], '\n')

    # Основная логика игры для слов из 6 символов

    if len(word_) == 6:
        print(len_6)

        while True:
            x = input('Введите букву:')

            if x not in word_:
                count += 1
                print(w[count])
                print(len_6)
            else:
                z = [i for i in range(len(word_)) if word_[i] == x]
                for i in z:
                    len_6 = len_6[:i] + x + len_6[i+1:]
                print(w[count])
                print(len_6)
            if '_' not in len_6 or count == 6:
                print('\nИгра окончена')
                break

    # Основная логика игры для слов из 8 символов
    else:
        print(len_8)
        while True:
            x = input('Введите букву:')

            if x not in word_:
                count += 1
                print(w[count])
                print(len_8)

            else:
                z = [i for i in range(len(word_)) if word_[i] == x]
                for i in z:
                    len_8 = len_8[:i] + x + len_8[i+1:]
                print(w[count])
                print(len_8)
            if '_' not in len_8 or count == 8:
                print('\nИгра окончена')
                break


def main() -> None:
    print(
        '''Добро пожаловать в угадайку,
количество букв в слове равно
количеству символов '_'. ''')

    w = {
        0: '''
|-----|
|
|
|
|
''',
        1: '''
|-----|
|     o
|
|
|
''',
        2: '''
|-----|
|     o
|     |  
|
|
|
''',
        3: '''
|-----|
|     o
|    /|
|
|
|
''',
        4: '''
|-----|
|     o
|    /|\\  
|
|
|
''',
        5: '''
|-----|
|     o
|    /|\\  
|    / 
|
|
''',
        6: '''
|-----|
|     o
|    /|\\  
|    / \\
|
|
''',
        7: '''
|-----|
|     o
|    /|\\  
|   _/ \\
|
|
''',
        8: '''
|-----|
|     o
|    /|\\  
|   _/ \_
|
|
'''
    }

    word_ = word()
    question(word_, w)


if __name__ == '__main__':
    main()
