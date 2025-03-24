#Pizza ordering System 

name=input("-> Enter you name here : ")
size=""
flavour=""
total_bill=0
order_number=15989

if name!="":
    print("Crown Crust")
    print("Pepperoni")
    print("Cheese Burst")
    print("Barbecue")
    print("Double Melt")
    print("Super Loaded")
    print("Super Cheese")
    flavour=input("-> Which Flavour would you like to choose? ")
else:
    print("invalid input ")    

if flavour!="":
    print("small pizza")
    print("meddium pizza")
    print("large pizza ")
    size=input("-> Which size would you like to order? ")
else:
    print("invalid input ")

size=size.lower()
flavour=flavour.lower()
cheese=""
if size=="small" or size=="SMALL":
    print("-> small pizza price is : Rs:700")
    cheese=input("-> Do you want extra cheese (y/n) ")
    total_bill += 700

    if cheese=="y":
        print("-> extra cheese price is : Rs:150")
        total_bill+=150
    else:
        print("Thanks for choosing us")

elif size=="medium":
    print("-> medium pizza price is : Rs:1300")
    cheese=input("-> Do you want extra cheese (y/n) ")
    total_bill+=1300

    if cheese=="y":
        print("-> extra cheese price is : Rs:250")
        total_bill+=250
    else:
        print("Thanks for choosing us")

elif size=="large":
    print("->large pizza price is : Rs:2000")
    cheese=input("->Do you want extra cheese (y/n) ")
    total_bill+=2000

    if cheese=="y":
        print("-> extra cheese price is : Rs:350")
        total_bill+=350
    else:
        print("Thanks for choosing us")
else:
    print(" invalid input for pizza ")        

print(f"order placed by : {name}".lower())
print(f"your order number is : {order_number}")
print(f"your have ordered : {size} {flavour} pizza")
print(f"your total bill is  : {total_bill} only")
