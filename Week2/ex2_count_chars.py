

def count_chars(word):
    result_dict = dict()
    for letter in word:
        if letter in result_dict:
            result_dict[letter] += 1
        else:
            result_dict[letter] = 1
    return result_dict


if __name__ == "__main__":
    word = "Happiness"
    dict_count_chars = dict()
    dict_count_chars = count_chars(word=word)
    dict_count_chars = dict(
        sorted(dict_count_chars.items(), key=lambda x: x[0]))
    print(dict_count_chars)
