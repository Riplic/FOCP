def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

print(calcAve(5)) 
print(calcAve(5, 10)) 
print(calcAve(5, 10, 15)) 
print(calcAve(5, 10, 15, 20))
