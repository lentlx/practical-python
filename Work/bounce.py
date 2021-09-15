# bounce.py
#
# Exercise 1.5
heightDrop = 100
bounce = 1

while bounce < 10:
    heightDrop = heightDrop * 3 / 5
    print(bounce, round(heightDrop))
    bounce = bounce + 1

