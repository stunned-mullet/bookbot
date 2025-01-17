def read_file(filepath):
    with(filepath)as f:
        file_contents = f.read()
    return file_contents

def main():
    book = read_file("books/frankenstein.txt")
    for lines in (book):
        print(line) 

main()
