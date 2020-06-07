test = map(int, input().strip().split())
print(f"{test}")

#map object cannot be printed, must be list or tuple first
print(list(test))

#print the sum of a map without list?
#nope invalid
print(sum(test))
