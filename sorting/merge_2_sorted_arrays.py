from collections import deque

left = deque([1, 5, 7, 9, 44, 66])
right = deque([2, 4, 8, 44])
res = []

while left and right:
    if left[0] < right[0]:
        res.append(left.popleft())
    else:
        res.append(right.popleft())

res.extend(left if left else right)

print(res)

# ----------------------------------------

left = [1, 5, 7, 9, 44,  66]
right = [2, 4, 8, 44]
i, j = 0, 0
res = []

while i < len(left) and j < len(right):
    if left[i] < right[j]:
        res.append(left[i])
        i += 1
    else:
        res.append(right[j])
        j += 1

res.extend(left[i:] if j == len(right) else right[j:])

print(res)