def get_num_words(string):
    word_list = string.split()
    w_count = len(word_list)
    return w_count

def get_char_number(string):
    dict_letters = {}
    for letter in string.lower():

        if letter in dict_letters.keys():
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    
    return dict_letters
def sort_on (dict):
    return dict["num"]

def sort_characters(dict):
    dict_temp = {}
    dict_num = {}
    lst_dict = []

    for letter in dict.keys():
        if letter.isalpha() == True:
            dict_temp["char"] = letter
            dict_temp["num"] = dict[letter]
            dict_num["num"] = dict[letter]
            lst_dict.append(dict_temp)
            dict_temp = {}
    lst_dict.sort(reverse=True, key=sort_on)

    for item in lst_dict:
        count = 0
        letter = ""
        num = 0
        for dictionary in item.keys():
            if count == 0:
                letter = item[dictionary]
                count += 1
            else:
                num = item[dictionary]
        print(f"{letter}: {num}")




