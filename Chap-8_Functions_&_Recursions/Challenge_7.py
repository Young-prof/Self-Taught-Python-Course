# Wrte a python function to remove a given word from a list and strip it at the same time
def removeAgivenWord(l, word):
    word = word.strip()
    if (word in l):
        l.remove(word)
    return List


List = ['Franklyn', 'Tekenatei', 'Perezitei', 'James', 'Ayiba']
List = removeAgivenWord(List, ' Franklyn')
print(List)
