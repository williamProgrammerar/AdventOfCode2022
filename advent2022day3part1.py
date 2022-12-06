lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sum = 0

def split_first_half(arr, end):
    list = []
    for i in range(0, end):
            list.append(arr[i])
    return list

def split_second_half(arr, start, end):
    list = []
    for i in range(start, end):
            list.append(arr[i])
    return list

def calc(dup):
    dup = dup.pop()
    if dup in lowercase:
        return lowercase.index(dup) + 1
    else: 
        return uppercase.index(dup) + 27

with open('day3test.txt') as knapsack:
    k = knapsack.read()
    k = k.splitlines()

    first_compartment = []
    second_compartment = []

    for i in k:
        mid = int(len(i)/2)

        first_compartment = split_first_half(i, mid)
        second_compartment = split_second_half(i, mid, len(i))

        duplicate = set(first_compartment).intersection(second_compartment)

        sum += calc(duplicate)

print(sum)