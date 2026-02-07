#!/usr/bin/env python3
"""
Main entry point for the In-Memory CLI Todo Application.

This application provides an interactive command-line interface for managing
todo items stored in memory during runtime.
"""

from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI


def main():
    """
    Initialize and run the Todo application.

    Creates a TodoService instance and starts the CLI interface.
    """
    # Initialize service and CLI
    service = TodoService()
    cli = TodoCLI(service)

    # Run the application
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Application interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please report this issue if it persists.")


if __name__ == "__main__":
    main()
