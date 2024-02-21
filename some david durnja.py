def calculate_ways(N, S):
    count = 0
    for i in range(3**N):
        x = []
        for j in range(N):
            x.append((i // (3**j)) % 3 - 1)

        sum_of_products = 0
        zero_count = 0

        for i in range(N):
            for j in range(i+1, N):
                sum_of_products += x[i] * x[j]
            if x[i] == 0:
                zero_count += 1

        if sum_of_products == S and zero_count == (N - zero_count):
            count += 1

    return count


# Read input from file
with open('input.txt', 'r') as file:
    N, S = map(int, file.readline().split())

# Calculate the number of ways
num_ways = calculate_ways(N, S)

# Write output to file
with open('output.txt', 'w') as file:
    file.write(str(num_ways))