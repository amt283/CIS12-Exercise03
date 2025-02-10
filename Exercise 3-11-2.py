def main():
    print_right("Testing")
    print_right("One, two, three")
    print_right("Testing!!!")

def print_right(text):
    spaces = 40 - len(text)
    if spaces > 0:
        print(" " * spaces + text)
    else:
        print(text)

main()