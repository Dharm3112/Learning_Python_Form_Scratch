def even_generator(num):
    li = []
    for i in range(2, num + 1, 2):
        li.append(i)
    return li

print(even_generator(10))