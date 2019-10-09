with open("/home/shuham97/Desktop/gitprjct/Hacktoberfest2019/Python/200805.jpg","rb") as image:
  f=image.read()
  b=bytearray(f)
  print(len(b))
  print(b)
