def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1

    count = 0
    count += tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("move disk", n, "from rod", source, "to rod", destination)
    count += 1
    count += tower_of_hanoi(n - 1, auxiliary, destination, source)

    return count

N = 2
total_moves = tower_of_hanoi(N, 1, 3, 2)
print(total_moves)
