def checkStraightLine(coordinates):
    num_points = len(coordinates)
    if num_points <= 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    initial_slope = (y2 - y1) / (x2 - x1)

    for i in range(2, num_points):
        x, y = coordinates[i]
        current_slope = (y - y1) / (x - x1)
        if current_slope != initial_slope:
            return False

    return True

# Example usage
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))  # Output: True
