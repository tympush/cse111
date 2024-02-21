def sumAllPossibleMultiplications(array):
    sum = 0
    for i in range(len(array)):
        for x in range(i+1, len(array)):
            sum += (array[i] * array[x])

    return sum


solutions = 0

with open('input.txt', 'r') as file:
    N, S = map(int, file.readline().split())

for outerLoopIndex in range(N+1):

    sequence = []
    for listAppendLoopIndex in range(N-outerLoopIndex):
        sequence.append(1)
    
    for sequenceVariantsIndex in range(len(sequence)+1):

        sequenceSum = sumAllPossibleMultiplications(sequence)

        if sequenceSum == S:
            solutions += 1
            break

        for i in range(len(sequence)):
            if sequence[i] == 1:
                sequence[i] = -1
                break


with open('output.txt', 'w') as file:
    file.write(str(solutions))

print("done")