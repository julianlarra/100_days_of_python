height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

IMC = round(weight / (height * height))
print(f" You IMC is: {IMC}")

if IMC >= 18.5:

    if IMC <= 25:
        print("You have a normal weight")
    elif IMC <= 30:
        print("You are slightly overweight")
    elif IMC <= 35:
        print("You are obese")
    else:
        print("You are clinically obese")
else:
    print("You are underweight")