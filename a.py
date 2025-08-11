task_list = []

print("""                               Hi Welcome to,
     //////////     ///////              |//////      ///////
        ///       ///    ///             |||  ///   ///    ///
       ///        ///   ///              |||  ///   ///   /// 
      ///         //////                 |//////    //////
                           Application""")

def add_task(task):
    task_list.append(task)

isEnd = False
while(not isEnd):
    user_input=input("""\n➕ Add task (a / add)
📋 View task_list (v / view)
🗑️  Delete task (d / delete)
🛑 Quit application (q / quit)

Please enter your input here: """).lower()
    if(user_input == "q" or user_input == "quit"):
        isEnd = True
        print("---------------------")
        print(user_input)
        print(user_input=="q")
        print(user_input == "q" or "quit")
    elif(user_input == "a" or "add"):
        while(True):
            user_input=input(f"\nEnter your task {len(task_list)+1}: ")
            if(len(user_input) < 3):
                print("Error: Minimum characters should be 3!")
                continue
            else:
                add_task(user_input)
                break