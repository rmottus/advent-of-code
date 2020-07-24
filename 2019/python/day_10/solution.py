import sys
from collections import  defaultdict
from math import atan2, pi

def main():
    astroid_locations = defaultdict(lambda: [])
    with open(sys.argv[1], 'r') as f:
        i = 0
        j = 0
        for line in f:
            for char in line:
                if char == '#':
                    astroid_locations[j].append(i)
                i += 1
            j += 1
            i = 0

    # print(astroid_locations)
    rows_with_astroids = list(astroid_locations.keys())

    visible_astroids = defaultdict(lambda: defaultdict(lambda: []))
    for row in range(len(rows_with_astroids)):
        j = rows_with_astroids[row]
        cols_with_astroids = astroid_locations[j]

        for col in range(len(cols_with_astroids)):
            i = cols_with_astroids[col]
            # There is an astroid at i, j

            # Find next astroid to the right in the same row
            if col + 1 < len(cols_with_astroids):
                visible_astroids[j][i].append([cols_with_astroids[col + 1], j])
                visible_astroids[j][cols_with_astroids[col + 1]].append([i, j])

            vis_from_cur = []
            for check_j in rows_with_astroids[row+1:]:
                for check_i in astroid_locations[check_j]:
                    if check_i == i:
                        # Would be a vertical line
                        if not any([ vis_i == i for [vis_i, vis_j] in vis_from_cur ]):
                            visible_astroids[j][i].append([check_i, check_j])
                            visible_astroids[check_j][check_i].append([i, j])
                            vis_from_cur.append([check_i, check_j])
                        continue

                    # Line from [i,j] to [check_i, check_j] is y = m * x + b
                    # where m = (check_j - j) / (check_i - i)
                    # and b = j - m * i
                    m = (check_j - j) / (check_i - i)
                    b = j - m * i
                    if not any([ vis_j == round(m * vis_i + b, 6) for [vis_i, vis_j] in vis_from_cur ]):
                        visible_astroids[j][i].append([check_i, check_j])
                        visible_astroids[check_j][check_i].append([i, j])
                        vis_from_cur.append([check_i, check_j])

    best_location = []
    best_location_astroids = -1
    visible_from_best = []
    for j in visible_astroids.keys():
        for i in visible_astroids[j]:
            visible_from_here = len(visible_astroids[j][i])
            # print([i,j], visible_from_here)
            if visible_from_here > best_location_astroids:
                best_location = [i, j]
                best_location_astroids = visible_from_here
                visible_from_best = visible_astroids[j][i]

    print(f"Best location is {best_location} with {best_location_astroids}")

    for location in visible_from_best:
        # Y values are flipped in this example (increasing Y goes down the graph)
        angle_to_loc = atan2( best_location[1] - location[1], location[0] - best_location[0])
        # Rotate axes 90 degress so that the laser starts firing upwards
        angle_to_loc = angle_to_loc - pi/2
        # Normalize to [0, 2*pi]
        angle_to_loc = angle_to_loc if angle_to_loc > 0 else angle_to_loc + 2 * pi
        location.append(angle_to_loc)

    # Lazer moves anticlockwise, so reverse sort
    sorted_astroids = sorted(visible_from_best, key=lambda loc: -loc[2])
    print(f"200th astroid destroyed is at {sorted_astroids[199]}")



            
            


if __name__ == '__main__':
    main()