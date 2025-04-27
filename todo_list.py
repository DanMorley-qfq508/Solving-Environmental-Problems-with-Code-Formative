class TodoList:
    def __init__(self, filename="todo_list.txt"):
        self.filename = filename
        self.todo_items = self.load_list()

    def load_list(self):
        # Load the to-do list from the file if it exists, otherwise return an empty list
        try:
            with open(self.filename, "r") as file:
                items = file.readlines()
            return [item.strip() for item in items]  # Strip newline characters
        except FileNotFoundError:
            return []  # If the file doesn't exist, return an empty list

    def save_list(self):
        # Save the to-do list to the file
        with open(self.filename, "w") as file:
            for item in self.todo_items:
                file.write(item + "\n")

    def add_item(self, item):
        # Adds an item to the todo list and saves the list to the file
        self.todo_items.append(item)
        self.save_list()
        print(f'Added: {item}')

    def print_list(self):
        # Prints the current todo list
        if not self.todo_items:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, item in enumerate(self.todo_items, 1):
                print(f"{idx}. {item}")

    def remove_item(self, index):
        # Removes an item from the todo list by index and saves the list to the file
        try:
            removed_item = self.todo_items.pop(index - 1)
            self.save_list()
            print(f'Removed: {removed_item}')
        except IndexError:
            print("Invalid index. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Print list")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            todo_list.add_item(item)

        elif choice == '2':
            todo_list.print_list()

        elif choice == '3':
            todo_list.print_list()
            try:
                index = int(input("Enter the index of the item to remove: "))
                todo_list.remove_item(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
class TodoList:
    def __init__(self):
        # Initializes the todo list as an empty list
        self.todo_items = []

    def add_item(self, item):
        # Adds an item to the todo list
        self.todo_items.append(item)
        print(f'Added: {item}')

    def print_list(self):
        # Prints the current todo list
        if not self.todo_items:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, item in enumerate(self.todo_items, 1):
                print(f"{idx}. {item}")

    def remove_item(self, index):
        # Removes an item from the todo list by index
        try:
            removed_item = self.todo_items.pop(index - 1)
            print(f'Removed: {removed_item}')
        except IndexError:
            print("Invalid index. Please try again.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Print list")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            item = input("Enter the item to add: ")
            todo_list.add_item(item)

        elif choice == '2':
            todo_list.print_list()

        elif choice == '3':
            todo_list.print_list()
            try:
                index = int(input("Enter the index of the item to remove: "))
                todo_list.remove_item(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


