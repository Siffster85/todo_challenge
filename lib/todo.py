#As a user

#So that I can find my tasks among all my notes

#I want to check if a line from my notes includes the string `#TODO`.

def todo_list(string):

    if not isinstance(string, str):
        raise TypeError("Please input a valid note")

    if string == "" or string == " ":
        return "Please input a valid note"

    return "#TODO" in string