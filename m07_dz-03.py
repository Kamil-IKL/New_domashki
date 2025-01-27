import string


class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            # открываю файл в реживе "чтения" ('r')
            with open(file_name, 'r', encoding='utf-8') as file:
                # перевожу содержимое файла в нижний регистр
                content = file.read().lower()
                # удаляю пунктуацию из содержимого файла (см. файл (m07_dz-03_Знаки_препинания_del)
                content = content.translate(str.maketrans('', '', string.punctuation))
                # разбиваю строки по словам
                words = content.split()
                # добавляю в словарь по ключу file_name(название файла)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word_positions = {}

        # использую метод "get_all_words" для получения всех слов из файла
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # Нахожу позицию первого вхождения "принятого" слова в нижнем регистре(lower())
            position = words.index(word.lower()) + 1  # (+ 1), т.к. начинается индексирование с нуля (0)
            word_positions[file_name] = position
        return word_positions

    def count(self, word):
        word_counts = {}

        # использую метод "get_all_words" для получения всех слов из файла
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # считаю количество вхождения "принятого" слова в нижнем регистре(lower())
            count = words.count(word.lower())
            word_counts[file_name] = count
        return word_counts


# # проверка на рабоспособность с одним файлом
# finder2 = WordsFinder('m07_dz-03_test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# проверка на рабоспособность c несколькими файлами
finder1 = WordsFinder('m07_dz-03_Walt Whitman - O Captain! My Captain!.txt',
                      'm07_dz-03_Rudyard Kipling - If.txt', 'm07_dz-03_Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('the'))
print(finder1.count('the'))
