def most_often_letter(string):
    max_numb = 0
    ans_letter = ''
    for letter in string:
        number = string.count(letter)
        if max_numb < number:
            max_numb = number
            ans_letter = letter
    return f'{ans_letter} - {max_numb}'

print(most_often_letter("blaldaaaaaaaaaaaaflkshjkdfhsla"))