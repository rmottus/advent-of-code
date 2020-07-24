import sys

def main():
    layer_width = 25
    layer_height = 6
    layer_total = layer_width * layer_height
    with open(sys.argv[1], 'r') as input_file:
        all_input = input_file.readline()
    
    as_nums = [ int(i) for i in all_input ]
    as_layers = [ as_nums[i:i+layer_total] for i in range(0, len(as_nums), layer_total) ]

    min_zeros = layer_total
    layer_with_max_zeros = []

    for layer in as_layers:
        num_zeros = layer.count(0)
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            layer_with_max_zeros = layer

    print(f"The layer with min zeros has #1s x #2s: {layer_with_max_zeros.count(1) * layer_with_max_zeros.count(2)}")

    final_image = []
    for i in range(0, layer_total):
        col = [ layer[i] for layer in as_layers ]
        color = 2
        for pixel in col:
            if pixel != 2:
                color = pixel
                break
        final_image.append('■' if color == 1 else ' ')

    for i in range(0, layer_total, layer_width):
        print(*final_image[i:i+layer_width], sep='')


if __name__ == '__main__':
    main()