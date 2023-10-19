#All dictionary Functions
my_dic = {
    "name":"Qavi",
    "age":19,
    "City":"Hyd"
}
print(my_dic)

#Add Item in dictionary
my_dic["Mobile Number"] = 3133825456

#Update Item value 
my_dic["age"] = 20
print(my_dic)

#remove item
my_dic.pop("age")
print(my_dic)

#Access
a = my_dic["name"]
print(a)

#Dictionary in For Loop
#items
for item in my_dic.items():
    print(item)
#keys
for keys in my_dic.keys():
    print(keys)
#values
for value in my_dic.values():
    print(value)


# Create a nested dictionary
my_dict = {
    'person1': {
        'name': 'Qavi',
        'age': 19,
        'city': 'Hyd'
    },
    'person2': {
        'name': 'Abdullah',
        'age': 15,
        'city': 'Chori Para'
    },
    'person3': {
        'name': 'Abdul Rehman',
        'age': 16,
        'city': 'Gaoshala'
    }
}

# Access values using loops
for person_key, person_info in my_dict.items():
    print(f"Person: {person_key}")
    for key, value in person_info.items():
        print(f"{key}: {value}")
    print()

for person_key in my_dict.items():
    print(f"Person: {person_key}")

print()

for person_key, person_info in my_dict.items():
    print(f"Person: {person_key} and {person_info}")


main_qavi = {
    "Student1":{
        "Roll No":"BSIT_2022_080",
        "Student Name":"M.Qavi",
        "Department":"IT"
    },
    "Student2":{
        "Roll No":"BSIT_2022_084",
        "Student Name":"Abdullah",
        "Department":"IT"
    },
    "Student3":{
        "Roll No":"BSIT_2022_086",
        "Student Name":"Abdul Rehman",
        "Department":"IT"
    },
    "Student4":{
        "Roll No":"BSIT_2022_077",
        "Student Name":"Fahad KK",
        "Department":"CS"
    }
}

for studentName, studentdata in main_qavi.items():
    print(f"Student: {studentName}")
    for key, value in studentdata.items():
        print(f"{key} {value}")
    print()

for studentName in main_qavi.keys():
    print(f"Student: {studentName}")

for studentName, studentdata in main_qavi.items():
    print(f"Student: {studentName} and {studentdata}")


A = {
    "Player1":"Baber Azam",
    "Player2":"M.Rizwan",
    "Player3":"Sheheen Afridi",
    "Player4":"Sarfraz",
    "Player5":"M.Amir",
    "Player6":"Naseem Shah",
    "Player7":"Hasnain"
}
print(A)
A["Player3"] = "Shahid Afridi"
print(A)
A.pop("Player3")
print(A)
A["Player3"] = "Shoaib Malik"
print(A)

for item in A.items():
    print(item)

for key in A.keys():
    print(key)

for value in A.values():
    print(value)
