#list is_even
#range(1,5)(start, stop)-1
#arg =X (x =1,x=2,x=3,x =4)
# x=1 1*10,
# is_even=[lambda  args=x: args*10 for x in range(1,5)]
# for item in is_even:
#     print(item())
# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num)
#Max lambda function
Max =lambda a,b : a if(a>b) else b
print(Max(2,4))

#filters a list of ages of above 18
ages =[20,5,6,40,60,90,50,10]
above_eighteen =list(filter(lambda age: age >18, ages))
print(above_eighteen)