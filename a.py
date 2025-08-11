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
            if(len(user_input) < 3):
                print("                    Error: Minimum characters should be 3!")
                continue
            else:
                add_task(user_input)
                break
    elif(user_input == "v" or user_input == "view"):
        print(view_tasks())
    else:
        print("\n                    Invalid input! Please enter input from above list.")