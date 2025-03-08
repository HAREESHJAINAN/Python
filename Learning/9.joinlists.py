"""
Python - Join Lists
Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.
One of the easiest ways are by using the + operator.
Example 
Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
"""
print("-----Example1-----")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

"""
Another way to join two lists is by appending all the items from list2 into list1, one by one:
Example
Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

"""
print("---example2----append()---------")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


""""


Or you can use the extend() method, where the purpose is to add elements from one list to another list:
Example
Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


"""
print("---example3----extend()-------")
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



"""
Python - List Methods
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list


"""