#Kyle Kekawa, Bryan Mai
#Creating a class that creates a rectangle

from rectangle import Rectangle
from check_input import get_int_range

def display_grid(grid):
    for row in grid:
        print(" ".join(row))

def reset_grid(grid):
    for i in range(20):
        for j in range(20):
            grid[i][j] = '.'

def place_rect(grid, rect):
    x, y = rect.get_coords()
    width, height = rect.get_dimensions()

    for i in range(y, y + height):
        for j in range(x, x + width):
            grid[i][j] = "*"

def main():
    grid = [['.' for _ in range(20)] for _ in range(20)]

    print("Enter rectangle width (1-5):")
    width = get_int_range("Width: ", 1, 5)

    print("Enter rectangle height (1-5):")
    height = get_int_range("Height: ", 1, 5)

    rect = Rectangle(width, height)

    while True:
        reset_grid(grid)
        place_rect(grid, rect)
        display_grid(grid)

        print("Enter Direction:")
        print("1. Up\n2. Down\n3. Left\n4. Right\n5. Quit")
        user_choice = get_int_range("Choice: ", 1, 5)

        if user_choice == 1:
            rect.move_up()
        elif user_choice == 2:
            rect.move_down()
        elif user_choice == 3:
            rect.move_left()
        elif user_choice == 4:
            rect.move_right()
        elif user_choice == 5:
            break

if __name__ == "__main__":
    main()
