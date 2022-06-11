account = 100
interest_rate = .075
years = 21

print(f"Initial Amount: {account}")

counter = 1
while counter <= years:
    accrued_interest = account * interest_rate
    account += accrued_interest
    rounded = round(account, 2)
    print(f"Year {counter}: {rounded}")
    counter += 1


