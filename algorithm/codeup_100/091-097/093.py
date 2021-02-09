n = int(input())
data = list(map(int, input().split()))

# print(min(data))
smallest = data[0]
for i in data:
    if i < smallest:
        smallest = i
print(smallest)
