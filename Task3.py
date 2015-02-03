# Jamie Hilton
# 12/12/2014
# Task 2

result = 0
index = 0
values = [0, 24, 13, 57, 45]
while index < 4:
    index = index+1
    if result < values[index]:
        result = values[index]
print(result)
