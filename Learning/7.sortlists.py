

"""
Python - Sort Lists________________________________________
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
Example
Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

output:
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

"""


Example
Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
output:
[23, 50, 65, 82, 100]


"""
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

"""
Sort Descending
To sort descending, use the keyword argument reverse = True:
Example
Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
output:
['pineapple', 'orange', 'mango', 'kiwi', 'banana']

"""
print("----------Sort Descending---------")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

"""
Example
Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
output:

[100, 82, 65, 50, 23]

"""
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


"""
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?
The reverse() method reverses the current sorting order of the elements.
Example
Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
output: ['cherry', 'Kiwi', 'Orange', 'banana']

"""

print("--------reverse()-------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
