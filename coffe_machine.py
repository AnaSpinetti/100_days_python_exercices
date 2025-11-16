coins = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.10,
    "Quarter": 0.25 
}

resources = {
        "water": 800, 
        "milk": 500,
        "coffee": 300,
        "money": 7.00
}

menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.50
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.50
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.00
    }
}

exit = False


def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}")

def print_options():
    print("Available items:")
    for item in menu:
        cost = menu[item]["cost"]
        print(f"- {item.capitalize()}: ${cost:.2f}")

def order_item(item):
    # Validando se tenho os items necessarios
    if(resources["water"] < menu[item]["water"]):
        print("Sorry there is not enough water.")
        return
    if(resources["coffee"] < menu[item]["coffee"]):
        print("Sorry there is not enough coffee.")
        return
    if("milk" in menu[item] and resources["milk"] < menu[item]["milk"]):
        print("Sorry there is not enough milk.")
        return

    # Inserindo moedas
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))* coins["Quarter"]
    dimes = int(input("How many dimes?: ")) * coins["Dime"]
    nickels = int(input("How many nickels?: ")) * coins["Nickel"]
    pennies = int(input("How many pennies?: ")) * coins["Penny"]

    # Calculando o total inserido e o troco
    total_inserted = quarters + dimes + nickels + pennies
    item_cost = menu[item]["cost"]
    if total_inserted < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        return

    change = total_inserted - item_cost
    
    # Verificar se a máquina tem dinheiro suficiente para dar o troco
    if change > resources["money"]:
        print(f"Sorry, the machine doesn't have enough change (${change:.2f} needed, ${resources['money']:.2f} available). Money refunded.")
        return
    
    if change > 0:
        print(f"Here is ${change:.2f} in change.")
        resources["money"] -= change  # Retirando o troco do dinheiro da máquina

    # Atualizando os recursos da maquina
    resources["money"] += total_inserted  # Adiciona todo o dinheiro inserido
    resources["water"] -= menu[item]["water"]
    resources["coffee"] -= menu[item]["coffee"]
    if "milk" in menu[item]:
        resources["milk"] -= menu[item]["milk"]

    # Entregando o item
    print(f"Here is your {item}. Enjoy!")

print("Welcome to the Coffee Machine!")

while exit == False:
    # Mostrando o menu
    print("\nMenu:")
    print("1. Print options")
    print("2. Order item")
    print("3. Exit")
    print("4. admin")
    
    # Solicitando escolha do usuario
    choice = input("Please choose an option (1, 2, 3 or 4 if you are admin): ")
    
    if choice == "1":
        print_options()
    elif choice == "2":
        item = input("What would you like to order?(espresso/latte/cappuccino): ")

        match item:
            case "espresso":
                order_item("espresso")
            case "latte":
                order_item("latte")
            case "cappuccino":
                order_item("cappuccino")
            case _:
                print("Invalid item selected, Try again.")

    elif choice == "3":
        exit = True
    elif choice == "4":
        password = input("Enter admin password: ")
        if password == "admin123":

            refill_choice = input("\nRefill Resources? (yes/no): ").lower().strip()
                        
            if refill_choice == "yes":
                print("Access granted. You can now refill resources.")
                water_add = int(input("Enter amount of water to add (ml): "))
                milk_add = int(input("Enter amount of milk to add (ml): "))
                coffee_add = int(input("Enter amount of coffee to add (g): "))
                
                add_money = input("Do you want to add money for change? (yes/no): ").lower().strip()
                if add_money == "yes":
                    money_add = float(input("Enter amount of money to add ($): "))
                    resources["money"] += money_add

                resources["water"] += water_add
                resources["milk"] += milk_add
                resources["coffee"] += coffee_add

                print("Resources refilled successfully.")
            elif refill_choice == "no":
                print("\n--- Machine Report ---")
                print_report()
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")

        else:
            print("Incorrect password. Access denied.")
    else:
        print("Invalid choice, please try again.")