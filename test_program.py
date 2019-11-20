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
    assert get_functions(path)== ['add', 'multiply']

def test_wrong_file_get_functions():
    with pytest.raises(FileNotFoundError) as fnf:
        get_functions('haha')
    assert 'No such file' in (str(fnf.value))



