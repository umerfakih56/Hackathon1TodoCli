"""
TodoService - Business logic for todo operations.

This module provides the TodoService class which manages todo items in memory.
"""

from typing import List, Optional
from src.models.todo import Todo


class TodoService:
    """
    Service class for managing todo items in memory.

    This class provides CRUD operations for todos and maintains an in-memory
    list of all todo items. Data is lost when the application terminates.

    Attributes:
        _todos (List[Todo]): In-memory list storing all todo items.
        _next_id (int): Counter for generating unique todo IDs.
    """

    def __init__(self):
        """Initialize TodoService with empty todo list and ID counter at 1."""
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def _generate_id(self) -> int:
        """
        Generate a unique ID for a new todo.

        Returns:
            Unique integer ID (sequential starting from 1).
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_todo(self, title: str, description: str = "") -> Todo:
        """
        Add a new todo item.

        Args:
            title: The todo's title (required, cannot be empty).
            description: Optional description (default: empty string).

        Returns:
            The newly created Todo object.

        Raises:
            ValueError: If title is empty or contains only whitespace.
        """
        # Validate title
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        # Create and store new todo
        todo = Todo(
            id=self._generate_id(),
            title=title.strip(),
            description=description.strip() if description else ""
        )
        self._todos.append(todo)
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Retrieve all todo items.

        Returns:
            List of all Todo objects (may be empty).
        """
        return self._todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Find a todo by its ID.

        Args:
            todo_id: The ID of the todo to find.

        Returns:
            Todo object if found, None otherwise.
        """
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def complete_todo(self, todo_id: int) -> bool:
        """
        Mark a todo as completed.

        Args:
            todo_id: The ID of the todo to mark complete.

        Returns:
            True if todo was found and marked complete, False otherwise.
        """
        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.is_completed = True
            return True
        return False

    def update_todo(
        self,
        todo_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> bool:
        """
        Update a todo's title and/or description.

        Args:
            todo_id: The ID of the todo to update.
            title: New title (if provided, cannot be empty).
            description: New description (if provided).

        Returns:
            True if todo was found and updated, False otherwise.

        Raises:
            ValueError: If provided title is empty or contains only whitespace.
        """
        todo = self.get_todo_by_id(todo_id)
        if not todo:
            return False

        # Update title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Title cannot be empty")
            todo.title = title.strip()

        # Update description if provided
        if description is not None:
            todo.description = description.strip() if description else ""

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete.

        Returns:
            True if todo was found and deleted, False otherwise.
        """
        for i, todo in enumerate(self._todos):
            if todo.id == todo_id:
                self._todos.pop(i)
                return True
        return False
