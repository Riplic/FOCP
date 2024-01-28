sentence = "this is a sentence containing some letters"
known_letters = {' ', 't', 'h', 's', 'e', 'i', 'o', 'c', 'a', 'n', 'r', 'l', 'g', 'm'}
unique_letters = {x for x in sentence if x not in known_letters}
print(unique_letters)
