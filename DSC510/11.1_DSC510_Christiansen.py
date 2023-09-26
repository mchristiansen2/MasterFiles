# DSC 510
# Week 11
# Programming Assignment Week 11
# Author: Madison Christiansen
# 11/13/2022
# Description: Cash Register

import locale


class CashRegister:
    def __init__(self):
        self.items = 0
        self.total = 0

    def addItem(self, price):  # gets parameter for price and keeps track of items
        self.items += 1
        self.total = self.total + sum(price)

    def getCount(self):  # returns item count
        return self.items

    def getTotal(self):  # returns total price
        locale.setlocale(category=locale.LC_ALL, locale='en_US')
        return locale.currency(self.total, symbol=True)

    def clearCart(self):
        self.total = 0.0
        self.items = 0
        print("Your cart has been deleted.")


def main():
    register = CashRegister()
    print("Welcome to the Cash Register.")
    price = []
    while price != 'total':
        price = input("Enter the amount you would like added, or enter 'total' to calculate the cart:")
        while True:
            if price == 'total':
                break
            try:
                price = [float(x) for x in price]
                break
            except ValueError:
                price = input("You did not enter a correct amount. Enter price or 'total':")
        if price == 'total':
            print('Items in your cart:', register.getCount(), 'Totalling:', register.getTotal())
        register.addItem(price)
    if price == 'total':
        another = input("Would you like to start a new cart, enter yes or no:")
        while True:
            if another == 'yes':
                register.clearCart()
                break
            if another == 'no':
                print("Thank you for using the Cash Register.")
                break
        register.addItem(price)


if __name__ == "__main__":
    main()

#   Change#:1
#   Change(s) Made: added class, main, and 4 def functions
#   Date of Change: 11/10/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/13/2022
#   Change#:2
#   Change(s) Made: added __int__ and parameters
#   Date of Change: 11/10/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/13/2022
#   Change#:3
#   Change(s) Made: updated main
#   Date of Change: 11/10/2022
#   Author: Madison Christiansen
#   Change Approved by: Catie Williams
#   Date Moved to Production: 11/13/2022
