word = input('donner un mot ')

if word[0] == word[-1]:
     print(f"{word} commence et termine par le meme caractère")
else:
     print(f"{word} ne commence et ne temine pas par le meme caratère ")
