# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 1
extra_payment_end_month = 13
extra_payment = 1000

while principal > 0:
    month = month + 1

    if extra_payment_start_month <= month < extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    if principal < current_payment:
        current_payment = principal * (1 + rate / 12)

    principal = principal * (1 + rate / 12) - current_payment
    total_paid = total_paid + current_payment

    print(month, total_paid, principal)
