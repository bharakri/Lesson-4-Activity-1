money = int(input("Input the amount of money you would like to withdraw: "))
number100 = money//100
number50 = (number100 % 100)//50
number10 = (number50 % 50)//10

print(f"You will have {number100} hundred dollar bills, {number50} fifty dollar bills, and {number10} 10 dollar bills")