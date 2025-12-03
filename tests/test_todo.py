from lib.todo import *
import pytest

def test_function_returns():
    assert type(todo_list("#TODO")) == bool

def test_check_value():
    assert todo_list("#TODO") == True

def test_check_value_in_note():
    assert todo_list("#TODO buy milk") == True
    assert todo_list("buy biscuits #TODO") == True
    assert todo_list("have a cup of tea") == False

def test_empty_string():
    assert todo_list("") == "Please input a valid note"
    assert todo_list(" ") == "Please input a valid note"

def test_type_error():
    with pytest.raises(TypeError) as e:
        todo_list(13)
    error_message = str(e.value)
    assert error_message == "Please input a valid note"