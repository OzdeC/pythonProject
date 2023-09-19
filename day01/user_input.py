#print(help(input))

name = input('Enter your name:\n ')
age = int(input('Enter your age:\n'))    #int( input('Enter your age:\n') )
gpa = float(input('Enter your gpa:\n'))
boolean_value = bool(input('Enter True or False:\n'))


print(name)
print(type(name))   #<class 'str'>

print(age)         #print(int(age) +5)  #result is; 35+5=40
print(type(age))

print(gpa)
print(type(gpa))

print(boolean_value)
print(type(boolean_value))