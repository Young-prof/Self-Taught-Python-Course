oxford = {
    'lakdi': 'mood',
    'kursi': 'Chair',
    'chaku': 'knife'
}
key = input("Enter the key\n")
if (oxford.get(key) == None):
    print("Value not Found")
else:
    print("the value correspinding to your key is: ", oxford.get(key))
