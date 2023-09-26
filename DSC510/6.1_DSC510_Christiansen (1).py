# DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Madison Christiansen
# 10/06/2022
# Description: List of temperatures.


def main():
    temperatures = []
    while temperatures != 'x':
        temp = input("Enter a temperature, enter X to quit:")
        while True:
            if temp == 'x':
                break
            try:
                float(temp)
                temp = float(temp)
                break
            except ValueError:
                temp = input("Enter a correct temperature:")
        if temp == 'x':
            break
        temperatures.append(temp)
    if not temperatures:
        print("Temperatures entered, not correct.")
    else:
        print("Temperatures entered:", temperatures)
        print("The highest temperature:", max(temperatures))
        print("The lowest temperature:", min(temperatures))


if __name__ == "__main__":
    main()


# Change#:1
# Change(s) Made: Added main
# Date of Change: 10/07/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/09/2022
# Change#:2
# Change(s) Made: added empty temp list
# Date of Change: 10/07/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/09/2022
# Change#:3
# Change(s) Made: added print messages
# Date of Change: 10/07/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 10/09/2022
# Change#:4
# # Change(s) Made: added append function, to allow for list creation
# # Date of Change: 10/07/2022
# # Author: Madison Christiansen
# # Change Approved by: Catie Williams
# # Date Moved to Production: 10/09/2022
