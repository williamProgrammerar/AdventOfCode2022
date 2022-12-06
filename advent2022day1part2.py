maxCalories = 0
list = []

def compareCalories(current, max):    
    if current > max:
        return current
    else: 
        return max

with open('calorieList.txt') as calorieList:
    s = calorieList.read()
    s = s.splitlines()
    
    totalCurrent = 0
    
    for i in s:
        if i.isdigit():
            totalCurrent += int(i)  
        else: 
            list.append(totalCurrent)
            totalCurrent = 0

    list.append(totalCurrent)    

list.sort(reverse = True)

if len(list) >= 3:
    print(list[0] + list[1] + list[2])