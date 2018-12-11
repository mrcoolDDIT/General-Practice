print("enter number sequence with space between each number")
test = [int(x) for x in input().split()]
print(min(set(test), key = test.count))
print(test)