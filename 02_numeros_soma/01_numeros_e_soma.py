#!/usr/bin/python3
#
####### Formatando Strings ########
#
# Transformando string em inteiro
quantidade_string = "3"
total = int(quantidade_string) + 2
print(total)
#
# Transformando string em real
quantidade_string = "3"
total = float(quantidade_string) + 2
print(total)
### Exemplo de calculos ###
# The cost of one server per hour.
cost_per_hour = 0.51
# Compute the costs for one server.
cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day
# Compute the costs for twenty servers
cost_per_day_twenty = 20 * cost_per_day
cost_per_month_twenty = 20 * cost_per_month
# Budgeting
budget = 918
operational_days = budget / cost_per_day
# Display the results.
print('Cost to operate one server per day is ${:.2f}.'.format(cost_per_day))
print('Cost to operate one server per month is ${:.2f}.'.format(
    cost_per_month))
print('Cost to operate twenty servers per day is ${:.2f}.'.format(
    cost_per_day_twenty))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(
    cost_per_month_twenty))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(
    budget, operational_days))
#
# Fontes:
# Curso Python for Beginners: Learn Python Programming (Python 3) Udemy Aula 10 a 14
