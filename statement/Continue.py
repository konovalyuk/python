j = 0
for i in range(5):
    j = j + 2
    print('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print('j not equal 6')
