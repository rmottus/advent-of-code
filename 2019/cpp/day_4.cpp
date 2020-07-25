#include <iostream>
#include <string>

using namespace std;

// This solution is very boring compared to the python one, but it's fast
// and much more memory efficient

int main(int argc, char **argv) {
    if (argc < 3) {
        cout << "Please provide min and max value to search between.";
        return -1;
    }

    int min = stoi(argv[1]);
    int max = stoi(argv[2]);

    int part_1_count = 0;
    int part_2_count = 0;

    for (int i = min; i < max; i++) {
        string str_rep = to_string(i);
        int cur_len = 1;
        bool non_dec = true, consec = false, exact_two = false;
        for (int j = 0; j < str_rep.length() - 1; j++) {
            if (str_rep[j] > str_rep[j+1]) {
                non_dec = false;
                break;
            } else if (str_rep[j] == str_rep[j+1]) {
                cur_len++;
            } else {
                if (cur_len == 2) {
                    exact_two = true;
                    consec = true;
                } else if (cur_len > 2) {
                    consec = true;
                }
                cur_len = 1;
            }
        }

        // Cover consecutive digits that end the number
        if (cur_len == 2) {
            exact_two = true;
            consec = true;
        } else if (cur_len > 2) {
            consec = true;
        }

        if (non_dec && consec) {
            part_1_count++;
            cout << i << " true";

            if (exact_two) {
                part_2_count++;

                cout << " true";
            }
            cout << endl;
        }
    }

    cout << "Part 1: " << part_1_count << endl;
    cout << "Part 2: " << part_2_count << endl;
}