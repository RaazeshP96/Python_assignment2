'''
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.

'''

people = list()
# inserting tuples in list
while True:
    fname = input("enter the first name:")
    lname = input("enter the last name:")
    age = int(input("enter age:") or '0')
    tuple1 = (fname, lname, age)
    people.append(tuple1)
    qns = input("Do you want to add more people? Press Y/N :").upper()
    if qns != 'Y':
        break

print(people)
print('-'*20)

# list of people with age
peopleWithAge = [i for i in people if i[2] != 0]
s = 0
for i in peopleWithAge:
    s = s+i[2]
aver = s//len(peopleWithAge)


# replacing no-age with average age
newPeople=list()
for i in people:
    newTup = (i[0], i[1], aver) if i[2] == 0 else i
    newPeople.append(newTup)
print(newPeople)
