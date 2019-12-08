import sys, itertools

def check_adj_matching_digits(num: int):
    digits = [ d for d in str(num) ]
    cur_len = 1
    for i in range (len(digits) - 1):
        if digits[i] == digits[i+1]:
            cur_len += 1
        else:
            if cur_len == 2:
                return True
            cur_len = 1

    return cur_len == 2

def main():
    [min, max] = [int(i) for i in sys.argv[1:3]]

    # Count non-decreasing numbers of length k in base N:
    # if k = 1 there are N
    # if k = 2 there are N * (N+1)/2
    ## N start with 0, N-1 start with 1, ..., 1 start with (N-1)
    # if k = 3 there are N * (N+1)/2 * (N+2)/3
    ## N*(N+1)/2 start with 0, (N-1)*N/2 start with 1, ... 1 start with (N-1)
    ## N*(N+1)/2 + (N-1)*N/2 + ... + 1 = (sum i=0 to N of i) + (sum i=0 to N-1 of i) ... + (sum i=0 to 1 of i)
    ##                                 = N * (N+1) * (N+2) / 6 = N * (N+1)/2 * (N+2)/3
    ## In general, number of length k is N * (N+1)/2 * (N+2)/3 ... * (N+k-1)/k
    
    # Similarilly, we can count the number of increasing numbers of length K in base N:
    # If k = 1, there are N
    # If k = 2, there are (N-1) * N / 2
    ## There are (N-1) that start with 0, N-2 that start with 1, ...
    # Note: We are just subbing N-1 for N in the above equations
    # In general, (N-1) * (N)/2 * (N+1)/3 ... * (N+k-2)/k

    # Any non-decreasing sequence that does not contain consecutive repeated digits must be an increasing sequence
    # So the difference of the two formula above is the total number of non-decreasing sequences of length k in base N
    # that conain at least one pair on consecutive repeated digits

    # Note: We are working with 6 digit numbers, but we do not allow leading 0s, and since they are non-decreasing, this means there will be no 0s
    #       so we are effectively working in base 9
    # Then there are 9 * 10/2 * 11/3 * 12/4 * 13/5 * 14/6 - 8* 9/2 * 10/3 * 11/4 * 12/5 * 13/6 = 1287 total passwords with length 6
    # But, how many are between the inputs?
    # There should be some way to count this without actually generating number, but I'm not going to spend too long thinking about it

    max_exp = len(str(max))
    # Wasting a bit of memory here by having an empty 0th index to make the logic a bit easier to think about
    # since none of the numbers can start with 0 or contain a 0
    non_dec = [
        [
            [] for j in range(10)
        ] for i in range(max_exp)
    ]
    inc = [[[] for j in range(10)] for i in range(max_exp)]

    for i in range(1, 10):
        non_dec[0][i].append(i)
        inc[0][i].append(i)

    for exp in range(1, max_exp):
        for first_digit in range(1, 10):
            to_add = first_digit * (10 ** exp)
            for next_digit in range(first_digit, 10):
                for num in non_dec[exp-1][next_digit]:
                    non_dec[exp][first_digit].append(to_add + num)
                if next_digit > first_digit:
                    for num in inc[exp-1][next_digit]:
                        inc[exp][first_digit].append(to_add + num)

    final_non_dec = list(itertools.chain.from_iterable(non_dec[-1]))
    final_inc = list(itertools.chain.from_iterable(inc[-1]))

    result = [ i for i in final_non_dec if i not in final_inc and i > min and i < max ]
    print(f"Count of non-decreasing numbers with at least one repeated consecutive digit between {min} and {max}: {len(result)}")

    result_part_2 = [ i for i in result if check_adj_matching_digits(i) ]
    print(f"Count of non-decreasing numbers with at least one repeated consecutive digit that's not a part of a larger group of matching digits between {min} and {max}: {len(result_part_2)}")

if __name__ == '__main__':
    main()