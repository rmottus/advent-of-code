import sys

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

if __name__ == '__main__':
    main()