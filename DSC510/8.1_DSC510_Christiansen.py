# DSC 510
# Week 8
# Programming Assignment Week 8
# Author: Madison Christiansen
# 10/19/2022
# Description: Dictionaries, tuples, and JSON data.


def process_line(line, word_count_dict):
    import string
    line = line.rstrip().lower().translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    add_word(words, word_count_dict)


def add_word(words, word_count_dict):
    for word in words:
        if word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1


def pretty_print(word_count_dict):
    print('Length of Dictionary:', len(word_count_dict))
    print('{:11}{:11}'.format("Word", "Count"))
    for key, value in sorted(word_count_dict.items()):
        print('{:20}{}'.format(key, value))


def main():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    print("Name of file:", gba_file.name)
    try:
        for line in gba_file:
            process_line(line, word_count_dict)
    except FileNotFoundError as e:
        print(e)
    else:
        pretty_print(word_count_dict)

    gba_file.close()


if __name__ == "__main__":
    main()


# Change#:1
# Change(s) Made: added main, and three functions
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:2
# Change(s) Made: downloaded and added open file
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:3
# Change(s) Made: changed main to try,else,except
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:4
# Change(s) Made: dictionary rewrite, adding a word
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:5
# Change(s) Made: updated add word, to for in to fix parameter of "word"
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:6
# Change(s) Made: fixed main ending
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:7
# Change(s) Made: added close() file
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
# Change#:8
# Change(s) Made: added ".translate" to take out punctuation
# Date of Change: 10/22/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2022
