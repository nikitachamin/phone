# var1 = '5 4'
# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
# var2 = var2.split()
# var3 = var3.split()
#
# var2 = set(var2)
# var3 = set(var3)
#
# set = sorted(var2.intersection(var3))
# for i in set:
#     print(i, end = " ")

arr = [5, 8, 6, 4, 9, 2, 7, 3]
temp = 0
for i in range(-1,len(arr)-1):
    print(arr[i])
    if arr[i] + arr[i-1] + arr[i+1] > temp:
        temp = arr[i] + arr[i-1] + arr[i+1]
print(temp)