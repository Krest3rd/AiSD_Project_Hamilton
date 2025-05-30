import sys
from decoration import header, footer, line, print_text_multiline

def invalid_usage():
    header("Correct usage: ./plik --hamilton OR ./plik --non-hamilton", pattern="-",length=60)
    sys.exit(1)

def invalid_command():
    header("INVALID COMMAND", pattern="-", length=43)
    print_text_multiline("Please enter a valid command or type 'help' for assistance.", width=43)
    footer("-",length=43)

def invalid_input(n:int):
    line("-")
    print_text_multiline(f"Invalid input. Number of nodes must be greater than {n} and saturation must be an integer between 0 and 100.")
    line('-')

def invalid_eof():
    header("Ctrl+D detected. Exiting.", pattern="-")
    sys.exit(1)
    
def invalid_keyboard_interrupt():
    header("Ctrl+C detected. Exiting.", pattern="-")
    sys.exit(0)