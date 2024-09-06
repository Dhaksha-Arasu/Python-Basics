def linear_search(lst, target):
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1
lst = list(map(str, input().split()))
target = str(input())
result = linear_search(lst, target)
print(result)