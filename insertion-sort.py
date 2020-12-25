# Python program for implementation of Insertion Sort 

def sortFrom(arr, position):
    key = arr[position]
    j = position-1
    while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
    arr[j + 1] = key
  
# Function to do insertion sort 
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)):
        sortFrom(arr, i);
  
  
# Driver code to test above 
print ("Test 1") 
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 

# Driver code to test above
print ("Test 2") 
arr2 = [4,3,2,1] 
insertionSort(arr2) 
for i in range(len(arr2)): 
    print ("% d" % arr2[i]) 
