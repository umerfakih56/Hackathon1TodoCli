"""
CLI interface for the Todo application.

This module provides the command-line interface for interacting with todos.
"""

from src.services.todo_service import TodoService


class TodoCLI:
    """
    Command-line interface for the Todo application.

    Provides an interactive menu system for managing todos.

    Attributes:
        service (TodoService): The service handling business logic.
    """

    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a TodoService instance.

        Args:
            service: TodoService instance for managing todos.
        """
        self.service = service

    def display_menu(self):
        """Display the main menu options."""
        print("\n" + "=" * 40)
        print("Todo List Manager".center(40))
        print("=" * 40)
        print("1. Add Todo")
        print("2. List Todos")
        print("3. Mark Complete")
        print("4. Update Todo")
        print("5. Delete Todo")
        print("6. Exit")
        print("=" * 40)

    def handle_add_todo(self):
        """
        Handle adding a new todo.

        Prompts user for title and optional description,
        then creates the todo using the service.
        """
        print("\n--- Add New Todo ---")
        title = input("Enter title: ").strip()

        if not title:
            print("❌ Error: Title cannot be empty")
            return

        description = input("Enter description (optional): ").strip()

        try:
            todo = self.service.add_todo(title, description)
            print(f"\n✓ Todo added successfully! (ID: {todo.id})")
        except ValueError as e:
            print(f"❌ Error: {e}")

    def handle_list_todos(self):
        """
        Handle listing all todos.

        Displays all todos with formatted output showing ID, title,
        description, and completion status.
        """
        print("\n--- All Todos ---")
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos yet. Add one to get started!")
            return

        print()
        for todo in todos:
            status = "[✓]" if todo.is_completed else "[ ]"
            print(f"{status} {todo.id}. {todo.title}")
            if todo.description:
                print(f"     {todo.description}")
        print()

    def handle_complete_todo(self):
        """
        Handle marking a todo as completed.

        Prompts user for todo ID and marks it as complete.
        """
        print("\n--- Mark Todo Complete ---")
        try:
            todo_id = int(input("Enter todo ID: "))
            if self.service.complete_todo(todo_id):
                print(f"\n✓ Todo {todo_id} marked as complete!")
            else:
                print(f"❌ Error: Todo with ID {todo_id} not found")
        except ValueError:
            print("❌ Error: Please enter a valid number")

    def handle_update_todo(self):
        """
        Handle updating a todo.

        Prompts user for todo ID and new values for title and/or description.
        """
        print("\n--- Update Todo ---")
        try:
            todo_id = int(input("Enter todo ID: "))

            # Check if todo exists first
            todo = self.service.get_todo_by_id(todo_id)
            if not todo:
                print(f"❌ Error: Todo with ID {todo_id} not found")
                return

            print(f"\nCurrent: {todo.title}")
            print("(Press Enter to keep current value)")

            title_input = input("New title: ").strip()
            description_input = input("New description: ").strip()

            # Only update if at least one value provided
            title = title_input if title_input else None
            description = description_input if description_input else None

            if title is None and description is None:
                print("No changes made")
                return

            try:
                if self.service.update_todo(todo_id, title, description):
                    print(f"\n✓ Todo {todo_id} updated successfully!")
                else:
                    print(f"❌ Error: Todo with ID {todo_id} not found")
            except ValueError as e:
                print(f"❌ Error: {e}")

        except ValueError:
            print("❌ Error: Please enter a valid number")

    def handle_delete_todo(self):
        """
        Handle deleting a todo.

        Prompts user for todo ID and deletes it from the list.
        """
        print("\n--- Delete Todo ---")
        try:
            todo_id = int(input("Enter todo ID: "))
            if self.service.delete_todo(todo_id):
                print(f"\n✓ Todo {todo_id} deleted successfully!")
            else:
                print(f"❌ Error: Todo with ID {todo_id} not found")
        except ValueError:
            print("❌ Error: Please enter a valid number")

    def run(self):
        """
        Run the main application loop.

        Displays menu, processes user input, and executes commands until exit.
        """
        print("\n✨ Welcome to Todo List Manager! ✨")
        print("Manage your tasks efficiently - all data stored in memory")

        while True:
            self.display_menu()
            choice = input("\nEnter choice (1-6): ").strip()

            if choice == "1":
                self.handle_add_todo()
            elif choice == "2":
                self.handle_list_todos()
            elif choice == "3":
                self.handle_complete_todo()
            elif choice == "4":
                self.handle_update_todo()
            elif choice == "5":
                self.handle_delete_todo()
            elif choice == "6":
                print("\n👋 Thanks for using Todo List Manager!")
                print("⚠️  Remember: All data will be lost on exit (in-memory only)")
                break
            else:
                print("\n❌ Invalid choice. Please select 1-6")
