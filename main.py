#!/usr/bin/env python3
import sys
from menu import generate_graph_mode, print_usage_and_exit

def main():
    args = sys.argv[1:]
    
    if len(args) != 1 or args[0] not in ("--hamilton", "--non-hamilton"):
        print_usage_and_exit()

    if args[0] == "--hamilton":
        generate_graph_mode(expect_saturation=True)
    elif args[0] == "--non-hamilton":
        generate_graph_mode(expect_saturation=False)

if __name__ == "__main__":
    main()
