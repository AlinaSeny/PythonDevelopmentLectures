import argparse
from cowsay import cowsay, Option, list_cows


parser = argparse.ArgumentParser()

parser.add_argument("-b", action="append_const", help="Borg mode")
parser.add_argument("-d", action="append_const", help="appear dead")
parser.add_argument("-g", action="append_const", help="greedy mode")
parser.add_argument("-p", action="append_const", help="state of paranoia")
parser.add_argument("-s", action="append_const", help="appear thoroughly stoned")
parser.add_argument("-t", action="append_const", help="tired cow")
parser.add_argument("-w", action="append_const", help="wired mode")
parser.add_argument("-y", action="append_const", help="youthful appearance")

parser.add_argument("-n", action="store_false", help="do not wrap text, if specified any positional arguments are prohibited")
parser.add_argument("-W", dest="width", action="store", default=40, help="specifies where the message should be wrapped")
parser.add_argument("-e", dest="eye_string", action="store", default="OO", help="custom eye string")
parser.add_argument("-T", dect="tongue_string", action="store", default="  ", help="custom tongue string")
parser.add_argument("-f", dect="cow", action="store", default="default", type=str, help="name of the cow")
parser.add_argument("-l", dest="list_cows", action="store_true", help="list all cows")
