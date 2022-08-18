# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn



    #  Task1ex6



"""         


three_mul = 'fizz'
five_mul = 'buzz'
num1 = 3
num2 = 5 
max_num = 100

   
for i in range(1,max_num):
    # % or modulo division gives you the remainder 
    
    if i%num1 == 0:
        print(i, three_mul)

    elif i%num2 == 0:
        print(i, five_mul)

    if i%num1 == 0 and i%num2 == 0:
        print(i, three_mul + five_mul)


"""



    #  Task2ex6



"""


n = 5
number = 1
sum = 0


while number < n + 1:
    sum = sum + number
    number = number + 1


print("Sum =", sum)


"""



    # Task3ex6



"""


n = 5
sum = 0


for num in range(n + 1):
    sum += num


print("Sum =", sum)


"""



    #  Task4ex6



"""


    #  Task_1_T4

    

for x in range(3):
    print(x)



    #  Task_2_T4




for j in range(5):
    print("This is loop number", j)    



    #  Task_3_T4



xy = 10


while xy > 0:
    print(xy)
    xy -= 1

print()

    #Task_4_T4

countdown = 5


while countdown != 0:
    print(f"{countdown}")
    countdown -= 1

else:
    print("Start!")  


"""


    #  Task5ex6



"""


x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))


if x == y or y == z or z == x:
    result = 0

else:
    sum = x + y + z
    result = sum


print("Calculated sum is ", result)


"""



#Task6ex6



"""


x = int(input("First number: "))
y = int(input("Second number: "))

result = x + y

if result >= 15 and result <= 20:
    result = 20


print("Calculated sum is ", result)


"""



#Task7ex6



"""


a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " ,b =", b)

temp = b
a = b
a = temp

print("After swapping: a =", a, " ,b =", b)


"""



#Task8ex6



"""


x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))

print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))


"""



#Task9ex6



"""


x = input("Type your value: ")

if x == "0":
    x = False

elif x == "1":
    x = True

else:
  pass

print("Your entered value is now ", x)


"""



#Task10ex6



"""


x = int(input("First number: "))
y = int(input("Second number: "))


if x % y == 0:
    print("First number is divisible by second number, result =", x / y)

elif y % y == 0:
    print("Second number is divisible by first number, result =", y / x)

else:
    print("Numbers are non-divisable!")


"""