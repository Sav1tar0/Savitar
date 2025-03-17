your_current_amount = float (input("Enter the amount: "))
your_current_currency=input("Enter the currency:(USD, EUR, AZN, TL) ").upper()
your_target_currency=input("Enter the target currency:(USD, EUR, AZN, TL) ").upper()

rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'AZN': 1.7,
    'TL': 25.0
}

if your_current_currency not in rates or your_target_currency not in rates:
    print("invalid currency")
else:
    converted_amount = your_current_amount * (rates[your_target_currency] / rates[your_current_currency])
    print(str(your_current_amount) + your_current_currency + "=" + str(converted_amount) + your_target_currency)
