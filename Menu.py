menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000
}


def show_menu():
    print("\n----- Menu cafe -----")
    for name, price in menu.items():
        print(f"{name}: {price} toman")