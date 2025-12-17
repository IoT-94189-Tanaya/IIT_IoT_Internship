def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
a=[1,2,3,4]
b=[4,5,6,7]
print (overlapping(a,b))