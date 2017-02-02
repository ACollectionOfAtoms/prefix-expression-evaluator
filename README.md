pip2 install -r requirements.txt
python2 app.py -f test/test_file.txt

"""
Assumptions:
    - We assume we will always be given a valid
    prefix expression: "You are given a prefix expression".

    - Assume only a small subset of possible operators will be used:
    '* / +'
"""

.h3 The problem
INPUT SAMPLE:

1
* + 2 3 4

Your program has to read this and insert it into any data structure you like.
Traverse that data structure and evaluate the prefix expression.
Each token is delimited by a whitespace.
You may assume that the only valid operators appearing in test data are
 '+','*' and '/'(floating-point division).
Please include unit tests that demonstrate how your code works.

Please zip the contents of your solution named: `prefix-[lastname].zip`

OUTPUT SAMPLE:

Print to stdout, the output of the prefix expression, one per line. E.g.

1
20

Constraints:
The evaluation result will always be an integer >= 0.
The number of the test cases is <= 40.
