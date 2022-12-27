oxford = {
    "gift": "Something willingly given to someon to appreciate",
    "this": "A keyword in C#",
    "Youtube": "a video sharing platform",
    "Instagram": "A picture sharing platform",
    "myList": [2, 4, 3, 3]
}
print(oxford)

print(oxford.keys())

print(oxford["this"])

for a, b in oxford.items():
    print(a, b)

for keys in oxford.keys():
    print(keys)

print(oxford.get("notpresent"))
