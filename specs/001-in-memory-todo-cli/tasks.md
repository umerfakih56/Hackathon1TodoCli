# Tasks: In-Memory CLI Todo Application

**Input**: Design documents from `/specs/001-in-memory-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Not requested in specification - tasks focus on implementation only

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `main.py` at repository root
- Paths shown below follow single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure (src/, src/models/, src/services/, src/cli/)
- [x] T002 [P] Create .gitignore with Python patterns (__pycache__/, *.pyc, .venv/, venv/, .env*)
- [x] T003 [P] Create README.md with project overview and usage instructions

**Checkpoint**: Project structure ready

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Todo data model in src/models/todo.py with id, title, description, and is_completed attributes
- [x] T005 Create TodoService class in src/services/todo_service.py with in-memory storage (list-based)
- [x] T006 Implement unique ID generation in TodoService (sequential starting from 1)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Todos (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todos and display them in a list

**Independent Test**: Add one or more todos and display the list - delivers working task tracker

### Implementation for User Story 1

- [x] T007 [US1] Implement add_todo() method in src/services/todo_service.py with title and optional description parameters
- [x] T008 [US1] Implement get_all_todos() method in src/services/todo_service.py to return all todos
- [x] T009 [US1] Add title validation in add_todo() to reject empty titles with clear error message
- [x] T010 [US1] Create CLI menu system in src/cli/todo_cli.py with display_menu() function
- [x] T011 [US1] Implement handle_add_todo() CLI handler in src/cli/todo_cli.py that prompts for title and description
- [x] T012 [US1] Implement handle_list_todos() CLI handler in src/cli/todo_cli.py that formats and displays all todos
- [x] T013 [US1] Create main application loop in main.py that initializes TodoService and runs CLI menu
- [x] T014 [US1] Add formatted output for todo list showing ID, title, description, and completion status

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Complete Todos (Priority: P2)

**Goal**: Enable users to mark todos as completed and distinguish completed from incomplete

**Independent Test**: Create todos (P1 functionality) and mark them as completed - delivers task completion workflow

### Implementation for User Story 2

- [x] T015 [US2] Implement complete_todo(todo_id) method in src/services/todo_service.py
- [x] T016 [US2] Add validation in complete_todo() to check if todo exists and return clear error for invalid IDs
- [x] T017 [US2] Handle gracefully when marking already-completed todo as completed (no error, idempotent operation)
- [x] T018 [US2] Implement handle_complete_todo() CLI handler in src/cli/todo_cli.py that prompts for todo ID
- [x] T019 [US2] Update display formatting in handle_list_todos() to visually distinguish completed todos (e.g., [✓] vs [ ])
- [x] T020 [US2] Add "Mark Complete" option to CLI menu in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todos (Priority: P3)

**Goal**: Enable users to update title or description of existing todos

**Independent Test**: Create todos (P1), then update their title or description - delivers task editing capability

### Implementation for User Story 3

- [x] T021 [US3] Implement update_todo(todo_id, title=None, description=None) method in src/services/todo_service.py
- [x] T022 [US3] Add validation in update_todo() to check if todo exists and return clear error for invalid IDs
- [x] T023 [US3] Add title validation in update_todo() to reject empty titles when updating
- [x] T024 [US3] Support optional description updates (allow adding, changing, or removing description)
- [x] T025 [US3] Implement handle_update_todo() CLI handler in src/cli/todo_cli.py that prompts for ID and new values
- [x] T026 [US3] Add "Update Todo" option to CLI menu in src/cli/todo_cli.py

**Checkpoint**: All user stories 1, 2, and 3 should now be independently functional

---

## Phase 6: User Story 4 - Delete Todos (Priority: P4)

**Goal**: Enable users to delete todos to keep list clean

**Independent Test**: Create todos (P1) and delete specific ones - delivers list management capability

### Implementation for User Story 4

- [x] T027 [US4] Implement delete_todo(todo_id) method in src/services/todo_service.py
- [x] T028 [US4] Add validation in delete_todo() to check if todo exists and return clear error for invalid IDs
- [x] T029 [US4] Implement handle_delete_todo() CLI handler in src/cli/todo_cli.py that prompts for todo ID
- [x] T030 [US4] Add confirmation message after successful deletion
- [x] T031 [US4] Add "Delete Todo" option to CLI menu in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T032 [P] Add input validation for numeric ID inputs in all CLI handlers (handle non-numeric gracefully)
- [x] T033 [P] Add error handling for edge cases (empty list display, special characters in titles/descriptions)
- [x] T034 [P] Implement clean exit option in CLI menu (quit/exit command)
- [x] T035 [P] Add welcome message and usage instructions when application starts
- [x] T036 [P] Format error messages consistently across all operations
- [x] T037 Update README.md with detailed usage examples for each operation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 but independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on US1 but independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Builds on US1 but independently testable

### Within Each User Story

- Foundational tasks (T004-T006) MUST complete before any user story
- Service methods before CLI handlers
- CLI handlers before menu integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T002, T003)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All Polish tasks marked [P] can run in parallel (T032-T036)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deliver MVP (can add and view todos)

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deliver MVP (add + view)
3. Add User Story 2 → Test independently → Deliver (add + view + complete)
4. Add User Story 3 → Test independently → Deliver (add + view + complete + update)
5. Add User Story 4 → Test independently → Deliver (full CRUD + complete)
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All data stored in-memory only (Python list in TodoService)
- No external dependencies required (standard library only)
- Application follows PEP-8 conventions
