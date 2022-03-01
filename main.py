text = "advanced programming"

print(text[1:10])
print(text[5:])
print(text[:10])
print(text[:])

print(text[:-1])
print(text[-5:-1])
print("advanced Programming"[-10:])

print("Advanced" + "Programming")
print("ha"*5)


print(len(text))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
text = "adanced Programming        "
print(text)
print(text.rstrip())
print(text.count('m'))

print(text.find('d'))
print(text.rfind('d'))

town = input("Enter the town you live in: ")
print(town.capitalize())

fullName = input("Enter full name: ")
n = fullName.find(" ")
# name = "Ali Hassan"
print(n)
print("First Name: "+fullName[:n])
print("Last Name: "+fullName[n+1:])

print("Advanced\tProgramming".expandtabs(20))
print("Advanced\nProgramming")

print("Advanced\"Programming")

print("Advanced", "Programming","Python",sep="-----")

print(text.upper().rfind('G'))

print(float("27"))
num = 27
c_num = str(num)
print(type(c_num))




print("ID".center(3), "Std Name".ljust(30), "CGPA".rjust(5))
print("1".center(3), "Ali Hassan".ljust(30), "90".rjust(5))
print("2".center(3), "Wala'a Ali".ljust(30), "80.5".rjust(5))
print("3".center(3), "Alaa Hani".ljust(30), "70.9".rjust(5))


print("{0:3s}{1:30s}{2:5s}".format("ID","Std Name", "CGPA"))
print("{0:3n}{1:30s}{2:5n}".format(1,"Ali Hassan", 90))
print("{0:3n}{1:30s}{2:5n}".format(2,"Alaa Hadi", 90.5))
print("{0:3n}{1:30s}{2:5n}".format(3,"Hosna Adil", 78.39))
