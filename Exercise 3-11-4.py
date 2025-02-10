def main():
    rectangle("O", 5, 4)

def rectangle(text, width, height):
    for i in range(height):
        print(text * width)

main()