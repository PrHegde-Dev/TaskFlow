import json
import os

def save_checklist(checklist, completed_tasks, incomplete_tasks, filename="checklist.json"):
    """Saves the checklist and task statuses to a JSON file."""
    data = {
        "checklist": checklist,
        "completed_tasks": completed_tasks,
        "incomplete_tasks": incomplete_tasks
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"\nChecklist saved to {filename}")

def load_checklist(filename="checklist.json"):
    """Loads the checklist and task statuses from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            print(f"\nChecklist loaded from {filename}")
            return data.get("checklist", []), data.get("completed_tasks", []), data.get("incomplete_tasks", [])
    else:
        print(f"\n{filename} not found. Starting with an empty checklist.")
        return [], [], []

def get_task_status(task):
  """Asks the user for the status of a task."""
  while True:
    status = input(f"Did you {task}? (yes/no): ").strip().lower()
    if status in ["yes", "no"]:
      return status
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

def process_checklist(checklist):
  """Processes the checklist by getting task statuses and categorizing them."""
  completed_tasks = []
  incomplete_tasks = []
  print("\nProcessing checklist for final status:")
  for task in checklist:
    status = get_task_status(task)
    if status == "yes":
      completed_tasks.append(task)
    else:
      incomplete_tasks.append(task)
  return completed_tasks, incomplete_tasks

def display_tasks(checklist, completed_tasks, incomplete_tasks):
  """Displays the checklist and task statuses."""
  print("\n--- Your Checklist ---")
  if not checklist:
      print("Your checklist is empty.")
  else:
      for i, task in enumerate(checklist):
          status = "Completed" if task in completed_tasks else "Incomplete"
          print(f"{i + 1}. {task} ({status})")
  print("----------------------")


def add_task(checklist, completed_tasks, incomplete_tasks, new_task):
  """Adds a new task to the checklist and marks it as incomplete."""
  if new_task and new_task not in checklist:
      checklist.append(new_task)
      incomplete_tasks.append(new_task) # New task is incomplete by default
      print(f"'{new_task}' added to the checklist.")
  elif new_task in checklist:
      print("Task already exists.")
  else:
      print("Task cannot be empty.")


def remove_task(checklist, completed_tasks, incomplete_tasks, task_to_remove):
  """Removes a task from the checklist and its status lists."""
  if task_to_remove in checklist:
      checklist.remove(task_to_remove)
      # Remove from completed or incomplete lists as well
      if task_to_remove in completed_tasks:
          completed_tasks.remove(task_to_remove)
      elif task_to_remove in incomplete_tasks:
          incomplete_tasks.remove(task_to_remove)
      print(f"'{task_to_remove}' removed from the checklist.")
  else:
      print(f"'{task_to_remove}' not found in the checklist.")

def mark_task_status(checklist, completed_tasks, incomplete_tasks):
    """Allows the user to mark tasks as complete or incomplete."""
    if not checklist:
        print("Your checklist is empty. Cannot mark tasks.")
        return completed_tasks, incomplete_tasks

    print("\nMarking tasks:")
    # Re-process all tasks to update status
    completed_tasks, incomplete_tasks = process_checklist(checklist)
    display_tasks(checklist, completed_tasks, incomplete_tasks)
    return completed_tasks, incomplete_tasks


def main():
    """Main function to run the checklist application."""
    checklist, completed, incomplete = load_checklist()

    # If no data loaded, start with a default checklist
    if not checklist:
        checklist = ["wake up", "do assignments", "eat lunch", "go to sleep"]
        incomplete = list(checklist) # Initially all tasks are incomplete

    while True:
        print("\n--- Menu ---")
        print("1. View Checklist")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task Status")
        print("5. Save and Exit")
        print("------------")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            display_tasks(checklist, completed, incomplete)
        elif choice == '2':
            new_task = input("Enter the new task to add: ").strip()
            add_task(checklist, completed, incomplete, new_task)
            save_checklist(checklist, completed, incomplete) # Save after adding
        elif choice == '3':
            task_to_remove = input("Enter the task to remove: ").strip()
            remove_task(checklist, completed, incomplete, task_to_remove)
            save_checklist(checklist, completed, incomplete) # Save after removing
        elif choice == '4':
            completed, incomplete = mark_task_status(checklist, completed, incomplete)
            save_checklist(checklist, completed, incomplete) # Save after marking
        elif choice == '5':
            save_checklist(checklist, completed, incomplete)
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the main application
if __name__ == "__main__":
    main()