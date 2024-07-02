import json

# Функция для преобразования списка слов в словарь с порядковым ключом


def words_dict() -> None:

    # открываем файл со списком слов
    words_list = {}

    with open('words.txt', 'r', encoding='UTF-8') as f:
        s = f.read()
        f.close

        word_sort = []
        words = s.split('\n')

    # сортируем по длине 6 или 8 символов
    for w_s in words:

        if len(w_s) == 6 or len(w_s) == 8:
            word_sort.append(w_s)

    # упаковываем слова в словарь
    for num, word in enumerate(word_sort, start=1):

        words_list[num] = word
    with open('sort_words.json', 'w', encoding='UTF-8') as write_file:
        json.dump(words_list, write_file, ensure_ascii=False)


words_dict()
