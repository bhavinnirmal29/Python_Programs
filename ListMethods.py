#def add(a,b):
 #    res=a+b
  #   return res


     
'''
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
'''
# animal list
animal = ['cat', 'dog', 'rabbit']

# another list of wild animals
wild_animal = ['tiger', 'fox']

# adding wild_animal list to animal list
animal.append(wild_animal)
#Updated List
print('Updated animal list: ', animal)
'''# animal list
animal = ['cat', 'dog', 'rabbit']

# an element is added
animal.append('guinea pig')

#Updated Animal List
print('Updated animal list: ', animal)
'''
# vowel list
vowel = ['a', 'e', 'i', 'u']

# inserting element to list at 4th position
vowel.insert(3, 'o')

print('Updated List: ', vowel)

# animal list
animal = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' element is removed
animal.remove('rabbit')

#Updated Animal List
print('Updated animal list: ', animal)

vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is:', count)
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )
