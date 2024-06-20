startScreen = """Please enter what product you want to buy[1-3] or select quit[4]:
1. A bottle of water - $1.99
2. A bottle of orange juice - $2.15
3. A bottle of iced tea - $2.49
4. Quit
"""
print('Vending Machine')
choice = " "

while True:
    total_money_deposited = 0
    cost = 0 
    
    choice = input(f"{startScreen}")
    
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        print("You made the wrong choice!")
        choice = input(f"{startScreen}")
        
    if choice == '1':
        choice = "bottle of water"
        cost += 199
    elif choice == '2':
        choice = "bottle of orange juice"
        cost += 215
    elif choice == '3':
        choice = "bottle of iced tea"
        cost += 249
    elif choice == '4':
        print("Goodbye!")
        break
    
    while total_money_deposited < cost:
        money_deposited = int(input('Please deposit money (in cents):\n'))
        total_money_deposited += money_deposited


    change = total_money_deposited - cost
    dollars = change // 100   # get the quotient Quotient
    change = change % 100     # get the remainder Remainder
    quarters = change // 25 
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    cents = change

    print(f"You bought a {choice}.")
    if dollars != 0 or quarters != 0 or dimes != 0 or nickels != 0 or cents != 0:
        print("Your change is:")
        if dollars != 0:
            print(f"Dollars - {dollars}")
            
        if quarters != 0:
            print(f"Quarters - {quarters}")
            
        if dimes != 0:
            print(f"Dimes - {dimes}")
        
        if nickels != 0:
            print(f"Nickels - {nickels}")
            
        if cents != 0:
            print(f"Cents - {cents}")
