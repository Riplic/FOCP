numbers = [10, 20, 30, 90, 200, 30, 22, 11]  

running_total = 0
for number in numbers:
    if number > 100:
        break    
    running_total += number
    print(running_total)
else:
    print("All numbers processed")