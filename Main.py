from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice

while True:
    print("\n========== Coffee Shop ==========")
    print("1. Namayesh menu cafe")
    print("2. Sabt sefaresh")
    print("3. Namayesh sefareshha")
    print("4. Mohasebe mablagh kol")
    print("5. Chap factor")
    print("6. Khorooj")
    choice = input("Entekhab shoma: ").strip()

    if choice == "1":
        show_menu()
    elif choice == "2":
        add_order()
    elif choice == "3":
        show_orders()
    elif choice == "4":
        print(f"Mablagh kol: {calculate_total()} toman")
    elif choice == "5":
        print_invoice()
    elif choice == "6":
        print("Khodahafez!")
        break
    else:
        print("Gozine namotabar ast!")