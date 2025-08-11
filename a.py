task_list = []

print("""                               Hi Welcome to,
     //////////     ///////              |//////      ///////
        ///       ///    ///             |||  ///   ///    ///
       ///        ///   ///              |||  ///   ///   /// 
      ///         //////                 |//////    //////
                           Application""")

def add_task(task):
    task_list.append(task)

def view_tasks():
    if(len(task_list)<=0):
        return "\n                    To do list is empty!"
    else:
        task_table = ""
        for index in range(len(task_list)):
            task_table += f"\n                    {index+1} - {task_list[index]}"
        return task_table

def delete_task():
    if(len(task_list) <= 0):
        return "\n                    There is nothing to remove. To do list is empty!"
    while(True):
        user_input=input("\nEnter task number or task name to remove: ")
        try:
            user_input = int(user_input)
            if(user_input > len(task_list) and not str(user_input) in task_list):
                print("\n                    Invalid input!")
            elif(user_input <= len(task_list) and str(user_input) in task_list):
                while(True):
                    user_value_or_number = input("""\nThere is a value and number equal to your input. Plese verify what you want to delete.
t - for task, n - for task number: """).lower()
                    if(user_value_or_number == "t"):
                        task_list.remove(str(user_input))
                        return f"\n                    {user_input} is removed successfully"
                    elif(user_value_or_number == "n"):
                        del task_list[user_input - 1]
                        return f"\n                    Task number {user_input} is removed successfully"
                    else:
                        print("\n                    Invalid input!")
            elif(user_input <= len(task_list)):
                del task_list[user_input - 1]
                return f"\n                    Task number {user_input} is removed successfully"
            elif(user_input <= len(task_list) and str(user_input) in task_list):
                task_list.remove(str(user_input))
                return f"\n                    {user_input} is removed successfully"
            else:
                print("\n                    Invalid input!")
                
        except ValueError:
            if(user_input in task_list):
                task_list.remove(user_input)
                return f"\n                    {user_input} is removed successfully"
            else:
                print("\n                    Invalid input!")

isEnd = False
while(not isEnd):
    user_input=input("""\n➕ Add task (a / add)
📋 View task_list (v / view)
🗑️  Delete task (d / delete)
🛑 Quit application (q / quit)

Please enter your input here: """).lower()
    if(user_input == "q" or user_input == "quit"):
        isEnd = True
    elif(user_input == "a" or user_input == "add"):
        while(True):
            user_input=input(f"\nEnter your task {len(task_list)+1}: ")
            if(len(user_input) < 1):
                print("                    Error: There shold be at least one character!")
                continue
            else:
                add_task(user_input)
                break
    elif(user_input == "v" or user_input == "view"):
        print(view_tasks())
    elif(user_input == "d" or user_input == "delete"):
        print(delete_task())
    else:
        print("\n                    Invalid input! Please enter input from the list.")