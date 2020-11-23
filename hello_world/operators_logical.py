#if the applicant has good credit and has high income then operator logical is going to be printed
has_high_income=True
has_good_credit=True
has_criminal_record=False
if has_good_credit and not has_criminal_record:
    print('You are elligble for loan')
temp=input("Please enter tempreature: ")
if int(temp)>30:
    print("It's a hot day ")
else:
    print("it's a cold day")