#n = int(input())
#arr = map(int, input().split())

n = 5
arr = [2, 3, 6, 6, 5]

arr = sorted(arr, reverse=True)
scores = []
[scores.append(i) for i in arr if i not in scores]
print(scores[1])