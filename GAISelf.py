#Exercise on functions, Easy part
1
def say_hello(name):
  print(f"Hello, {name}!")
say_hello("Ridoh")

2
def add_three_numbers (a, b, c):
  print(f"The sum of the three numbers is: ", a+b+c)
add_three_numbers(5, 6, 7)

3
def area_of_rectangle(length, breadth):
  print(f"the area of the rectamgle is: ", length*breadth)
area_of_rectangle(5, 6)

#Intermediate
1
def check_even_odd(number):
  if number%2==0:
    print(f"{number} is even number")
  else:
    print(f"{number} is odd number")
check_even_odd(7)

2
def personalized_greeting(name="Geust", age=0):
  print(f"Hello, {name}! You are {age} years old.")
personalized_greeting("Ridoh", 32)
personalized_greeting()

3
def simple_calculator(a,b,operation):
  if operation=="+":
    return (f"The sum of {a} and {b} is:  {a+b}")
  elif operation=="-":
    return (f"The difference between {a} and {b} is: {a-b}" )
  elif operation=="*":
    print(F"The product of  {a} and {b} is: {a*b}")
  elif operation=="/":
    if b==0:
      print("Error: Division by zero")
    else:
      print(f"The division of {a} and {b} is: {round(a/b,2)}")
  else:
    print("Invalid operation")
simple_calculator(5, 6, "/")