list_of_available_pizza = [
    "peperoni",
    "magerita",
    "bolognaise",
    "fromage",
    "champignon",
]
order_list = []
order = 0
unit_price = 10

print("Hello! Here are the available pizza:")
for i, pizza in enumerate(list_of_available_pizza):
    i += 1
    print(str(i) + ". " + pizza)
choice = "yes"
while choice == "yes":
    pizza_number = int(input("what do you want to order? (select a number)"))
    if pizza_number <= len(list_of_available_pizza) and pizza_number > 0:
        order_list.append(list_of_available_pizza[pizza_number - 1])
        order = order + 1
        print(
            "Adding "
            + str(list_of_available_pizza[pizza_number - 1])
            + " to your order"
        )
    else:
        print("sorry pizza " + str(pizza_number) + " does not exist")

    message = "Do you want to add a pizza to your order? "
    choice = input(message)
    while choice != "yes" and choice != "no":
        print("invalid response ")
        choice = input(message)


print("you have ordered " + str(order) + " pizza")
print("your order: " + str(order_list))
total_price = unit_price * len(order_list)
print("price " + str(total_price))
if total_price >= 10:
    is_tip_value_valid = False
    while not is_tip_value_valid:
        tip = int(input("Do you want to add some tip? (0-25%)"))
        tip_amount = (tip / 100) * total_price
        amount_to_pay = tip_amount + total_price
        if tip <= 25 and tip > 0:
            print("Thanks, you have to pay " + str(amount_to_pay))
            print("The pizza are on the way...")
            is_tip_value_valid = True

        else:
            print("invalid tip")

else:
    print("see you next time")
