Good_credit=False
price=100000
down_payment=price
if Good_credit:
    down_payment=price*0.1
else:
    down_payment=price*0.2

print(f'down_payment is ${down_payment}')