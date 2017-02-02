from __future__ import division # for floating point divison
from libs.evaluators import PrefixEvaluator

def test_evaluation():
    peval = PrefixEvaluator()
    test_string = '* + 2 3 4'
    assert peval.evaluate(test_string) == 20

def test_is_integer():
    peval = PrefixEvaluator()
    string_int_list = [str(i) for i in range(0,11)] # ['0', '1',...,'10']
    for string in string_int_list:
        assert peval._is_integer(string)

def test_string_multiplication():
    peval = PrefixEvaluator()
    assert peval._eval_string_op['*'](2,3) == 2 * 3

def test_string_division():
    peval = PrefixEvaluator()
    assert peval._eval_string_op['/'](4,5) == 4 / 5

def test_string_addition():
    peval = PrefixEvaluator()
    assert peval._eval_string_op['+'](6,7) == 6 + 7

def test_string_subtraction():
    peval = PrefixEvaluator()
    assert peval._eval_string_op['-'](9,8) == 9 - 8

def test_expression_parser():
    peval = PrefixEvaluator()
    pre_parsed = '* + 2 3 4'
    properly_parsed = ['*', '+', 2, 3, 4]
    assert peval._parsed_expression(pre_parsed) == properly_parsed
