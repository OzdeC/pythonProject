if False:
  print('Python Programming')

print('Java Programming')

print('----------------------')

score = 70

if score >= 60 :
  print('Congrats! you passed teh exam')


s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H and W')

print('-----------------')

if score >= 60:
    print('passed')
else:
    print('Failed')

print('-------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'

print(result)

#Ternary:

#age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'

print(result)

print('-------------')

# Multi- Branch Statements

num = 100

if num >= 0:
    result = 'Positive'    # pass line is a place holder for statements
elif num <= 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)


print('-------------')

num = 200
result2 = 'Positive' if num >= 0 else 'Negative'

print(result2)

print('---------------------------------')

score = -300

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

print('---------------------------------')

score = 95
if 0 <= score <= 100:

    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid Score')











