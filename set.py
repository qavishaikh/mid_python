# All Set Functions

my_set = {1,2,3,4}
print(my_set)
print(type(my_set))

#Add Elements in the Set
my_set = {1,2,3,4}
my_set.add(5)
print(my_set)

#Remove Specific Element
my_set = {1,2,3,4}
my_set.remove(2)
print(my_set)

#Union Returns a new set containing all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

#Method 2for union
seta = {"a", "b" , "c"}
setb = {1, 2, 3}
setc = seta.union(setb)
print(setc)

# Intersection Returns a new set containing elements that are present in both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)

#Method 2 for Intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Length
my_set = {1, 2, 3}
length = len(my_set)
print(length)

# issubset Checks if the set is a subset of another set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1.issubset(set2)
print(is_subset)

# issuperset Checks if the set is a superset of another set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
is_superset = set1.issuperset(set2)
print(is_superset)

#Set in for loop
a_set = {"A","B","C","D"}
for x in a_set:
  print(x)

#add new set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


my_set = {1,2,3}
my_set.add(4)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.update({4,5,6})
print(my_set)
my_set.update({2,9})
print(my_set)