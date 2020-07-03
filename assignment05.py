'''
    Create a tuple with your first name, last name, and age. Create a list,
    people, and append your tuple to it. Make more tuples with the
    corresponding information from your friends and append them to the
    list. Sort the list. When you learn about sort method, you can use the
    key parameter to sort by any field in the tuple, first name, last name,
    or age.

'''
myInfo = ("rajesh", "prajapati", 22)
people = [myInfo]
while True:
    fname = input("enter the first name:")
    lname = input("enter the last name:")
    age = int(input("enter age:"))
    tuple1 = (fname, lname, age)
    people.append(tuple1)
    qns = input("Do you want to add more people? Press Y/N :").upper()
    if qns != 'Y':
        break

print("Before sorting:")
print(people)
print('===============================')
people.sort(key=lambda x: x[2])  # sorting by age
print("after sorting:")
print(people)
