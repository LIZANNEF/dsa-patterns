from itertools import accumulate
#using accumulate
a = [10, 24, 26, 49, 57]
c = accumulate(a) #returns <itertools.accumulate object at 0x0000029390BE8240>
b = list(accumulate(a)) #returns a list [10, 34, 60, 109, 166]
print(b)
print(c)

#to find sum of sub array between index i, j

print("Enter index i, j")
i = int(input())
j = int(input())
sum = (b[j]-b[i-1] if i > 0 else b[j])
print("Sum is: "+str(sum))

# eg i=0, j=2, returns 60

#Without built-in accumulate function
def create_prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr
# It converts a normal array into its prefix sum array, in place (i.e., directly modifies the same array).

# Iteration	    i	    Operation	                    arr after operation
# start	        –	    initial	                        [10, 24, 26, 49, 57]
# 1	            1	    arr[1] += arr[0] → 24 + 10	    [10, 34, 26, 49, 57]
# 2	            2	    arr[2] += arr[1] → 26 + 34	    [10, 34, 60, 49, 57]
# 3	            3	    arr[3] += arr[2] → 49 + 60	    [10, 34, 60, 109, 57]
# 4	            4	    arr[4] += arr[3] → 57 + 109	    [10, 34, 60, 109, 166]
a = [10, 24, 26, 49, 57]
b= create_prefix_sum(a)
i=0
j=2
sum = (b[j]-b[i-1] if i > 0 else b[j])
print(sum)
