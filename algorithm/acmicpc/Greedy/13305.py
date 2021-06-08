n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

now_price = price[0]
result = now_price * distance[0]

for i in range(1, n-1):
    if now_price > price[i]:
        now_price = price[i]
    result += now_price * distance[i]

print(result)
