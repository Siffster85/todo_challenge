from lib.todo import *

def test_function_returns():
    assert type(todo_list("#TODO")) == bool

def test_check_value():
    assert todo_list("#TODO") == True

def test_check_value_in_note():
    assert todo_list("#TODO buy milk") == True
    assert todo_list("buy biscuits #TODO") == True
    assert todo_list("have a cup of tea") == False