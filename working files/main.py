import art, data


def receiveOrder():
    # returns a string (a customer order, an admin command or None)
    orderNo = input("Type the number corresponding to your order: ")
    try:
        orderNo = int(orderNo)
        if orderNo in menu:
            order = menu[orderNo]
            return order
        else:
            return
    except ValueError:
        return orderNo.lower()


def getResources(order):
    waterNeeded = data.menu[order]["ingredients"]["water"]
    coffeeNeeded = data.menu[order]["ingredients"]["coffee"]
    if "milk" in data.menu[order]["ingredients"]:
        milkNeeded = data.menu[order]["ingredients"]["milk"]
    else: milkNeeded = 0
    return waterNeeded, coffeeNeeded, milkNeeded


def resourceIsSufficient(order):
    water, coffee, milk = getResources(order)
    if stock["waterAvailable"] >= water and stock["coffeeAvailable"] >= coffee and stock["milkAvailable"] >= milk:
        return True
    elif stock["waterAvailable"] < water:
        return "water"
    elif stock["coffeeAvailable"] < coffee:
        return "coffee"
    else: return "milk"


def receiveMoney(order):
    total = 0
    price = data.menu[order]['cost']
    quarters = int(input("How many quarters: "))
    total += quarters * 0.25
    if total < price:
        dimes = int(input("How many dimes: "))
        total += dimes * 0.1
        if total < price:
            nickels = int(input("How many nickels: "))
            total += nickels * 0.05
    return total


def processMoney(order):
    total = receiveMoney(order)
    price = data.menu[order]['cost']
    balance = total - price
    if balance < 0:
        return False, balance, total
    else:
        return True, balance, total


def generateReport():
    print(f"Water: {stock["waterAvailable"]}ml")
    print(f"Coffee: {stock["coffeeAvailable"]}g")
    print(f"Milk: {stock["milkAvailable"]}ml")
    print(f"Money: ${till:.2f}")


machineIsOn = True

menu = {}
for num, item in zip(range(1,10), data.menu):
    menu[num] = item

stock ={"waterAvailable": data.resources["water"],
        "coffeeAvailable": data.resources["coffee"],
        "milkAvailable": data.resources["milk"]}

till = 0

while machineIsOn:

    orderIsValid = True
    while orderIsValid:
        print(art.logo)
        print("Welcome to the Coffee Mixer!")
        option = receiveOrder()     # receive order from user
        if option == "off":         # check if it is admin command to switch off machine
            orderIsValid = False
            machineIsOn = False
        elif option == "report":    # check if it is admin command to generate report
            orderIsValid = False
            generateReport()

        elif option in data.menu:   # check if it is a valid menu order
            outcome = resourceIsSufficient(option)
            if outcome is True:     # check if resources are sufficient for order
                price = data.menu[option]['cost']
                print(f"You ordered {option.title()}. The price is ${price:.2f}")
                print(f"Please insert your coins in the slot.")
                # money = receiveMoney(option)
                # output = processMoney(money, option)
                funds = processMoney(option)      # receive money and calculate
                moneyIsSufficient = funds[0]
                balance = funds[1]; total = funds[2]

                if moneyIsSufficient:       # check if funds is sufficient for order
                    print(f"The total deposit is ${total:.2f}")
                    if balance > 0:
                        print(f"Here is your balance of ${balance:.2f}\n {art.coins}")
                        input("Press any key to continue")

                    # addToTill
                    till += price      # if funds are sufficient, add coins to till

                    # processOrder
                    resources = getResources(option)
                    stock["waterAvailable"] -= resources[0]
                    stock["coffeeAvailable"] -= resources[1]
                    stock["milkAvailable"] -= resources[2]
                    print(f"Here is your hot cup of {option.title()}.\n{art.coffee[option]}")
                    input("Press any key to continue")

                else:
                    # return money if found to be insufficient
                    orderIsValid = False
                    print(f"Your money (${total:.2f})  is insufficent for the order. Here is your refund!\n{art.dollar}")
                    input("Press any key to continue")

            else:
                # giveFeedback if resources available are not enough for order
                print(f"Apologies. There is insufficient {outcome} to process this order.")
        else:
            # give feedback; order is not valid
            orderIsValid = False
            print("Invalid selection!")

# TODO: Handle exceptions for data inputs, blank or invalid inputs