list_of_available_pizza = ["peperoni", "magerita", "bolognaise", "fromage", "champignon"]
order_list = []
order = 0
unit_price = 10

print("Hello! Here are the available pizza:")
for i, pizza in enumerate(list_of_available_pizza):
    i += 1
    print(str(i) + ". " + pizza)
choice = input("Do you want to add a pizza to your order? ")
while choice == "yes":
    pizza_number = int(input("what do you want to order? (select a number)"))
    if pizza_number <= len(list_of_available_pizza) and pizza_number > 0:
        order_list.append(list_of_available_pizza[pizza_number - 1])
        order = order + 1
        print("Adding " + str(list_of_available_pizza[pizza_number]) + " to your order")
    else:
        print("sorry pizza " + str(pizza_number) + " does not exist")
    choice = input("Do you want to add a pizza to your order? ")
          
print("you have ordered " + str(order) + " pizza") 
print("your order: " + str(order_list))
Total_price = unit_price * len(order_list) 
print("price " + str(Total_price)) 
Tip = int(input("Do you want to add some tip? (0-25%)"))
Tip_amount = (Tip/100)*Total_price
Amount_to_pay = Tip_amount + Total_price
print("Thanks, you have to pay " + str(Amount_to_pay))
print("The pizza are on the way...")