weight=int(input("weight in kgs:"))
height=float (input("height in meters:"))
bmi=weight/(height)**2
if bmi<18.5:
    print("you are underweight")
elif 18.5 <= bmi <24.9:
    print("you are normal weight")
elif 25.0 <= bmi <29.9:
    print("you are over weight")
else:
   print("you are obese")