print("""                               Hi Welcome to,
     //////////     ///////              |//////      ///////
        ///       ///    ///             |||  ///   ///    ///
       ///        ///   ///              |||  ///   ///   /// 
      ///         //////                 |//////    //////
                           Application""")

isEnd = False
while(not isEnd):
    user_input=input("""➕Add task(a/add)
📋View tasks(v/view)
🗑️Delete task(d/delete)
🛑Quit application(q/quit)
Please enter your input here: """)
    if(user_input == "q" or "quit"):
        isEnd = True