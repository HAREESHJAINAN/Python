"""
Access Items
List items are indexed and you can access them by referring to the index number:

Example1
Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  #Note: The first item has index 0.

"""
print("Example1")
thislist = ["apple", "banana", "cherry"]
print(thislist[2])   #Note: The first item has index 0.
print(thislist[1])   #Note: The first item has index 0.


"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example2
Return the third, fourth, and fifth item:

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5])
Note: The search will start at index 2 (included) and end at index 5 (not included).

"""

print("Example2")
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[2:5])  #Note: The search will start at index 2 (included) and end at index 5 (not included). Remember that the first item has index 0.


"""
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

"""
thislist2 = ["apple", "banana", "cherry"]
if "apple" in thislist2:
  print("Yes, 'apple' is in the fruits list available")