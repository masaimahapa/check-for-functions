from program import check_function, list_all_js_function_names

import pytest

def test_check_function():
    line=" function foo():"
    assert check_function(line)=='foo'

def test_check_no_fucntion():
    line= 'haha'
    assert check_function(line)==None

def test_check_funcion_call():
    line= 'foo(5,2)'
    assert check_function(line)== None


def test_get_functions():
    path='cards.js'
    assert list_all_js_function_names(path)== [{'name': 'promptUser', 'start_row': 7, 'end_row': 13}, {'name': 'Array.prototype.memory_card_shuffle', 'start_row': 15, 'end_row': 23}, {'name': 'newBoard', 'start_row': 25, 'end_row': 35}, {'name': 'flip2Back', 'start_row': 64, 'end_row': 80}]
'''
def test_wrong_file_get_functions():
    with pytest.raises(FileNotFoundError) as fnf:
        get_functions('haha')
    assert 'No such file' in (str(fnf.value))
'''
def test_not_python_file():
    with pytest.raises(TypeError) as TE:
        list_all_js_function_names('haha.spy')
    assert 'Not' in (str(TE.value))



