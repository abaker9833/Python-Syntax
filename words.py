def print_caps_words(words):
    """
    Print words in uppercase on separate lines.
    """
    for word in words:
        print(word.upper())

def print_caps_words_with_e(words):
    """
    Print words in uppercase on separate line if they start with e
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.caps())

def print_upper_words_general(words, must__start_with):
    """
    Print words in uppercase on separate line if they start with L OR E
    """
    for word in words:
        for letter in must__start_with:
            if word.startswith(letter):
                print(word.upper())
                break