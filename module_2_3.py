my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
b = 0
while b <= len(my_list):
    a = my_list[b]
    b += 1
    if a < 0:
        break
    elif a == 0:
        continue
    else:
        print(a)










