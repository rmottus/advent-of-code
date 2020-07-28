#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <stack>

using namespace std;

bool get_path(
    const map<string, vector<string>> &graph,
    const string &start,
    const string &target,
    vector<string> &path
) {
    path.push_back(start);

    if (start == target) {
        return true;
    }

    for (auto v: graph.at(start)) {
        if (get_path(graph, v, target, path)) {
            return true;
        }
    }

    path.pop_back();
    return false;
}

int main() {
    map<string, vector<string>> orbits;

    string line;
    while (getline(cin, line)) {
        size_t mid_marker = line.find(')');
        if (mid_marker == string::npos) {
            cerr << "Malformed input line - missing )" << endl;
            return -1; 
        }
        string left = line.substr(0, mid_marker);
        string right = line.substr(mid_marker + 1);

        if (orbits.count(left) == 0) {
            orbits[left] = { right };
        } else {
            orbits[left].push_back(right);
        }
    }

    vector<string> current_level, next_level;
    current_level.push_back("COM");
    int depth = 0;
    int total_orbits = 0;

    while(!current_level.empty()) {
        for (auto planet: current_level) {
            total_orbits += depth;
            for (auto child: orbits[planet]) {
                next_level.push_back(child);
            }
        }
        depth++;
        current_level.swap(next_level);
        next_level.clear();
    }

    cout << "Total orbits: " << total_orbits << endl;

    vector<string> path_to_you;
    get_path(orbits, "COM", "YOU", path_to_you);

    vector<string> path_to_santa;
    get_path(orbits, "COM", "SAN", path_to_santa);

    int min_path = min(path_to_you.size(), path_to_santa.size());

    int i = 0;
    for (; i < min_path; i++) {
        if (path_to_you[i] != path_to_santa[i]) {
            break;
        }
    }

    // Total path length - shared parts - 2 to exclude endpoints
    cout << "Total hops from you to santa is: " << path_to_you.size() + path_to_santa.size() - 2*i - 2 << endl;
}