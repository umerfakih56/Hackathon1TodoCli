# In-Memory CLI Todo Application

A simple command-line todo list application built with Python that stores all data in memory during runtime.

## Features

- ✅ Add new todo items with title and optional description
- ✅ View all todos with their completion status
- ✅ Mark todos as completed
- ✅ Update todo title or description
- ✅ Delete todos
- ✅ Interactive menu-driven CLI
- ✅ In-memory storage (no persistence)

## Requirements

- Python 3.13 or higher
- No external dependencies (uses Python standard library only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/asadaligith/Todo-App-CLI-Based.git
cd Todo-App-CLI-Based
```

2. No additional installation needed - uses Python standard library only

## Usage

Run the application:
```bash
python main.py
```

### Available Commands

The application will display an interactive menu with the following options:

1. **Add Todo** - Create a new todo item
2. **List Todos** - Display all todos with their status
3. **Mark Complete** - Mark a todo as completed
4. **Update Todo** - Modify title or description
5. **Delete Todo** - Remove a todo from the list
6. **Exit** - Quit the application

### Example Workflow

```bash
$ python main.py

=== Todo List Manager ===
1. Add Todo
2. List Todos
3. Mark Complete
4. Update Todo
5. Delete Todo
6. Exit

Enter choice: 1
Enter title: Buy groceries
Enter description (optional): Milk, eggs, bread

Todo added successfully!
```

## Architecture

The application follows a three-layer architecture:

- **Models** (`src/models/`) - Data structures (Todo)
- **Services** (`src/services/`) - Business logic (TodoService)
- **CLI** (`src/cli/`) - User interface (TodoCLI)

## Project Structure

```
.
├── main.py                 # Application entry point
├── src/
│   ├── models/
│   │   └── todo.py        # Todo data model
│   ├── services/
│   │   └── todo_service.py # Business logic
│   └── cli/
│       └── todo_cli.py    # CLI interface
├── specs/                  # Feature specifications
└── README.md
```

## Design Principles

This application follows these core principles:

- **Code Quality**: PEP-8 compliant, clean, maintainable code
- **In-Memory Only**: No file I/O, databases, or external storage
- **CLI-First**: Simple, predictable command-line interface
- **Separation of Concerns**: Clear architectural boundaries
- **No External Dependencies**: Standard library only

## Data Persistence

⚠️ **Important**: All todo data exists only in memory and will be lost when the application exits. This is by design - the application is intended for temporary task tracking during a single session.

## Contributing

This project follows spec-driven development. See the `specs/` directory for detailed specifications, plans, and tasks.

## License

MIT License
