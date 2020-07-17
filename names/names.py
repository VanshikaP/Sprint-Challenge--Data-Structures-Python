import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

# Sol1 - 1.46s - O(n^2)
# for name_1 in names_1:
    # if name_1 in names_2:
    # duplicates.append(name_1)

# Sol2 - 1.6s - O(n^2)
# duplicates = [name for name in names_1 if name in names_2]


# Sol3 - sort and then binary search - O(nlog(n)) - 0.5s
# Binary Search - log(n)
def myBinarySearch(items, item):
    if len(items) is 1:
        if items[0] is item:
            return True
        else:
            return False
    elif item == items[int(len(items)/2)]:
        return True
    elif item < items[int(len(items)/2)]:
        newItems = items[0:int(len(items)/2)]
        return myBinarySearch(newItems, item)
    else:
        newItems = items[int(len(items)/2):]
        return myBinarySearch(newItems, item)

# Built in Sorting - nlog(n)
names_1.sort() 

# Iterating over array and searching - nlog(n)
for name in names_2:
    if myBinarySearch(names_1, name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
