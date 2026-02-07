"""
Todo data model.

This module defines the Todo class which represents a single todo item.
"""


class Todo:
    """
    Represents a todo item with id, title, description, and completion status.

    Attributes:
        id (int): Unique identifier for the todo.
        title (str): The todo's title (required).
        description (str): Optional description providing more details.
        is_completed (bool): Whether the todo has been completed.
    """

    def __init__(self, id: int, title: str, description: str = ""):
        """
        Initialize a new Todo instance.

        Args:
            id: Unique identifier for the todo.
            title: The todo's title.
            description: Optional description (default: empty string).
        """
        self.id = id
        self.title = title
        self.description = description
        self.is_completed = False

    def __repr__(self) -> str:
        """
        Return string representation of Todo for debugging.

        Returns:
            String representation showing all attributes.
        """
        status = "✓" if self.is_completed else " "
        return (
            f"Todo(id={self.id}, title='{self.title}', "
            f"description='{self.description}', completed=[{status}])"
        )

    def __str__(self) -> str:
        """
        Return user-friendly string representation of Todo.

        Returns:
            Formatted string for display.
        """
        status = "[✓]" if self.is_completed else "[ ]"
        desc = f" - {self.description}" if self.description else ""
        return f"{status} {self.id}. {self.title}{desc}"
