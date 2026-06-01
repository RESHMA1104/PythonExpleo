def message(name, msg):
    print("Hello", name+" " + msg)
message(name="John", msg="Have a good day") #2 Keyword Arguments
message(msg="Have a good day", name = "John") # 2 Keyword Arguments(Positional order change)
message("John", msg="Have a good day") # 1 Positional, 1 Keyword Arguments