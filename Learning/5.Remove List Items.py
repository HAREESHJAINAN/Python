"""
Python - Remove List Items
Remove Specified Item
The remove() method removes the specified item.

ExampleGet your own Python Server
Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print(len(thislist))



"""
If there are more than one item with the specified value, the remove() method removes the first occurrence:

Example
Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

"""
print("-----------------remove()")
thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)


"""

Remove Specified Index
The pop() method removes the specified index.

Example
Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

Note: If you do not specify the index, the pop() method removes the last item.
"""
print("--------------pop(1)----------")#If you do not specify the index, the pop() method removes the last item.
thislist2 = ["apple", "banana", "cherry"]
thislist2.pop(1)
print(thislist2)


"""
Example
Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""

print("---------pop()-------")#If you do not specify the index, the pop() method removes the last item.
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop()
print(thislist3)




"""

The del keyword also removes the specified index:

Example
Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""

thislist4 = ["apple", "banana", "cherry"]
del thislist4[0]
print(thislist4)


"""
he del keyword can also delete the list completely.

Example
Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

"""

del_list = ["apple", "banana", "cherry"]
del del_list
print('deleted')



"""

Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

Example
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""

thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)
print("=====================clear()")