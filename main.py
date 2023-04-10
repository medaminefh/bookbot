def count_words(s):
    return len(s.split())

def count_letters(s):
    letters = {}
    for i in s:
        if not i.isalpha():
            continue
        elif i in letters:
            letters[i]+=1
        else:
            letters[i] = 0

    myKeys = list(letters.keys())
    myKeys.sort()
    sorted_dict = {i: letters[i] for i in myKeys}
    return sorted_dict

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words_count = count_words(file_contents)
    letters = count_letters(file_contents.lower())
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{words_count} words found in the document')
    for i in letters:
        print(f'The {i} character was found {letters[i]} times')

    print('--- End report ---')
