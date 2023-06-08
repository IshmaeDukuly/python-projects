

# The programme calculates the number of days, weeks, and months you will have if your were to live 100 years

age_as_int = int(input("What is your current Age?: "))
years_remaining = 100 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12


message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months"
print(message)