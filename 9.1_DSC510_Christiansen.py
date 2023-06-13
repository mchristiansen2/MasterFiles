# DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Madison Christiansen
# 10/26/2022
# Description: Modifying week 8 program to generate text file from output.


import string


def process_line(line, word_count_dict):
    """Process the line to get lowercase words to add to the dictionary. """
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        print("word before strip ", word)
        # ignore the '−−' that is in the file
        if word != '--':
            word = word.lower()
            word = word.strip()
            # get commas, periods, and other punctuation out as well
            word = word.strip(string.punctuation)
            print("word after strip, ", word)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):
    """Update the word frequency: word is the key, frequency is the value """
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def process_file(new_file, word_count_dict):
    """Output results to a new txt file"""
    with open(new_file, 'w') as fileHandle:
        fileHandle.write('Original Text: gettysburg.txt\n'
                         f'Length of the dictionary: {len(word_count_dict)} words\n'
                         f"{'Word':20}{'Count'}\n"
                         f"{'':-<26}\n")
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    for val, key in value_key_list:
        fileHandle.write('{:12s} {:<3d}.format(key, val)')


def main():
    word_count_dict = {}
    try:
        with open("gettysburg.txt", 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_count_dict)
        # data = fileHandle.read()
        print('Opening File:', {fileHandle.name})
        new_file = str(input("Enter new file name:")).rstrip()
        if new_file.endswith('.txt'):
            new_file = new_file
        else:
            new_file = new_file + '.txt'
        process_file(new_file, word_count_dict)
    except FileNotFoundError as e:
        print(e)
    process_file(new_file, word_count_dict)
    print('New file created', {new_file})


if __name__ == "__main__":
    main()

#   Change#:1
#   Change(s) Made: Added process_file in place of pretty_print
#   Date of Change: 10/28/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 10/30/2022
#   Change#:2
#   Change(s) Made: Added the new file extension to main
#   Date of Change: 10/28/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 10/30/2022
def main():
    word_count_dict = {}
    try:
        with open("gettysburg.txt", 'r') as fileHandle:
            for line in fileHandle:
                process_line(line, word_count_dict)
        # data = fileHandle.read()
        print('Opening File:', {fileHandle.name})
        new_file = str(input("Enter new file name:")).rstrip()
        if new_file.endswith('.txt'):
            new_file = new_file
        else:
            new_file = new_file + '.txt'
        process_file(new_file, word_count_dict)
    except FileNotFoundError as e:
        print(e)
    process_file(new_file, word_count_dict)
    print('New file created', {new_file})
