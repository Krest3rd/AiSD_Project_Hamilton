#!/usr/bin/env python3
import sys
from menu import run_hamilton_mode, run_non_hamilton_mode, print_usage_and_exit

def main():
    args = sys.argv[1:]
    
    if len(args) != 1 or args[0] not in ("--hamilton", "--non-hamilton"):
        print_usage_and_exit()

    if args[0] == "--hamilton":
        run_hamilton_mode()
    elif args[0] == "--non-hamilton":
        run_non_hamilton_mode()

if __name__ == "__main__":
    main()
