#making a function
def reverseList(A, start, end): 
    if start >= end: 
        return
    A[start], A[end] = A[end], A[start] 
    reverseList(A, start+1, end-1) 
A = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12] 

print(A) 
reverseList(A, 0, 11) 
print("Reversed list is") 
#Printing the output
print(A)
