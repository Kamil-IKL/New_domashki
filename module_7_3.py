import string


class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            # �������� ���� � ������ "������" ('r')
            with open(file_name, 'r', encoding='utf-8') as file:
                # �������� ���������� ����� � ������ �������
                content = file.read().lower()
                # ������ ���������� �� ����������� ����� (��. ���� (m07_dz-03_�����_����������_del)
                content = content.translate(str.maketrans('', '', string.punctuation))
                # �������� ������ �� ������
                words = content.split()
                # �������� � ������� �� ����� file_name(�������� �����)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word_positions = {}

        # ��������� ����� "get_all_words" ��� ��������� ���� ���� �� �����
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # ������ ������� ������� ��������� "���������" ����� � ������ ��������(lower())
            position = words.index(word.lower()) + 1  # (+ 1), �.�. ���������� �������������� � ���� (0)
            word_positions[file_name] = position
        return word_positions

    def count(self, word):
        word_counts = {}

        # ��������� ����� "get_all_words" ��� ��������� ���� ���� �� �����
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            # ������ ���������� ��������� "���������" ����� � ������ ��������(lower())
            count = words.count(word.lower())
            word_counts[file_name] = count
        return word_counts


# # �������� �� ��������������� c ����� ������
# finder2 = WordsFinder('m07_dz-03_test_file.txt')
# print(finder2.get_all_words())  # ��� �����
# print(finder2.find('TEXT'))  # 3 ����� �� �����
# print(finder2.count('teXT'))  # 4 ����� teXT � ������ �����

# �������� �� ��������������� c ����������� �������
finder1 = WordsFinder('m07_dz-03_Walt Whitman - O Captain! My Captain!.txt',
                      'm07_dz-03_Rudyard Kipling - If.txt', 'm07_dz-03_Mother Goose - Monday�s Child.txt')
print(finder1.get_all_words())  # ��� �����
print(finder1.find('the'))
print(finder1.count('the'))