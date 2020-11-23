weight_kg=float(input(" Enter weight in lbs:"))
unit=input("L for pounds and k for kgs:")
if unit.upper()=="L":
    converted=weight_kg*0.45
    print(f'you are {converted} kilos')
else:
    converted=weight_kg/0.45
    print(f'you are {converted} kilos')
