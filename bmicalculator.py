weight = float(input("enter weight in kg"))
height = float(input("enter height in cm"))

height_in_meters = height/100
bmi = weight/(height_in_meters **2)

print("your BMI is:", bmi)

if bmi < 18.5:
    print("You're underweight")
elif 18.5 <= bmi < 25:
    print("you're a normal weight")
elif 25 <= bmi < 30:
    print("you're overweight")
else:
    print("you're obese")
