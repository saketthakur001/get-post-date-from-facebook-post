import re

def remove_swearings(text):

    print(text, '--- the actual text')
    words = text.split(' ')
    new_sentense = ''
    shouldBeAdded = True
    for word in words:
        if word not in unKind_words:
            for start_unkind_word in start_unkind_words:
                # print(word, start_unkind_word)
                if re.search(f"^{re.escape(start_unkind_word)}", word):
                    # print(word, ' -- unkind word detected')
                    shouldBeAdded = False
        else: shouldBeAdded = False
        if shouldBeAdded:
            new_sentense += word + ' '
        shouldBeAdded = True
    return new_sentense[:-1]
