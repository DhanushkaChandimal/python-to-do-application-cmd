# 📝 Terminal To-Do List Application (Python)

A colorful, interactive terminal-based **To-Do List** application written in Python.\
It allows you to **add**, **view**, and **delete** tasks with a fun and user-friendly CLI interface.

---

## ✨ Features

- ➕ **Add Tasks** — Create new tasks and store them in a list.
- 📋 **View Tasks** — Display your task list in a formatted table.
- 🗑️ **Delete Tasks** — Remove tasks by number or by description.
- 🛑 **Quit Application** — Exit with a custom ASCII farewell message.
- 🎨 **Colorful Output** — Uses ANSI escape codes for better readability.

---

## 📂 Project Structure

```
to_do_list.py   # Main Python script
README.md       # Documentation
```

---

## 🔧 Requirements

- Python **3.7+**
- Runs directly in the terminal (no external libraries required)

---

## 🚀 How to Run

1. **Clone this repository** or download the file:

```bash
git clone https://github.com/DhanushkaChandimal/python-to-do-application-cmd.git
```

2. **Run the script**:

```bash
app.py
```

---

## 📖 Usage Instructions

When the application starts, you’ll see a welcome banner and a menu:

```
➕ Add task (a / add)
📋 View task_list (v / view)
🗑️  Delete task (d / delete)
🛑 Quit application (q / quit)
```

### **1️⃣ Add a Task**

- Type `a` or `add`
- Enter the task description (must be at least 1 character, no duplicates allowed)

### **2️⃣ View Tasks**

- Type `v` or `view`
- Displays a numbered list of all tasks

### **3️⃣ Delete a Task**

- Type `d` or `delete`
- Enter the task **number** or **name** to delete
- If your input matches both a number and a task name, you’ll be asked to clarify

### **4️⃣ Quit the App**

- Type `q` or `quit` to exit
- A farewell ASCII message is displayed

---

## 🖼️ Example Run

```plaintext
➕ Add task (a / add)
📋 View task_list (v / view)
🗑️  Delete task (d / delete)
🛑 Quit application (q / quit)

Please enter your input here: a

Enter your task 1: Buy milk
Task Buy milk added successfully

Please enter your input here: v
Task No.   Task Description
1           Buy milk

Please enter your input here: d
Enter task number or task name to remove: 1
Task number 1 is removed successfully
```

---

## 💡 Notes

- The application stores tasks only for the current session — once you quit, the list resets.
