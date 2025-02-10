def main():
    rectangle("O", 5, 4)

# Write a function called rectangle that takes a string and two integers and
# draws a rectangle with the given width and height, made up using copies of the
# string.
def rectangle(text, width, height):
    for i in range(height):
        print(text * width)

main()