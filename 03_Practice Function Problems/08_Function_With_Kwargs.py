def sum_numbers(**kwargs):
    sum = 0
    for key, values in kwargs.items():
        print(f"{key} : {values}")

print(sum_numbers(a=1, b=2, c=3, d=4))
print(sum_numbers(a=1, b=2, c=3, d=4))