def kg_to_lbs():
    weight_lbs = float(input(" Enter weight in lbs:"))
    unit = input("p for pounds and k for kgs:")
    if unit.upper() == "P":
        converted = weight_lbs * 0.45
        print(f'you are {converted} pounds')
    elif unit.upper() == "K":
        converted = weight_lbs / 0.45
        print(f'you are {converted} kilos')


kg_to_lbs()
