# # TODO:1. Write a python script to calculate sum of first N natural numbers
# n=int(input('Enter the number:'))
# i=1
# sum = 0
# while i<=n:
#   sum = sum+i
#   i=i+1
# print(sum)
# print()

# #2. Write a python script to calculate sum of squares of first N natural numbers
# n = int(input('Enter the number:'))
# i=1
# sum = 0 
# while i<=n:
#   sum = sum+(i**2)
#   i=i+1
# print(sum)
# print()

# #3. Write a python script to calculate sum of cubes of first N natural numbers
# n = int(input('Enter the number:'))
# i=1
# sum = 0 
# while i<=n:
#   sum = sum+(i**3)
#   i=i+1
# print(sum)
# print()

# #4. Write a python script to calculate sum of first N odd natural numbers
# n = int(input('Enter the value of n:'))*2
# i=0
# sum = 0 
# while i <=n:
#   if i % 2 !=0:
#     sum = sum+i
#   i=i+1
# print(sum)
# print()

# #6. Write a python script to calculate sum of first N even natural numbers
# n = int(input('Enter the value of n:'))*2
# i=0
# sum = 0 
# while i <=n:
#   if i % 2==0:
#     sum = sum+i
#   i=i+1
# print(sum)
# print()

# #7 Write a python script to calculate factorial of a given number
# i=1
# result = 1
# num = int(input('Enter the number you want to find factorial:'))
# while num>=i:
#   result = (num%10)*result
#   num=num-i
# print('the result is:',result)
# print()



# TODO: INeuron Solution
# n = int(input('Enter the number:'))
# p,i=1,1
# while i <=n:
#   p = p*i
#   i+=1
# print('The factorial is:',p)
# print

# #TODO:7. Write a python script to count digits in a given number

# count = 0
# num = int(input('Enter the number:'))
# while num>0:
#   number = num %10
#   num = num//10
#   number = num
  
#   count = count+1      

# print('Total number of digits is:', count)

# # 2nd Way

# n = int(input('Enter the number:'))
# count = 0
# while n !=0:
#   n=n//10
#   count = count+1
# print('The number of digits in a number is:',count)
  
  
# #TODO: 8. Write a python script to calculate sum of digits of a given number
# i = int(input('Enter the number:'))
# sum = 0
# while i>0:
#   sum = sum+(i%10)
#   i=i//10
  
# print(sum)


# # 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
