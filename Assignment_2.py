#Task 1: Check if a Number is Even or Odd

a = int(input("enter the number : "))
if (a%2 == 0):
    print(a, "is an even number")
else:
    print(a, "is an odd number")
print("EXIT")

#Task 2: Sum of Integers from 1 to 50 Using a Loop

sum =  0
for i in range(1,51):
    sum = sum + i
print("The sum of numbers from  1 to 50 is:", sum)