from __future__ import division # for floating point divison

class PrefixEvaluator():
    def __init__(self):
        self._eval_string_op = {
            # Using a dict, we can return a function that can
            # evalute expressions of an arbitrary number of terms
            # with the given operations.
            #
            # example: eval_string_op['*'](2,3,4)
            # returns 24
            '*': lambda *args: reduce(lambda x,y: x*y, args),
            '/': lambda *args: reduce(lambda x,y: x/y, args),
            '+': lambda *args: reduce(lambda x,y: x+y, args),
            '-': lambda *args: reduce(lambda x,y: x-y, args)
        }

    def evaluate(self, prefix_exp):
        """ evaluate a space delimited prefix expression """
        token_list = self._parsed_expression(prefix_exp)
        token_list.reverse() # convert to postfix to easily utilize stack
        operand_stack = []
        for token in token_list:
            if self._is_integer(token):
                operand_stack.append(token)
            else:
                operand_a = operand_stack.pop()
                operand_b = operand_stack.pop()
                result = self._eval_string_op[token](operand_a, operand_b)
                operand_stack.append(result)
        return operand_stack.pop()

    def _is_integer(self, string):
        """
        return bool indicating if string can be
        cast as an integer.
        """
        try:
            int(string)
        except ValueError:
            return False
        return True

    def _parsed_expression(self, prefix_exp):
        """
        prefix_exp: string
        returns a list from string
        casting as int when appropriate
        """
        expression_list = prefix_exp.split()
        return [int(token) if self._is_integer(token) else token for token in expression_list]
