# Here we remove item by the Values stored in the Variable

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Working with a value that is been removed with the remove method

faultyCar = 'suzuki'
motorcycles.remove('suzuki')
print(motorcycles)

result = f"Yeah, that's my First Car actually, the '{faultyCar}', i sold it because it is faulty"
print(result)
