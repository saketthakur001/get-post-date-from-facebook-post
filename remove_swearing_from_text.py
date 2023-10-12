import re
unKind_words = ['madarchod',
'bhenchod',
'maakichut',
'bhosdike',
'maaklaude',
'bsdk',
'rndiik',
'randi',
'lund',
'chutiya',
'bhdwee',
'gndu',
'gandu',
'bhadwee',
'bhadwee',
'chutt',
'choochi',
'bhosdaa',
'bhosdike',
'bhsdike',
'chudaap',
'lawde',
'lnd',
'betichod',
'btichd',
'betichod',
'chod',
'gndwee',
'gandwee',
'gndmree',
'gandmree',
'kutte',
'kaminey',
'kminey',
'mc',
'bc',
'mcc'
]

start_unkind_words = ['mada',
 'beti',
 'bti',
 'chod',
 'chut',
 'lun',
 'lawd',
 'lode',
 'gnd',
 'gand',
 'mc',
 'bc',
 'chut',
 'randi',
 'lndu',
 'bhsd',
 'bhons',
 'bhad',
 "bhen",
 "bhnk"
 ]

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

# print('Main Paytm se loan liyaa tha bhnklundoo ne pass hi nhii kiaa')
#test 1
print(remove_swearings('Main Paytm se loan liyaa tha bhnklundoo ne pass hi nhii kiaa'), '\n')
#test 2
print(remove_swearings('Gali Gali m chor h Paytm madarchod h'), '\n')
#test 3
print(remove_swearings('Bhdwye h paytm valt gndu k bachhe'), '\n')
#test 4
print(remove_swearings('Sentence daal ye bhnklnd Paytm vali ki maakichut'), '\n')