documentation = """
# Checklist Application Documentation

This document explains how to use the simple command-line checklist application.

## How to Run the Application

1.  Save the provided Python code as a file (e.g., `checklist_app.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the application using the command:
    ```bash
    python checklist_app.py
    ```

## Interacting with the Menu

When you run the application, you will be presented with a menu of options:

```
--- Menu ---
1. View Checklist
2. Add Task
3. Remove Task
4. Mark Task Status
5. Save and Exit
------------
Enter your choice:
```

Enter the number corresponding to the action you want to perform and press Enter.

*   **1. View Checklist:** Displays your current checklist with the status (Completed or Incomplete) for each task.
*   **2. Add Task:** Prompts you to enter a new task to add to your checklist. New tasks are added as Incomplete by default.
*   **3. Remove Task:** Prompts you to enter the task you want to remove from the checklist.
*   **4. Mark Task Status:** Iterates through your current checklist, asking you for the status (yes/no) for each task. This updates the completed/incomplete status of your tasks.
*   **5. Save and Exit:** Saves the current state of your checklist and task statuses to a file and exits the application.

## Examples

Here are some examples of how to use the menu options:

### Viewing the Checklist

```
--- Menu ---
1. View Checklist
2. Add Task
3. Remove Task
4. Mark Task Status
5. Save and Exit
------------
Enter your choice: 1

--- Your Checklist ---
1. wake up (Completed)
2. do assignments (Incomplete)
3. eat lunch (Incomplete)
4. go to sleep (Completed)
----------------------
```

### Adding a Task

```
--- Menu ---
1. View Checklist
2. Add Task
3. Remove Task
4. Mark Task Status
5. Save and Exit
------------
Enter your choice: 2
Enter the new task to add: Buy groceries
'Buy groceries' added to the checklist.

Checklist saved to checklist.json
```

### Removing a Task

```
--- Menu ---
1. View Checklist
2. Add Task
3. Remove Task
4. Mark Task Status
5. Save and Exit
------------
Enter your choice: 3
Enter the task to remove: eat lunch
'eat lunch' removed from the checklist.

Checklist saved to checklist.json
```

### Marking Task Status

```
--- Menu ---
1. View Checklist
2. Add Task
3. Remove Task
4. Mark Task Status
5. Save and Exit
------------
Enter your choice: 4

Marking tasks:

Processing checklist for final status:
Did you wake up? (yes/no): yes
Did you do assignments? (yes/no): no
Did you Buy groceries? (yes/no): yes
Did you go to sleep? (yes/no): yes

--- Task Status ---

Completed tasks:
- wake up
- Buy groceries
- go to sleep

Incomplete tasks:
- do assignments
-------------------

Checklist saved to checklist.json
```

## Persistence (Saving and Loading)

The application automatically saves your checklist and the status of each task to a file named `checklist.json` whenever you:

*   Add a task
*   Remove a task
*   Mark task statuses
*   Choose the "Save and Exit" option

When you run the application, it will automatically look for the `checklist.json` file in the same directory. If the file exists, it will load your previous checklist and task statuses, allowing you to continue where you left off. If the file is not found, it will start with a default or empty checklist.

This ensures that your checklist data is persistent between application runs.
"""

print(documentation)