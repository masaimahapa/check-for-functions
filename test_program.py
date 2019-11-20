from program import check_function, get_functions

import pytest

def test_check_function():
    line="def get_money():"
    assert check_function(line)=='get_money'

def test_check_no_fucntion():
    line= 'haha'
    assert check_function(line)==None

def test_check_funcion_call():
    line= 'add(5,2)'
    assert check_function(line)== None

def test_check_no_colon_syntax_error():
    line= 'def my_function(argument)'
    assert check_function(line)== None


def test_get_functions():
    path='calculator.py'
    assert get_functions(path)== [{'name': 'add', 'start_row': 1, 'end_row': 7}, {'name': 'multiply', 'start_row': 9, 'end_row': 18}, {'name': 'themba', 'start_row': 20, 'end_row': 23}, {'name': 'another_one', 'start_row': 25, 'end_row': 27}]
'''
def test_wrong_file_get_functions():
    with pytest.raises(FileNotFoundError) as fnf:
        get_functions('haha')
    assert 'No such file' in (str(fnf.value))
'''
def test_not_python_file():
    with pytest.raises(TypeError) as TE:
        get_functions('haha.spy')
    assert 'Not' in (str(TE.value))



