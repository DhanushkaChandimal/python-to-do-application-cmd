task_list = []
RESET = '\033[0m'

print(f"""{'\033[106m'}                               Hi Welcome to,                .{RESET}

     //////////     ///////              |//////      ///////
        ///       ///    ///             |||  ///   ///    ///
       ///        ///   ///              |||  ///   ///   /// 
      ///         //////                 |//////    //////
      
{'\033[105m'}                           Application                       .{RESET}""")

def quitApp():
    print(f"""
|||||||||||   |||    |||       ///\\\\\\       |||\\\    |||   ||| ///
    |||       |||    |||      ///  \\\\\\      ||| \\\   |||   |||///
    |||       ||||||||||     /////\\\\\\\\\\     |||  \\\  |||   |||\\\\\\ 
    |||       |||    |||    ///      \\\\\\    |||   \\\ |||   ||| \\\\\\ 
    |||       |||    |||   ///        \\\\\\   |||    \\\|||   |||  \\\\\\     {'\033[104m'}You!{RESET}
""")

def add_task():
    while(True):
        user_input=input(f"\nEnter your task {len(task_list)+1}: ")
        if(len(user_input) < 1):
            print(f"                    {'\033[91m'}Error: There shold be at least one character!{RESET}")
            continue
        else:
            task_list.append(user_input)
            print(f"                    {'\033[92m'}Task {'\033[1m'}{user_input}{'\033[22m'} added sucessfully{RESET}")
            break

def view_tasks():
    if(len(task_list)<=0):
        print(f"\n                    {'\033[93m'}To do list is empty!{RESET}")
    else:
        print(f"                    {'\033[1m'}{'\033[4m'}Task No.   Task Description{RESET}")
        for index in range(len(task_list)):
            print(f"                    {index+1}           {task_list[index]}")

def delete_task():
    if(len(task_list) <= 0):
        return f"\n                    {'\033[93m'}There is nothing to remove. To do list is empty!{RESET}"
    while(True):
        user_input=input("\nEnter task number or task name to remove: ")
        try:
            user_input = int(user_input)
            if(user_input > len(task_list) and not str(user_input) in task_list):
                print(f"\n                    {'\033[93m'}There is nothing found in the list!{RESET}")
                view_tasks()
            elif(user_input <= len(task_list) and str(user_input) in task_list):
                while(True):
                    user_value_or_number = input("""\nThere is a value and number equal to your input. Plese verify what you want to delete.
t - for task, n - for task number: """).lower()
                    if(user_value_or_number == "t"):
                        task_list.remove(str(user_input))
                        return f"\n                    {'\033[92m'}{'\033[1m'}{user_input}{'\033[22m'} is removed successfully{RESET}"
                    elif(user_value_or_number == "n"):
                        del task_list[user_input - 1]
                        return f"\n                    {'\033[92m'}Task number {'\033[1m'}{user_input}{'\033[22m'} is removed successfully{RESET}"
                    else:
                        print(f"\n                    {'\033[91m'}Invalid input!{RESET}")
            elif(user_input <= len(task_list)):
                del task_list[user_input - 1]
                return f"\n                    {'\033[92m'}Task number {'\033[1m'}{user_input}{'\033[22m'} is removed successfully{RESET}"
            elif(user_input <= len(task_list) and str(user_input) in task_list):
                task_list.remove(str(user_input))
                return f"\n                    {'\033[92m'}{'\033[1m'}{user_input}{'\033[22m'} is removed successfully{RESET}"
            else:
                print(f"\n                    {'\033[91m'}There is nothing found in the list!{RESET}")
                view_tasks()
                
        except ValueError:
            if(user_input in task_list):
                task_list.remove(user_input)
                return f"\n                    {'\033[92m'}{'\033[1m'}{user_input}{'\033[22m'} is removed successfully{RESET}"
            else:
                print(f"\n                    {'\033[91m'}There is nothing found in the list!{RESET}")
                view_tasks()

isEnd = False
while(not isEnd):
    user_input=input(f"""\n➕ Add task (a / add)
📋 View task_list (v / view)
🗑️  Delete task (d / delete)
🛑 Quit application (q / quit)

Please enter your input here: """).lower()
    if(user_input == "q" or user_input == "quit"):
        isEnd = True
        quitApp()
    elif(user_input == "a" or user_input == "add"):
        add_task()
    elif(user_input == "v" or user_input == "view"):
        view_tasks()
    elif(user_input == "d" or user_input == "delete"):
        print(delete_task())
    else:
        print(f"\n                    {'\033[91m'}Invalid input! Please enter input from the {'\033[1m'}{'\033[4m'}list.{RESET}")
