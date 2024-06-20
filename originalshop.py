buy = True  # for while loop
# Values of each product
water = 199
orange_juice = 215
iced_tea = 249
# Values of currency
dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

print("Vending Machine")
while buy:
    pay = 0  # input amount
    # Number of each currency for change calculations
    numDol = 0
    numQuarter = 0
    numDime = 0
    numNick = 0
    numPen = 0

    print("Please enter what product you want to buy[1-3] or select quit[4]")
    prompt = input("1. A bottle of water - $1.99\n" + "2. A bottle of orange juice - $2.15\n" + "3. A bottle of iced tea - $2.49\n" + "4. Quit\n")
    if prompt == "1":
        while pay < water:
            pay = int(input("Please deposit money (in cents):\n"))
        print("You bought a bottle of water.")
        change = pay - water
        # print(f"change total is {change}")


    elif prompt == "2":
        while pay < orange_juice:
            pay = int(input("Please deposit money (in cents):\n"))
        print("You bought a bottle of orange juice.")
        change = pay - orange_juice
        # print(f"change total is {change}")

    elif prompt == "3":
        while pay < iced_tea:
            pay = int(input("Please deposit money (in cents):\n"))
        print("You bought a bottle of iced tea.")
        change = pay - iced_tea
        # print(f"change total is {change}")


    elif prompt == "4":
        print("Goodbye!")
        break

    else:
        print("You made the wrong choice!")

    # calculating change:
    if change > 0:
        print("Your change is:")
        while change >= dollar:  # dollar
            numDol += 1
            change -= 100
        if numDol > 0:
            print(f"Dollars - {numDol}")

        while change >= quarter:  # quarter
            numQuarter += 1
            change -= 25
        if numQuarter > 0:
            print(f"Quarters - {numQuarter}")

        while change >= dime:  # dime
            numDime += 1
            change -= 10
        if numDime > 0:
            print(f"Dimes - {numDime}")

        while change >= nickel:  # nickel
            numNick += 1
            change -= 5
        if numNick > 0:
            print(f"Nickels - {numNick}")

        while change >= penny:  # penny/cent
            numPen += 1
            change -= 1
        if numPen > 0:
            print(f"Cents - {numPen}")