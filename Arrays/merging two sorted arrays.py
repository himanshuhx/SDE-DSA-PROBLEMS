# two arrays are given already sorted
# [2,4,5,9] n=4
# [1,3,7] m=3

#approach1 create extra array of size(n+m)
# copy content of both than sort the new array
#  copy again to original arrays
# 0(n+m) for copying to new array +0(nlogn) for sorting +  0(n) for copying to 1st array + 0(m) for copying to 2 arr

# approach 2
# insertion sort


# approach 3
# gap algo
# gap =(n+m)/2 keep dividing by 2 until gap!=0
# maintain two pointers start and end and diff == gap
# keep traversing if ele found st start>end swap