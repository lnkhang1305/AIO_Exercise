

def count_word_in_file(data):
    text_list = data.lower().split()
    result_dict = dict()
    for word in text_list:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict


if __name__ == "__main__":
    with open('P1_data.txt', 'r') as f:
        data = f.read()
        print(type(data))
        dict_word_count = dict()
        dict_word_count = count_word_in_file(data=data)
        print(dict_word_count)
