def single_root_words(root_word, *other_words):
    same_words = []  # создаю пустой список для подходящих слов
    other_words_lower = []  # создаю пустой список для слов из списка "*other_words" в нижнием регистре

    # переводим элементы списка "*other_words" в нижний регистр
    for i in [*other_words]:
        i = i.lower()
        other_words_lower.append(i)  # добавляю в список other_words_lower
        # print(i)
    # print(other_words_lower)

    # проверяю содержит ли root_word (с учетом нижнего регистра) слово или наоборот
    for word in other_words_lower:
        # print(word)
        if root_word.lower() in word or word in root_word.lower():
            same_words.append(word)  # добавляю в список подходящих слов
    return same_words # возвращаю список подходящих слов


result1 = single_root_words('rich', 'RIchiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('кол', 'НиКоЛай', 'онколог', 'эконом', 'кальмар', 'КОЛОБОК')
print(result1)
print(result2)
print(result3)