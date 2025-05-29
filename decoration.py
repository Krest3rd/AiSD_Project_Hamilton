def line(pattern="",length=42):
    line = (pattern * length)[:length]
    print(line)

def header(title,pattern="=",length=42):
    print()
    line(pattern,length)
    print(f"{title:^{length}}")
    line(pattern,length)
    print()

def footer(pattern="="):
    print()
    line(pattern)
    
def print_text_multiline(text,width=42,path=False):
    if path:
        split_text = " -> ".join(map(str, text))
    else:
        split_text = text
    while split_text:
        print(split_text[:width])
        split_text = split_text[width:]
