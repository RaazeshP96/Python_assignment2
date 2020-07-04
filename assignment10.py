'''

 Write a function that takes camel-cased strings (i.e. ThisIsCamelCased),
 and converts them to snake case (i.e. this_is_camel_cased). 
 Modify the function by adding an argument, separator, 
 so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

'''


def camToSnak(str1, seprator):
    resStr = str1[0].lower()
    for i in str1[1:]:
        resStr = resStr+seprator+i.lower() if i.isupper() else resStr+i
    return resStr


str1 = input("Enter the camel cased string: ")
seprator = input("Enter the seprator: ")
print(camToSnak(str1, seprator))
