from Menu import menu

orders = []


def add_order():
    name = input("Name mahsool: ").strip().lower()
    if name not in menu:
        print("In mahsool dar menu vojud nadarad!")
        return

    count = input("Tedad: ").strip()
    if not count.isdigit() or int(count) <= 0:
        print("Tedad namotabar ast!")
        return

    orders.append({
        "name": name,
        "price": menu[name],
        "count": int(count)
    })
    print("Sefaresh sabt shod.")


def show_orders():
    if len(orders) == 0:
        print("Hanuz sefareshi sabt nashode ast.")
        return

    print("\n----- Sefareshha -----")
    for order in orders:
        print(f"{order['name']} | Gheymat: {order['price']} | Tedad: {order['count']}")