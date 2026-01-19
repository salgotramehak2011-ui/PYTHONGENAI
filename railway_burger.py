#---------------------RAILWAY----------------------------
print("WELCOME TO CODERAIL RAILWAY BOOKING SYSTEM")
name = input("Enter your name: " )
age = int(input("Enter your age: "))
print("chooose the travel class: ")
print("1.First class-1500")
print("2.Second class-1000")
print("3.Sleeper class-500")
travel_choice = input("Enter choice(1/2/3):")
if travel_choice == "1":
    ticket_price = 1500
    travel_class = "First class"
elif travel_choice == "2":
    ticket_price = 1000
    travel_class = "Second class"
elif travel_choice == "3":
    ticket_price = 500
    travel_class = "Third class"
else:
    print("Inavlid")

if age <= 5:
    ticket_price = 0
elif age >= 60:
    ticket_price = ticket_price * 0.8

add_meal = input("Do you want to add meal?(yes/no): ")
if add_meal == "yes":
    meal_charge = 200
    ticket_price += meal_charge
else:
    add_meal = "no"
    meal_charge = 0
#------------------------------------------------------------
print("---------Ticket Summary---------")
print("Passenger Name:",name)
print("Passenger Age:",age)
print("Class:",travel_class)
print("Meal Added:",add_meal)
print("Final Price:",ticket_price)
print("Enjoy your journey!")



#-------------------- ----BURGER KING----------------------------------

print("WELCOME TO BURGER KINGS!")
menu = input("Menu: \n1 Whooper Burger-$150 \n2 Crispy Veg-$100 \n3 Chicken Wings-$120\nEnter the items number(1/2/3):")
quantity = int(input("Enter Quantity"))
coupon = input("Do you have a coupon? (yes/no): ")
discount = 0
price = 0
items =""
if menu == "1":
    price = 150
    items = "Whooper Burger"
elif menu == "2":
    price = 100
    items = " Crispy Veg "
elif menu == "3":
    price = 120
    items = "Chicken Wings"


total_price = price*quantity
discount_price = total_price
if coupon =="yes":
    code = input("Enter your coupon code:")
    if code == "KING50":
        discount = "50%"
        discount_price = total_price/2
    elif code == "BK20":
        discount = "Rs. 20 OFF"
        discount_price = total_price-20
elif coupon == "no":
    discount = 0
    discount_price = total_price

final_price = discount_price
#------------------------------------------------------
print("----Bill Details----")
print("Applying coupon....")
print("original price:",total_price)
print("Discount Applied:",discount)
print("Final price",final_price)
print("Thanks for ordering at burger king!")


        
        












 


