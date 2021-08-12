# rollercoaster permite vender entradas a quienes cumplan el requisito de altura minima
# y a quienes puedan ingresar determina la tarifa adecuada segun el rango de edad.
# Tambien permite ofrecer la opccion de agregar una foto y el monto es añadido al boleto final
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print ("You can ride the rollercoaster¡")
  age = int(input("What is your age?"))
  if age < 12:
     bill = 5
     print("Child tickets are $5.")
  elif age <= 18:
     bill = 7
     print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo =  input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y" :
   bill += 3
   print(f"Your final bill is ${bill}")

  else:
    print(f"Please pay ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")
