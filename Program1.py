print("Welcome to Melanie dental clinic")

print (input("what is your name?"))

a= input("have you ever been here before?")

if(a=="yes"):
    print("Welcome back")
else:
    print("we hope you have the best first experience here")

height= input("what is your height in cm")
weight= input("what is your weight in kg")
print (input("when were you last weighed in?"))

print ("practitioner's assessment of health")

bmi=(weight/(height**2))*10000
bmi=round(bmi,2)

print(bmi)

if(bmi>30):
    print("you are obese")
    intermediate_health_score=0
elif(bmi>25 and bmi<29.9):
    print("you are overweight")
    intermediate_health_score=3
elif(bmi>18.5 and bmi<24.9):
    print("you are healthy")
    intermediate_health_score=5
elif(bmi>17 and bmi<18.4):
    print("you are underweight")
    intermediate_health_score=3
elif(bmi<17):
    print("you are thin")
    intermediate_health_score=0
    
