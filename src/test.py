def recursion_count(n:int, total=0):
    if(n>0):
        return recursion_count(n-1, total+n)
    return total


print(recursion_count(3))