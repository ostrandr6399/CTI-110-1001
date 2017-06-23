# Get the price of the meal
#Calculate the sales tax .07
#Calculate the tip .18

Meal = float(input('Enter the price of your meal:  '))
sales_tax = Meal * .07
total_meal = Meal + sales_tax
print (format (total_meal, '.2f'), 'Is what your food cost with sales tax.')
tip = total_meal * .18
print (format (tip, '.2f'), 'is your tip.')
your_total_cost = total_meal + tip
print (format (your_total_cost, '.2f'), 'is your total cost.')
