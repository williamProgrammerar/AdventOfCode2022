lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sum = 0

def calc(badge):
    badge = badge.pop()
    if badge in lowercase:
        return lowercase.index(badge) + 1
    else: 
        return uppercase.index(badge) + 27

with open('day3test.txt') as knapsack:
    k = knapsack.read()
    k = k.splitlines()

    members = []
    groups = []

    for i in k:
        if len(members) < 3:
            members.append(i)
        else: 
            groups.append(members)
            members = []
            members.append(i)
        
    if len(members) > 0:
        groups.append(members)
        
    for i in groups:
        duplicate = set(i[0]).intersection(i[1]).intersection(i[2])
        sum += calc(duplicate)

print(sum)