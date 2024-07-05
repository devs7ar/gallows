import json
from random import choice


def get_word() -> str:

    with open('words.txt', 'r', encoding='UTF-8') as all_words:

        words = all_words.read()
        words_list = words.split('\n')
        random_word = choice(words_list)

        return random_word


def question(line: str, random_word: str, gallows: dict, count: int) -> None:
    print(gallows[count], '\n')

    print(line)

    while True:
        letter = input('Введите букву:')

        if letter not in random_word:
            count += 1
            print(gallows[count])
            print(line)
        else:
            z = [i for i in range(len(random_word))
                 if random_word[i] == letter]
            for i in z:
                line = line[:i] + letter + line[i+1:]
            print(gallows[count])
            print(line)
        if count == len(random_word) and '_' in line:
            print(
                f'''Повезет в следующий раз, \nправильное слово \'{random_word}\'''')
            break


def main() -> None:

    print(
        '''Добро пожаловать в угадайку,
количество букв в слове равно
количеству символов '_'. ''')

    gallows = {
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

    random_word = get_word()
    line = '_' * len(random_word)

    question(line, random_word, gallows, count=0)


if __name__ == '__main__':
    main()
