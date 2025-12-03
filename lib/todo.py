#As a user

#So that I can find my tasks among all my notes

#I want to check if a line from my notes includes the string `#TODO`.

def todo_list(string):
    if "#TODO" in string:
        return True
    else:
        return False