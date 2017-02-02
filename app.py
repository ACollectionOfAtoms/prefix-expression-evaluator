from libs.evaluators import PrefixEvaluator
from argparse import ArgumentParser
import os.path

parser = ArgumentParser(description='Process text files with prefix expressions per newline')
parser.add_argument('-f', dest='filename', required=False, metavar="FILE")

filename = parser.parse_args().filename
pre_eval = PrefixEvaluator()

with open(filename, 'r') as f:
    for line in f:
        print pre_eval.evaluate(line)
