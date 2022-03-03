def step(x, y, direction):
    if direction == 0:
        x += 1
    elif direction == 1:
        y += 1
    elif direction == 2:
        x -= 1
    elif direction == 3:
        y -= 1
    return x, y


def print_spiral(size: int):
    table = [[0 for _ in range(size)] for _ in range(size)]
    number = 1
    x, y = 0, 0
    steps = size - 1
    while number < size ** 2:
        for direction in range(4):
            for st in range(steps):
                table[y][x] = number
                if direction == 3 and st == steps - 1:
                    direction = 0
                x, y = step(x, y, direction)
                number += 1
        steps -= 2
        if steps == 0 and size % 2:
            table[y][x] = number
    # Print the table
    for row in table:
        for num in row:
            print(num, end='\t')
        print()
    print()


if __name__ == '__main__':
    print_spiral(3)
    print_spiral(5)
    print_spiral(8)
    print_spiral(21)
