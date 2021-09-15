# bounce.py
#
# Exercise 1.5
height_drop = 100
bounce = 1

while bounce < 10:
    height_drop = height_drop * 3 / 5
    print(bounce, round(height_drop))
    bounce = bounce + 1

# num_bills = 1
# sears_height = 443
# bill_thickness = 0.11 * 0.001
# day = 1

# while num_bills * bill_thickness < sears_height:
#     print(day, num_bills * bill_thickness)

#     day = day + 1
#     num_bills = num_bills * 2