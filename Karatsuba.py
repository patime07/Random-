def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Calculate the size of the numbers.
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the digit sequences in the middle.
    high1, low1 = x // 10**m, x % 10**m
    high2, low2 = y // 10**m, y % 10**m
    
    # Perform the three recursive steps.
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    # Combine the results.
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Example binary numbers
binary_x = '11'  # Binary for 43
binary_y = '11'  # Binary for 75

# Convert to decimal
x_decimal = binary_to_decimal(binary_x)
y_decimal = binary_to_decimal(binary_y)

# Perform multiplication using Karatsuba's algorithm
result_decimal = karatsuba(x_decimal, y_decimal)

# Convert result back to binary
result_binary = decimal_to_binary(result_decimal)
#output
print(result_decimal, result_binary)
