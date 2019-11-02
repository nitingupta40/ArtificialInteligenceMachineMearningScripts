class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    target =9
    num ={2,7,9,11}
    print("hey")

    map = {}
    print("hey")
    print(map)
    print("yes")
    for i in range(len(num)):
       if num[i] not in map:
           map[target - num[i]] = i + 1
           print(map[target - num[i]])
       else:
           print("don")