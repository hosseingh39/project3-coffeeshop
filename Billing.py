from Order import orders


def calculate_total():
    total = 0
    for order in orders:
        total += order["price"] * order["count"]
    return total


def calculate_discount(total):
    if total > 1000000:
        return total * 10 / 100
    return 0


def print_invoice():
    if len(orders) == 0:
        print("Sefareshi baraye sodur factor vojud nadarad.")
        return

    total = calculate_total()
    discount = calculate_discount(total)
    final = total - discount

    print("\n========== Factor ==========")
    for order in orders:
        print(f"{order['name']} x {order['count']}")
    print("----------------------------")
    print(f"Mablagh kol: {total} toman")
    print(f"Takhfif: {discount} toman")
    print(f"Mablagh ghabel pardakht: {final} toman")
    print("============================")