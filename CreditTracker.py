import os

cards = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def add_card():
    clear_screen()
    print("*" * 59)
    print("Add Card - Enter card details to save a new card")
    print("(takes just a few seconds and requires manual input)")
    print("*" * 59)

    name = input("Card Nickname: ")
    last4 = input("Last 4 of Card #: ")
    balance = float(input("Card Balance: "))
    limit = float(input("Credit Limit: "))

    card = {
        "name": name,
        "last4": last4,
        "balance": balance,
        "limit": limit
    }

    cards.append(card)

    print("\nCard saved successfully.")
    input("Press Enter to return to the Main Menu...")


def view_cards():
    while True:
        clear_screen()
        print("*" * 59)
        print("View All Cards - Displays a brief description of each card")
        print("*" * 59)

        if len(cards) == 0:
            print("No cards have been added yet.\n")
            input("Press Enter to return to the Main Menu...")
            return

        print(f"{'#':<5}{'Name':<20}{'Card #':<10}{'Balance':<12}")
        print("-" * 59)

        for index, card in enumerate(cards, start=1):
            print(
                f"{index:<5}"
                f"{card['name']:<20}"
                f"{card['last4']:<10}"
                f"{card['balance']:<12}"
            )

        choice = input("\nEnter a number to see more details or B to return: ")

        if choice.lower() == "b":
            return

        if not choice.isdigit():
            print("Invalid input. Please enter a card number or B to return.")
            input("Press Enter to continue...")
            continue

        choice = int(choice)

        if 1 <= choice <= len(cards):
            selected_card = cards[choice - 1]
            clear_screen()
            utilization = selected_card['balance'] / selected_card['limit'] * 100


            print("\nCard Details")
            print("-" * 25)
            print(f"Card Nickname: {selected_card['name']}")
            print(f"Last 4 of Card #: {selected_card['last4']}")
            print(f"Card Balance: ${selected_card['balance']:.2f}")
            print(f"Credit Limit: ${selected_card['limit']:.2f}")
            print(f"Utilization %: {utilization:.2f}%")
            print("-" * 25)

            input("\nPress Enter to return to View All Cards...")
        else:
            print("Invalid card number.")
            input("Press Enter to continue...")


def remove_card():
    clear_screen()
    print("*" * 59)
    print("Remove Card - Remove one of your existing cards")
    print("*" * 59)

    if len(cards) == 0:
        print("No cards are available to remove.\n")
        input("Press Enter to return to the Main Menu...")
        return

    print(f"{'#':<5}{'Name':<20}{'Card #':<10}")
    print("-" * 35)

    for index, card in enumerate(cards, start=1):
        print(f"{index:<5}{card['name']:<20}{card['last4']:<10}")

    choice = input("\nEnter a number OR enter card name to remove, or B to return: ")

    if choice.lower() == "b":
        return

    selected_card = None

    if choice.isdigit():
        choice_number = int(choice)

        if 1 <= choice_number <= len(cards):
            selected_card = cards[choice_number - 1]
    else:
        for card in cards:
            if card["name"].lower() == choice.lower():
                selected_card = card
                break

    if selected_card is None:
        print("Card not found.")
        input("Press Enter to return to the Main Menu...")
        return

    confirm = input(f"Are you sure you want to remove this card? {selected_card['name']} (Y/N): ")

    if confirm.lower() == "y":
        cards.remove(selected_card)
        print(f"{selected_card['name']} was removed.")
    else:
        print("Removal canceled.")

    input("Press Enter to return to the Main Menu...")


def main_menu():
    while True:
        clear_screen()
        print("*" * 59)
        print("MAIN MENU")
        print("Track balances and organize your credit cards in one place.")
        print("*" * 59)
        print("1. Add Card")
        print("2. View Cards")
        print("3. Remove Card")
        print("4. Exit")

        choice = input("\nInput your selection: ")

        if choice == "1":
            add_card()
        elif choice == "2":
            view_cards()
        elif choice == "3":
            remove_card()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
            input("Press Enter to continue...")


main_menu()
