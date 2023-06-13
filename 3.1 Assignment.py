# DSC 510
# Week 3
# Programming Assignment Week 3
# Author: Madison Christiansen
# 09/16/2022
# Description: implementing "if statements"
print("Welcome to Fiber Optic Calculator")
company_name = input("Please provide the company name:")  # retrieve company name
feet_needed = int(input("Enter the amount of feet needed:"))  # retrieve feet needed
if feet_needed <= 100:
    print("Installation cost per foot: $0.87.")
    print("Total Cost:", feet_needed * 0.87)  # calculates cost per feet
elif 100 < feet_needed <= 250:
    print("Installation cost per foot: $0.80")
    print("Total Cost:", feet_needed * 0.80)  # calculates cost per feet
elif 250 < feet_needed <= 500:
    print("Installation cost per foot: $0.70.")
    print("Total Cost:", feet_needed * 0.70)  # calculates cost per feet
else:
    print("Installation cost per foot: $0.50.")
    print("Total Cost:", feet_needed * 0.50)  # calculates cost per feet
print("Below is your receipt:")  # receipt
print("Company Name:", company_name)
print("Length of Cable in Feet:", feet_needed)
if feet_needed <= 100:
    print("Installation cost per foot: $0.87.")
    print("Total Cost:", feet_needed * 0.87)
elif 100 < feet_needed <= 250:
    print("Installation cost per foot: $0.80")
    print("Total Cost:", feet_needed * 0.80)
elif 250 < feet_needed <= 500:
    print("Installation cost per foot: $0.70.")
    print("Total Cost:", feet_needed * 0.70)
else:
    print("Installation cost per foot: $0.50.")
    print("Total Cost:", feet_needed * 0.50)
# Change Control Log:
# Change#:1
# Change(s) Made: Added "if statements" to calculate cost
# Date of Change: 6/16/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 9/18/2022
# Change Control Log:
# Change#:2
# Change(s) Made: Added "if statements" to calculate cost in receipt
# Date of Change: 6/16/2022
# Author: Madison Christiansen
# Change Approved by: Catie Williams
# Date Moved to Production: 9/18/2022
