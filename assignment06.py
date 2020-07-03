'''
Create a list with the names of friends and colleagues. Search for the
name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

'''
# creating the colleagues list
colleagues = list()
while True:
    colleague = input("Enter the name of  colleague:")
    colleagues.append(colleague)
    qns = input("Do you want to add more friend? Press Y/N :").upper()
    if qns != 'Y':
        break

# checking john in the list or not
index = False
for i in colleagues:
    if i.lower() == 'john':
        print('John is found')
        index = True
        break
if index == False:
    print("Not found")
