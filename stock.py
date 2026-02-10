import time
import os
import random

stocks_code = ["VCB", "BID", "VIC", "VHM", "VNM", "HPG", "FOX", "TCB", "MBB", "VRE", "MSN", "FPT", "ICT", "SGT", "JPN"]
portfolio = []
Total = 0

turn = 0
market_type = ""
price_to_buy = 0

banking_stock = 75
vin_stock = 58
retail_stock = 45
tech_stock = 51

who_to_change = ["bank", "vin", "retail", "tech"]
up_or_down = 0
change_factor = 0
change_in_price = 0

while True:
    for i in range(0, 5):
        up_or_down = random.randint(-2, 1)
        if up_or_down < 0:
            up_or_down = -1
        else:
            up_or_down = 1
        change_factor = random.randint(10, 20)
        change_in_price  = up_or_down*change_factor
        random_field = random.choice(who_to_change)
        if random_field == "bank":
            banking_stock = banking_stock + change_in_price
        elif random_field == "vin":
            vin_stock = vin_stock + change_in_price
        elif random_field == "retail":
            retail_stock = retail_stock + change_in_price
        elif random_field == "tech":
            tech_stock = tech_stock + change_in_price

    print("Available stock codes: \n"
          "-----BANKING-----\n"
          "1.VCB       2.BID\n"
          "3.TCB       4.MBB")
    print("-----VIN GROUP-----\n"
          "1.VIC       2.VHM\n"
          "3.VRE")
    print("-----RETAIL & INDUSTRIAL-----\n"
          "1.VNM       2.MSN\n"
          "3.HPG       4.JPN")
    print("-----TECHNOLOGY-----\n"
          "1.FOX       2.FPT\n"
          "3.ICT       4.SGT")
    print("Capslock not needed")
    user_input = input("Enter a stock code you want to buy (q to quit): ")
    user_input = user_input.upper()
    if user_input == "Q":
        print("Should have bought more.")
        break
    if user_input not in stocks_code:
        for wait_time in reversed(range(1, 4)):
            print("Invalid stock code!")
            print(f"Wait to be redirected 00:0{wait_time}")
            time.sleep(1)
            os.system('cls')
    else:
        if user_input == "VCB" or user_input == "BID" or user_input == "TCB" or user_input == "MBB":
            market_type = "BANKING"
        elif user_input == "VIC" or user_input == "VHM" or user_input == "VRE":
            market_type = "VIN"
        elif user_input == "VNM" or user_input == "MSN" or user_input == "HPG" or user_input == "JPN":
            market_type = "RETAIL"
        elif user_input == "FOX" or user_input == "FPT" or user_input == "ICT" or user_input == "SGT":
            market_type = "TECH"

        if market_type == "BANKING":
            price_to_buy = banking_stock
        elif market_type == "VIN":
            price_to_buy = vin_stock
        elif market_type == "RETAIL":
            price_to_buy = retail_stock
        elif market_type == "TECH":
            price_to_buy = tech_stock

        print(f"We set stock prices by group. The average stock prices of each groups are: \n"
              f"BANKING: ${banking_stock}\n"
              f"VIN GROUP: ${vin_stock}\n"
              f"RETAIL AND INDUSTRIAL: ${retail_stock}\n"
              f"TECHNOLOGY: ${tech_stock}")
        amount = int(input(f"Enter the {user_input} amount: "))
        for wait_time_2 in reversed(range(1, 7)):
            print(f"The price to buy {amount} stocks of {user_input}: ${amount*price_to_buy}")
            print(f"Wait for directing: 00:0{wait_time_2}")
            time.sleep(1)
        turn = turn+1
        portfolio.append(f"{turn}. {user_input}: {amount} stocks. Price at bought: ${price_to_buy}")
        print("-----YOUR PORTFOLIO-----")
        for stock in portfolio:
            print(stock)
        print(f"-----CURRENT PRICE----- \n"
                  f"BANKING: ${banking_stock}\n"
                  f"VIN GROUP: ${vin_stock}\n"
                  f"RETAIL AND INDUSTRIAL: ${retail_stock}\n"
                  f"TECHNOLOGY: ${tech_stock}")
        time.sleep(6)

