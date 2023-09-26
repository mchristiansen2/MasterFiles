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
    fileHandle = open(new_file, 'w')
    #  with open(new_file, 'w') as fileHandle: - changed to be able to write in new file and not close
    fileHandle.write(f'Length of the dictionary:,{len(word_count_dict)} words\n'
                     f"{'Word,':5}{'Count'}\n"  # f"{'Word':20}{'Count'}\n" - too far
                     f"{'':-<26}\n")  # f"('{11}{11}'.format('Word', 'Count'))\n" -did not work
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))  # sorts on list's first element, the frequency.
        value_key_list.sort(reverse=True)  # Reverse to get the biggest first
    for key, val in value_key_list:
        fileHandle.write(f"{key:}, {val:15}\n")   # needed a "," to separate
        # '{:12s} {:<3d}'.format(key, val) - needed f string


def main():
    word_count_dict = {}
    fileHandle = open('gettysburg.txt', 'r')
    print("Name of file:", fileHandle.name)
    try:
        for line in fileHandle:
            process_line(line, word_count_dict)
        # data = fileHandle.read()
        print('Opening File:', {fileHandle.name})
        new_file = str(input("Enter new file name:")).rstrip()
    except FileNotFoundError as e:
        print(e)
    else:
        new_file = new_file + '.txt'
        process_file(new_file, word_count_dict)


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
