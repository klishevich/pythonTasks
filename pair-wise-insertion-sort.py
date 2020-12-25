# Python program for implementation of Insertion Sort 

def sortFrom(arr, position, key):
    j = position-1
    while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
    arr[j + 1] = key
    return j+1
  
# Function to do insertion sort 
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    arrayLength = len(arr)
    startIndex = 0 if (arrayLength % 2 == 0) else 1
    for i in range(startIndex, arrayLength, 2):
        indexMin = i;
        keyMin = arr[i];
        indexMax = i+1;
        keyMax = arr[i+1];
        if arr[i] > arr[i+1]:
            indexMin = i+1;
            keyMin = arr[i+1];
            indexMax = i;
            keyMax = arr[i];
        print ("indexMax % d" % indexMax);
        print ("keyMax % d" % keyMax);
        arr.pop(indexMin);
        position = sortFrom(arr, i, keyMax);
        print ("% d" % position);
        arr.insert(position, keyMin);
        position = sortFrom(arr, position, keyMin);
        print ("% d" % position);
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6, 1, 3]
print ("Test 1 start") 
insertionSort(arr) 
print ("Test 1 result") 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 

# Driver code to test above
arr2 = [3,4,2,1] 
print ("Test 2 start") 
insertionSort(arr2) 
print ("Test 2 result") 
for i in range(len(arr2)): 
    print ("% d" % arr2[i]) 
