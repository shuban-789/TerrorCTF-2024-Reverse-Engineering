ct = "qdoqlq@SCz.l\\c1^_0df0rq^_0ocz"
flag = []
def decrypt(ct):
  for i in range(len(ct)):
    if i%2 == 0:
      flag.append(chr(ord(ct[i])+3))
    elif (ord(ct[i]) == 124) or (ord(ct[i]) == 125):
      flag.append(chr(ord(ct[i])+2))
    else:
      flag.append(chr(ord(ct[i])+1))
decrypt(ct)
print("".join(flag))
