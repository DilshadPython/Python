# if return vowl character then is True
def is_letter_vowel(let=str(input('Enter a letter: '))):
    if let == 'a' or let == 'e' or \
       let == 'i' or let == 'o' or \
       let == 'u' or let == 'q':
        return True
    else:
        return False


print(is_letter_vowel())
