def dec_to_binary(n):
    # Base case
    if n == 0:
        return "0"
    
    # Recursive case
    if n > 1:
        return dec_to_binary(n // 2) + str(n % 2)
    else:
        return str(n)

# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Process each test case
    for _ in range(test_cases):
        n = int(input())
        bin_num = dec_to_binary(n)
        # Ensure the binary number is 8 bits by prepending zeros as needed
        print(bin_num.zfill(8))
