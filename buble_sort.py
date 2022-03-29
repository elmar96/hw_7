unsorted = [5, 15, 3, 7, 8, 20, 12]
c = 0
n = 7

for run in range(n - 1):
    for i in range(n - 1 - run):
        if unsorted[i] > unsorted[i + 1]:
            c += 1
            unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]

print(f'sorted list: {unsorted}')
print(f'number of substitutions: {c}')
