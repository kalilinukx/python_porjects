customer={
    'name':"john smith",
    'age':40,
    "is_verified":True,
    "birthdate":"jan 3 1878"
}
print(customer.get("birthdate","jan 1 1980"))
customer["name"]="jack smith"
print(customer["name"])