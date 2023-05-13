def most_often_letter(string):
    max_numb = 0
    ans_letter = ''
    for letter in string:
        number = string.count(letter)
        if max_numb < number:
            max_numb = number
            ans_letter = letter
    return f'{ans_letter} - {max_numb}'



def one_list(list_in):
    ans_list = []
    for sublist in list_in:
        if isinstance(sublist, list):
            one_list(sublist)
        else:
            ans_list.append(sublist)
     return ans_list

print(most_often_letter("blaldaaaaaaaaaaaaflkshjkdfhsla"))
print(one_list([1, 2, 3, [4, 5], 6, [[[7]]], 8, 9, 10]))