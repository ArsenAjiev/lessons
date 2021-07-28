dictionary = {
    "apple": "яблоко",
    "house": "дом"
}

dict_rus_to_eng = {
    value: key
    for key, value in dictionary.items()
}


def from_eng_to_rus(eng):
    rus =dictionary[eng]
    return rus

print(from_eng_to_rus("apple"))

print(dict_rus_to_eng)

def from_rus_to_eng(rus):
    eng = dictionary[rus]
    return eng

print(from_rus_to_eng("яблоко"))

