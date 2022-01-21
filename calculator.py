
#  add
def add(n1, n2):
 return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2

operations = {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide,
}

num1= int(input("What's the first number?: "))

for simbol in operations:
  print(simbol)

operation_simbol= input("Pick an operation from the line above:\n")

num2= int(input("What's the second number?: "))

calculation_function= operations[operation_simbol]

answer= calculation_function(num1, num2)

print(f"{num1} {operation_simbol} {num2} = {answer}")

