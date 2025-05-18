def dictData(dicyonary_data):
    print('keys values items')
    for key in dicyonary_data:
        value = dicyonary_data[key]
        print(key, value, key)

data = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dictData(data)
