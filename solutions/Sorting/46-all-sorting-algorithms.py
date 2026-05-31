# Welcome to WorkPad
# Start coding here...

# Bubble Sort Algo

def bubblesort(arr,compare):
  n = len(arr)
  for i in range(n):
    isswapped = False
    for j in range(n - i - 1):
      if compare(arr[j],arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
        isswapped = True
    if not isswapped:
      break
  return arr

print(f"Ascending Bubble Sort : {bubblesort([6,2,4,3,5,1],lambda a,b : a>b)}")
print(f"Decending Bubble Sort : {bubblesort([6,2,4,3,5,1],lambda a,b : a<b)}")


# Selection Sort Algo

def selectionsort(arr,compare):
  n = len(arr)
  for i in range(n):
    min_index = i
    for j in range(i+1 , n):
      if compare(arr[j],arr[min_index]):
        min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
  return arr

print(f"Asceding Selection Sort : {selectionsort([6,2,4,3,5,1], lambda a,b : a<b)}")
print(f"Des Selection Sort : {selectionsort([6,2,4,3,5,1], lambda a,b : a>b)}")  


# Insertion Sort Algo 
def insertionsort(arr,compare):
  n = len(arr)
  for i in range(1,n):
    temp = arr[i]
    j = i -1
    while j >=0 and compare(temp,arr[j]):
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = temp
  return arr

print(f"Asceding Selection Sort : {insertionsort([6,2,4,3,5,1], lambda a,b : a<b)}")
print(f"Des Selection Sort : {insertionsort([6,2,4,3,5,1], lambda a,b : a>b)}") 



# Merge Sort Algo
def merge(left,right):
  i = 0
  j = 0
  result = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
    
  while i < len(left):
    result.append(left[i])
    i += 1
  while j < len(right):
    result.append(right[j])
    j += 1
  
  return result

def mergesort(arr):
  if len(arr)<=1:
    return arr

  mid = len(arr)//2

  left = mergesort(arr[:mid])
  right = mergesort(arr[mid:])

  return merge(left,right)

print(f"Merge Sort: {mergesort([6,2,4,3,5,1])}")


#Quick Sort Algo 

def partition(arr,low,high):
  pivot = arr[high]
  i = low - 1
  for j in range(low,high):
    if arr[j] < pivot:
      i += 1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

def quicksort(arr,low,high):
  if low < high:
    pivot_index = partition(arr,low,high)
    quicksort(arr,low,pivot_index-1)
    quicksort(arr,pivot_index+1,high)


def answer(arr):
  quicksort(arr,0, len(arr) - 1)
  return arr

print(f"Quick Sort : {answer([6,2,4,3,5,1])}")





