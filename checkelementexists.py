list = [1, 2, 3, 4, 5, 6, 7, 8]
fe = 4
for i in list:
    if(i == fe):
        print("found")
        break
else:
    print("not found")


if(fe in list):
    print('true')
else:
    print("false")
