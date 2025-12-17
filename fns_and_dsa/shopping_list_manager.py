list_of_shopping_lists = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return input("Enter your choice: ")


def add_shopping_list(name: str):
    list_of_shopping_lists.append(name)
    return list_of_shopping_lists


def remove_shopping_list(name: str):
    try:
        list_of_shopping_lists.remove(name)
    except ValueError:
        print(f"'{name}' not found in shopping lists.")
    return list_of_shopping_lists


def display_shopping_lists():
    if not list_of_shopping_lists:
        print("No shopping lists.")
    else:
        for i, item in enumerate(list_of_shopping_lists, 1):
            print(f"{i}. {item}")
    return list_of_shopping_lists


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            name = input("Enter the name of the shopping list: ").strip()
            if name:
                add_shopping_list(name)
                print("Added.")
            else:
                print("Name cannot be empty.")
        elif choice == "2":
            name = input("Enter the name to remove: ").strip()
            if name:
                remove_shopping_list(name)
        elif choice == "3":
            display_shopping_lists()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()

