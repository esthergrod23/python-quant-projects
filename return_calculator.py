initial_money = float(input("Initial money: "))
return_percent = float(input("Return %: "))
decimal_return = return_percent / 100
profit_loss = initial_money * decimal_return

# Calculate final capital
final_money = initial_money + profit_loss

# Print results
print("-------- RESULT --------")
print("Initial money:", initial_money)
print("Return %:", return_percent)
print("Profit/Loss:", profit_loss)
print("Final money:", final_money)


if final_money > initial_money:
    print("Status: Profit")
elif final_money < initial_money:
    print("Status: Loss")
else:
    print("Status: No change")
