import data, art

options = {1:"espresso", 2:"latte", 3: "cappuccino"}

def receiveOrder():
    orderNo = input("Type the number corresponding to your order: ")
    try:
        orderNo = int(orderNo)
        if orderNo in options:
            order = options[orderNo]
            return order
        else:
            return
    except ValueError:
        return orderNo.lower()


def receiveMoney(order):
    total = 0
    if order in data.menu:
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
    else:
        return

def processMoney(total, order):
    price = data.menu[order]['cost']
    balance = total - price
    if balance < 0:
        return False, balance
    else:
        return True, balance


def checkResources(order):
    waterNeeded = data.menu[order]["ingredients"]["water"]
    coffeeNeeded = data.menu[order]["ingredients"]["coffee"]
    if "milk" in data.menu[order]["ingredients"]:
        milkNeeded = data.menu[order]["ingredients"]["milk"]
    else: milkNeeded = 0
    return waterNeeded, coffeeNeeded, milkNeeded


