def main():
    print_right("Testing")
    print_right("One, two, three")
    print_right("Testing!!!")

# Write a function named print_right that takes a string named text as a
# parameter and prints the string with enough leading spaces that the last letter
# of the string is in the 40th column of the display.
def print_right(text):
    spaces = 40 - len(text)
    if spaces > 0:
        print(" " * spaces + text)
    else:
        print(text)

main()