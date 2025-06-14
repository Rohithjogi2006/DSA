def linear_search (arr , target):
    for i in range (len (arr)):
        if arr[i]==target:
            return i
    return -1

arr=[5,2,3,4,1,9,6,8,7]
target=int(input("enter a number :"))

res= linear_search(arr,target)
if res!=-1:
    print("element found")
else:
    print("element not found")