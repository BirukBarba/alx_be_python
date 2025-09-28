
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item name: ")
            shopping_list.append(f"{item}")
            print(f"{item} is added to the list.")
            # Prompt for and add an item
            pass
        elif choice == '2':
            item = input("Enter the item name: ")
            shopping_list.remove(f"{item}")
            print(f"{item} is removed from the list.")
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()