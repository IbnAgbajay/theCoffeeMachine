import functions, art, data

waterAvailable = data.resources["water"]
coffeeAvailable = data.resources["coffee"]
milkAvailable = data.resources["milk"]

till = 0

def resourceIsSufficient(order):
    water, coffee, milk = functions.checkResources(order)
    if waterAvailable >= water and coffeeAvailable >= coffee and milkAvailable >= milk:
        return True
    elif waterAvailable < water:
        return "water"
    elif coffeeAvailable < coffee:
        return "coffee"
    else: return "milk"

def generateReport():
    print(f"Water: {waterAvailable}ml")
    print(f"Coffee: {coffeeAvailable}g")
    print(f"Milk: {milkAvailable}ml")
    print(f"Money: ${till:.2f}")

machineIsOn = True
while machineIsOn:
    print(art.logo)
    orderIsValid = True
    while orderIsValid:

        print("Welcome to the Coffee Mixer!")
        option = functions.receiveOrder()
        if option == "off":
            orderIsValid = False
            machineIsOn = False
        elif option == "report":
            orderIsValid = False
            generateReport()

        elif option in data.menu:
            # check if resources are sufficient for order
            outcome = resourceIsSufficient(option)
            if outcome is True:
                price = data.menu[option]['cost']
                print(f"You ordered {option.title()}. The price is ${price:.2f}")
                print(f"Please insert your coins in the slot.")
                money = functions.receiveMoney(option)
                output = functions.processMoney(money, option)
                moneyIsSufficient = output[0]
                balance = output[1]

                if moneyIsSufficient:
                    print(f"The total deposit is ${money:.2f}")
                    if balance > 0:
                        print(f"Here is your balance of ${balance:.2f}")

                    # addToTill
                    till += price

                    # processOrder
                    resources = functions.checkResources(option)
                    waterAvailable -= resources[0]
                    coffeeAvailable -= resources[1]
                    milkAvailable -= resources[2]
                    print(f"Here is your hot cup of {option.title()}.\n{art.coffee[option]}")

                else:
                    # return money
                    orderIsValid = False
                    print(f"Your money (${money:.2f})  is insufficent for the order. Here is your refund!")

            else:
                # giveFeedback
                print(f"Apologies. There is insufficient {outcome} to process this order.")
        else:
            orderIsValid = False
            print("Invalid selection!")
