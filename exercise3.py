# save indexes of all "0" in a list
def get_index_list(grid):
    index_list = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "0":
                index_list.append((i, j))
    return index_list


# return the final grid after n seconds
def bomber_man(n, grid):
    # length of row
    row = len(grid)

    # length of column
    column = len(grid[0])

    # for every even number of seconds, the grid will be full of bombs
    if n % 2 == 0:
        return [['0' for _ in range(column)] for _ in range(row)]

    # for every n % 4 == 3 number of seconds, the grid will be full of bombs
    # except the ones that were blown up after initial placement
    elif n % 4 == 3:
        new_grid = [['0' for _ in range(column)] for _ in range(row)]
        for i, j in get_index_list(grid):
            new_grid[i][j] = '.'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < row and 0 <= y < column:
                    new_grid[x][y] = '.'
        return new_grid

    # for every n % 4 == 1 number of seconds, the bombs will be placed at initial positions
    return grid


def main():
    # insert here number of seconds and the grid positioning of bombs
    N = 3
    GRID = [".......", "...0...", "....0..", ".......", "00.....", "00....."]

    final_grid = bomber_man(N, GRID)
    for row in final_grid:
        print("".join(row))


if __name__ == "__main__":
    main()
