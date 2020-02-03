import sys
from collections import  defaultdict

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

    visible_astroids = defaultdict(lambda: defaultdict(lambda: 0))
    for row in range(len(rows_with_astroids)):
        j = rows_with_astroids[row]
        cols_with_astroids = astroid_locations[j]

        for col in range(len(cols_with_astroids)):
            i = cols_with_astroids[col]
            # There is an astroid at i, j

            # Find next astroid to the right in the same row
            if col + 1 < len(cols_with_astroids):
                visible_astroids[j][i] += 1
                visible_astroids[j][cols_with_astroids[col + 1]] += 1

            vis_from_cur = []
            for check_j in rows_with_astroids[row+1:]:
                for check_i in astroid_locations[check_j]:
                    if check_i == i:
                        # Would be a vertical line
                        if not any([ vis_i == i for [vis_i, vis_j] in vis_from_cur ]):
                            visible_astroids[j][i] += 1
                            visible_astroids[check_j][check_i] += 1
                            vis_from_cur.append([check_i, check_j])
                        continue

                    # Line from [i,j] to [check_i, check_j] is y = m * x + b
                    # where m = (check_j - j) / (check_i - i)
                    # and b = j - m * i
                    m = (check_j - j) / (check_i - i)
                    b = j - m * i
                    if not any([ vis_j == round(m * vis_i + b, 6) for [vis_i, vis_j] in vis_from_cur ]):
                        visible_astroids[j][i] += 1
                        visible_astroids[check_j][check_i] += 1
                        vis_from_cur.append([check_i, check_j])

    best_location = []
    best_location_astroids = -1
    for j in visible_astroids.keys():
        for i in visible_astroids[j]:
            visible_from_here = visible_astroids[j][i]
            # print([i,j], visible_from_here)
            if visible_from_here > best_location_astroids:
                best_location = [i, j]
                best_location_astroids = visible_from_here

    print(f"Best location is {best_location} with {best_location_astroids}")



            
            


if __name__ == '__main__':
    main()