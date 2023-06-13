# DSC 510
# Week 5
# Programming Assignment Week 4
# Author: Madison Christiansen
# 09/26/2022
# Description: Creating loops and functions. Creating a simple calculator


def performcalculation(operation):  # to preform the arithmetic calculation
    print("Preform Calculation Function")
    while True:
        try:
            first_number = float(input("Please provide your first number: "))
            second_number = float(input("Please provide your second number: "))
            break
        except ValueError:
            print("You did not enter a valid number")
    if operation == '+':
        print("Answer:", (first_number + second_number))
    elif operation == '-':
        print("Answer:", (first_number - second_number))
    elif operation == '*':
        print("Answer:", (first_number * second_number))
    elif operation == '/':
        print("Answer:", (first_number / second_number))


def calculateaverage():  # to preform the average calculation
    integer_number = int(input("Enter the amount of numbers you have in the list:"))
    avg = 0
    print("Type a number then hit enter, continue for all numbers:")
    for x in range(integer_number):
        avg = int(input())
    avg = avg / integer_number
    print("Average:", avg)


def main():  # running the program for both calculations
    print("Thank you for using the calculator.")


choice = input('''Select which calculation you want preformed: "
               Arithmetic Calculation: (enter) ARI
               Average Calculation: (enter) AVG
               Enter input to continue:''')

if choice == 'ARI':
    operation = input('''
                      For additon enter: +'
                      For subtraction enter: -
                      For multiplication enter: *
                      For division enter: /
                      Enter input to continue:''')
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        performcalculation(operation)

if choice == "AVG":
    calculateaverage()

if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made: Added three different "def" functions
# Date of Change: 9/28/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/1/2022
# Change#:2
# Change(s) Made: Added to perform calculation function
# Date of Change: 9/28/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/1/2022
# Change#:3
# Change(s) Made: Added to preform average function
# Date of Change: 9/29/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/1/2022
# Change#:4
# Change(s) Made: created main
# Date of Change: 9/29/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/1/2022
# Change#:5
# Change(s) Made: entered choice options in main
# Date of Change: 9/29/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/1/2022
