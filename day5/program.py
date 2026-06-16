 
arr=[97,54,85,96,74]
ele=arr[0]
sec=0
arr.sort()
for i in range(len(arr)):
    if arr[i]>ele:
        sec=ele
        ele=arr[i]
    else:
        ele=arr[i]
print(sec)


#write a binary search code
def binary(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1 
print(binary([1, 2, 3, 4, 5], 3))  

#wap to count frequency of each character in a string not count space

# def count_frequency(string):
#     frequency = {}
#     for char in string:
#         if char != " ":  # Ignore spaces
#             if char in frequency:
#                 frequency[char] += 1
#             else:
#                 frequency[char] = 1
#     return frequency

# print(count_frequency("hello  world"))

# a = [10, 20, 4, 45, 99]
# max1 = a[0]
# max2 = 0
# for n in a:
#     if n > max1:
#         max2 = max1  
#         max1 = n     
#     elif n > max2 and n != max1:
#         max2 = n  
# print(max2) 

print(bool([])) 


