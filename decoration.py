#default length should be preferably divisible by 3
#  'cuz /!\ is 3 characters long and it looks cool
default_length = 42
default_pattern = "="

def line(pattern=default_pattern,length=default_length):
    line = (pattern * length)[:length]
    print(line)

def header(title,pattern=default_pattern,length=default_length):
    print()
    line(pattern,length)
    print(f"{title:^{length}}")
    line(pattern,length)
    print()

def footer(pattern=default_pattern,length=default_length):
    print()
    line(pattern,length)
    
def print_text_multiline(text,width=default_length,path=False):
    if path:
        split_text = " -> ".join(map(str, text))
    else:
        split_text = text
    while len(split_text) > width:
        break_position = split_text.rfind(' ', 0, width)
        if break_position == -1:
            break_position = width 
        print(split_text[:break_position])
        split_text = split_text[break_position:].lstrip()
    if split_text:
        print(split_text)
