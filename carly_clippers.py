#!/bin/python3

hairstyles = ["Bouffant", "Pixie", "Dreadlocks", "Crew", "Bowl", "Bob", "Mohawk", "Flattop"]
prices = [15, 10, 15, 20, 30, 40, 50, 35]
last_week = [2, 3, 2, 4, 4, 5, 6, 3]

total_price = 0
for price in prices:
    total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
