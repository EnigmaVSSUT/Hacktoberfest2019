with open("200805.jpg","rb") as image:
  f=image.read()
  b=bytearray(f)
  print(len(b))
  print(b)
