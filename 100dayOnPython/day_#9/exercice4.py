myList =[2,4,5,8,7,9,4,7,8,0,0,3,8]
delDoublons = []

for item in myList:
     if item not in delDoublons:
          delDoublons.append(item)

print(f'la nouvelle list sans doublons est {delDoublons}')