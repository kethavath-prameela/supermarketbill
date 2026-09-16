name = input("Enter your name:")

#list of items
lists = '''
Rice  Rs 10/kg
sugar Rs 8/kg
oil   Rs 30/liter
'''

#Declaration
Price =0
Pricelist =[]
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []
items = []

#Rate for each item
items = {'rice': 10, "sugar": 8, "oil": 30}

while True:
    option = input("Press 1 for list or 2 to Exit:")
    if option == "2":
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To buy press 1 or 2 to exti:")
            if inp1 == '2':
                print("Than you for shopping")
                break
            elif inp1 == '1':
                item = input("choose your items:").lower()
                while True:
                    quantity_input = input("Enter quantity:")
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity")
                        if item in items:
                            price = quantity*items[item]
                            Pricelist.append((items, quantity, items[item], price))
                            totalprice +=price
                            ilist.append(item)
                            qlist.append(item)
                            qlist.append(quantity)
                            plist.append(price)
                        else:
                            print("Selected item is not available sorry for the inconvenience")
                            if totalprice > 0:
                                tax = (totalprice * 18) / 100
                                finalamount = tax + totalprice
                                print(25 * "=", "pythonlife Supermarket", 25 * "=")
                                print(28 * " ", "Hyderabad") 
                                print("Name :",name, 30 * " ","August 04 2026")


                                           
