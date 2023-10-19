#All Tupple Fucntions
tupple = ("Qavi","Hamdan")
print(tupple)
print(type(tupple))


#Access Tupple Element
thistuple = ("apple", "banana", "cherry","Mango")
print(thistuple[0])
print(thistuple[-1])

#Substring
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:5])
print(thistuple[2:])
if "apple" in thistuple:
  print("Yes, apple is in the fruits tuple")
else:
    print("No, apple is not in this tupple")

#Updatre the Tupple
x = ("Qavi", "Fareed", "Abdullah")
y = list(x)
y[1] = "Saad"
x = tuple(y)
print(x)

#Add Item from List Conversion
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

#Add Item in typple by adding two tupples
thistuple = ("apple", "banana", "cherry")
y = ("Grapes",)
a = thistuple + y
print(a)

#Remove Element from List Conversion
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

#Delete Complete Tupple
thistuple1 = ("apple", "banana", "cherry")
del thistuple1

#Loop in Tupple
ab = ("ABC", "BC", "AC")
for x in ab:
  print(x)

#Count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#Index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

#Updatre the Tupple
x = ("Qavi", "Fareed", "Abdullah")
print(x)
y = list(x)
y[1] = "Saad"
x = tuple(y)
print(x)

