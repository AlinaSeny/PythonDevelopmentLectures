import argparse
import cowsay


parser = argparse.ArgumentParser()

parser.add_argument("message", nargs="+", type=str)
parser.add_argument("-b", const="b", dest='mode', action="append_const", help="Borg mode")
parser.add_argument("-d", const="d", dest='mode', action="append_const", help="appear dead")
parser.add_argument("-g", const="g", dest='mode', action="append_const", help="greedy mode")
parser.add_argument("-p", const="p", dest='mode', action="append_const", help="state of paranoia")
parser.add_argument("-s", const="s", dest='mode', action="append_const", help="appear thoroughly stoned")
parser.add_argument("-t", const="t", dest='mode', action="append_const", help="tired cow")
parser.add_argument("-w", const="w", dest='mode', action="append_const", help="wired mode")
parser.add_argument("-y", const="y", dest='mode', action="append_const", help="youthful appearance")

parser.add_argument("-n", action="store_false")
parser.add_argument("-W", dest="width", action="store", default=40)
parser.add_argument("-e", dest="eye_string", action="store", default="OO", help="eye string")
parser.add_argument("-T", dest="tongue_string", action="store", default="  ", help="tongue string")
parser.add_argument("-f", dest="cow_name", action="store", default="default", type=str, help="name of cow")
parser.add_argument("-l", dest="list_cows", action="store_true", help="list all cows")

args = parser.parse_args()
args.mode = None if args.mode is None else "".join(args.mode)

if args.list_cows:
    print(sorted(cowsay.list_cows()))
else:
    print(cowsay.cowsay(" ".join(args.message), cow=args.cow_name, eyes=args.eye_string,
                                tongue=args.tongue_string, width=args.width, preset=args.mode))
