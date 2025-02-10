def main():
    triangle('L', 7)

# Write a function called triangle that takes a string and an integer and draws a
# pyramid with the given height, made up using copies of the string.
def triangle(text, height):
    for i in range(height + 1): # height + 1 because i starts at 0, height will be one short otherwise
        print(text * i)

main()