#include <iostream>
#include <vector>
#include <string>
#include <climits>

using namespace std;

const int zero_ascii = 48;

struct Layer {
    vector<int> data;

    void print(const int &w) {
        for (int i = 0; i < data.size(); i++) {
            if (i > 0 && i % w == 0) {
                cout << endl;
            }

            cout << (data[i] == 1 ? "■" : " ");
        }
        cout << endl;
    }
};

int main(int argc, char **argv) {

    int width = stoi(argv[1]);
    int height = stoi(argv[2]);
    int layer_size = width * height;

    string all_data;
    getline(cin, all_data);
    int num_layers = all_data.size() / layer_size;

    vector<Layer> layers(num_layers);
    int min_zeros = INT_MAX;
    int total = 0;
    for(int i = 0; i < num_layers; i++) {
        Layer &cur = layers[i];
        int zeros = 0, ones = 0, twos = 0;

        for (int j = 0; j < layer_size; j++) {
            int d = (int) all_data[i * layer_size + j] - zero_ascii;
            cur.data.push_back(d);
            switch(d) {
                case 0:
                    zeros++;
                    break;
                case 1:
                    ones++;
                    break;
                case 2:
                    twos++;
                    break;
            }
        }

        if (zeros < min_zeros) {
            min_zeros = zeros;
            total = ones * twos;
        }
    }

    cout << "The total number of 1s x 2s on the layer with minium number of zeros is " << total << endl;


    Layer final_output;
    for (int i = 0; i < layer_size; i++) {
        int colour = 2;
        for (auto &v: layers) {
            if (v.data[i] != 2) {
                colour = v.data[i];
                break;
            }
        }
        final_output.data.push_back(colour);
    }
    
    final_output.print(width);
}