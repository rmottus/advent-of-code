import sys
from collections import deque, defaultdict
from typing import List

def get_path(cur_node: str, tar_node: str, tree: defaultdict, path: List[str]):
    path.append(cur_node)

    if cur_node == tar_node:
        return True

    for item in tree[cur_node]:
        if get_path(item, tar_node, tree, path):
            return True

    # Target not a child of this node, so remove from the path
    path.pop()
    return False

def main():
    tree = defaultdict(list)
    with open(sys.argv[1], 'r') as inp:
        for line in inp.readlines():
            [parent, child] = line.strip().split(")")
            tree[parent].append(child)

    
    depth = 1
    total_orbits = 0
    cur_level = tree.get('COM')
    queue = deque()

    while len(cur_level) > 0:
        for item in cur_level:
            total_orbits += depth
            for planet in tree.get(item, []):
                queue.append(planet)

        depth += 1
        cur_level = list(queue) if len(queue) > 0 else []
        queue.clear()

    print(f"Total orbits is: {total_orbits}")

    path_to_me = []
    get_path('COM', 'YOU', tree, path_to_me)

    path_to_santa = []
    get_path('COM', 'SAN', tree, path_to_santa)

    i = 0
    j = 0
    while True:
        if path_to_me[i] == path_to_santa[j]:
            i += 1
            j += 1
        else:
            break
    
    path = path_to_me[i - 1:]
    path.reverse()
    path += path_to_santa[j:]

    # Minus 2 because we want to exclude the endpoints, minus 1 because we are counting hops between planets
    print(path)
    print(f"Number of orbital transfer to get to Santa is {len(path) - 3}")

if __name__ == '__main__':
    main()