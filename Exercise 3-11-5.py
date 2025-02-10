def main():
    bottle_verse(5)

# Write a function called bottle_verse that takes a number as a parameter and
# displays the verse that starts with the given number of bottles.
def bottle_verse(bottle_num):
    for i in range(bottle_num, 0 , -1):
        bottle_song(bottle_num)
        bottle_num -= 1

def bottle_song(bottle_num):
    if bottle_num > 2:
        print(f""" 
        {bottle_num} bottles of beer on the wall
        {bottle_num} bottles of beer
        Take one down, pass it around
        {bottle_num-1} bottles of beer on the wall
        """)
    elif bottle_num == 2:
        print(f""" 
        {bottle_num} bottles of beer on the wall
        {bottle_num} bottles of beer
        Take one down, pass it around
        {bottle_num-1} bottle of beer on the wall
        """)
    else:
        print(f""" 
        {bottle_num} bottle of beer on the wall
        {bottle_num} bottle of beer
        Take one down, pass it around
        No more bottles of beer on the wall!
        """)

main()