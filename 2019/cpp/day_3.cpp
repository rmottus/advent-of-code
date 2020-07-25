#include <vector>
#include <utility>
#include <iostream>
#include <sstream>
#include <climits>

using namespace std;

typedef pair<int, int> intpair;

// This is using a much better algorithm that I did used in python
// Instead of creating an array tracking each point each wire covers, then looping over these for both wires to find cross points, 
// we just track the endpoints of each movement of each wire, then calculate intersection points between them


vector<string> tokenize(const string &str) {
    vector<string> tokens;
    stringstream splitter(str);
    string token;

    while(getline(splitter, token, ',')) {
        tokens.push_back(token);
    }
    return tokens;
}

vector<intpair> create_wire_points(const vector<string> &path) {
    vector<intpair> wire = { {0, 0} };
    int x = 0, y = 0;

    for (auto s: path) {
        char dir = s[0];
        int dist = stoi((char *)&s[1]);

        switch(dir) {
            case 'U':
                y += dist;
                wire.push_back({ x, y });
                break;
            case 'D':
                y -= dist;
                wire.push_back({ x, y });
                break;
            case 'L':
                x -= dist;
                wire.push_back({ x, y });
                break;
            case 'R':
                x += dist;
                wire.push_back({ x, y });
                break;
            default:
                throw "Unkown direction";
        }
    }

    return wire;
}

bool is_between(const int &i, const int &j, const int &k) {
    if (i <= j) {
        return i <= k && k <= j;
    }
    return j <= k && k <= i;
}

vector<intpair> find_cp(const vector<intpair> &first_wire, const vector<intpair> &second_wire) {
    vector<intpair> result;

    int a_dist = 0;
    for (int i = 0; i < first_wire.size() - 1; i++) {
        intpair a_first_point = first_wire[i],
                a_second_point = first_wire[i+1];
        int a_x_1 = a_first_point.first,
            a_y_1 = a_first_point.second;
        int a_x_2 = a_second_point.first,
            a_y_2 = a_second_point.second;
        bool a_vert = a_x_1 == a_x_2;

        int b_dist = 0;
        for (int j = 0; j < second_wire.size() - 1; j++) {
            intpair b_first_point = second_wire[j], 
                    b_second_point = second_wire[j+1];
            int b_x_1 = b_first_point.first,
                b_y_1 = b_first_point.second;
            int b_x_2 = b_second_point.first,
                b_y_2 = b_second_point.second;
            bool b_vert = b_x_1 == b_x_2;

            if (a_vert != b_vert) {
                if (a_vert) {
                    // intpair cp = { a_x_1, b_y_1 };
                    if (is_between(b_x_1, b_x_2, a_x_1) && is_between(a_y_1, a_y_2, b_y_1)) {
                        result.push_back({
                            abs(a_x_1) + abs(b_y_1),
                            a_dist + abs(a_y_1 - b_y_1) + b_dist + abs(b_x_1 - a_x_1)
                        });
                    }
                } else {
                    // intpair cp = { b_x_1, a_y_1 };
                    if (is_between(a_x_1, a_x_2, b_x_1) && is_between(b_y_1, b_y_2, a_y_1)) {
                        result.push_back({
                            abs(b_x_1) + abs(a_y_1),
                            a_dist + abs(a_x_1 - b_x_1) + b_dist + abs(b_y_1 - a_y_1)
                        });
                    }
                }
            }

            b_dist += (b_vert ? abs(b_y_1 - b_y_2) : abs(b_x_1 - b_x_2));
        }
        a_dist += (a_vert ? abs(a_y_1 - a_y_2) : abs(a_x_1 - a_x_2));
    }
    
    return result;
}

int main() {
    string first_line, second_line;
    getline(cin, first_line);
    getline(cin, second_line);

    auto first_path = tokenize(first_line);
    auto second_path = tokenize(second_line);

    auto first_wire = create_wire_points(first_path);
    auto second_wire = create_wire_points(second_path);
    std::cout << first_wire.size() << " " << second_wire.size() << endl;

    auto crosspoints = find_cp(first_wire, second_wire);

    int man_min = INT_MAX;
    int len_min = INT_MAX;
    for (auto cp: crosspoints) {
        int man_dist = cp.first;
        if (man_dist < man_min) {
            man_min = man_dist; 
        }

        int len_dist = cp.second;
        if (len_dist < len_min) {
            len_min = len_dist; 
        }
    }

    std::cout << "The nearest cross intpair by Manhatten distance is this far away: " << man_min << endl;
    std::cout << "The nearest cross intpair by wire length is this far away: " << len_min << endl;
}