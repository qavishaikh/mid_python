# All List Functions

qavi = ["Qavi","Aliza","Hamdan","Neha"]
print(qavi)
qavi.append("Muzammil")
print(qavi)
qavi.insert(2, "Aysha")
print(qavi)
qavi1 = ["Alizna","Ahsan","Fatima"]
qavi.extend(qavi1)
print(qavi)
qavi.remove("Aysha")
print(qavi)
qavi.pop(1)
print(qavi)
x = qavi.index("Alizna")
print(x)
print(qavi)
c = qavi.count("Ahsan")
print(c)
print(qavi)
leng = len(qavi)
print(leng)

for x in qavi:
    print(x)



num = [1,2,3,4,5,6]
num.sort()
print(num)
num.reverse()
print(num)
length = len(num)
print(length)


# list2 = ["a","b","C"]
# print(list2)
# index = 0
# while index < len(list2):
#     if list2[index]=="b":
#         list2[index]="c"
#     index+=1
# print(list2)



# list1 = ["A", "B", "C"]
# print(list1)
# for index, value in enumerate(list1):
#     if value == "B":
#         list1[index] = "F"
# print(list1)

# list3 = ["Q","A","V","I"]
# print(list3)
# list3 = ["R" if item == "Q" else item for item in list3]
# print(list3)

list3 = ["Q", "A", "V", "I"]
print(list3)

# Create an empty list to store the modified values
new_list = []

for item in list3:
    if item == "Q":
        new_list.append("R")
    else:
        new_list.append(item)

list3 = new_list  # Update list3 with the modified values

print(list3)



one = []
one.append(1)
one.append(2)
print(one)
one.pop()
print(one)

two = [1,2,3,4,5,6]
one.extend(two)
print(one)
one.remove(2)
print(one)

v = two.index(3)
two[v] = 9
print(two)

one1 = []

for index in range(5):
    one1.append(index)
print(one1)

names = ["Qavi","Hamdan","Aliza","Neha"]
for index, name in enumerate(names):
    print(f"{index + 1} {name}")