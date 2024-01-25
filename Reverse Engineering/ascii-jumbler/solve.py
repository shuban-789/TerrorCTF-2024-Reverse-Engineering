#!/usr/bin/python3
jumbled_data = [[611], [101, 0], [411], [411], [111, 0], [411], [76, 1], [84, 0], [70], [321], [80], [411], [84, 1], [95, 0], [52], [611], [95, 0], [711], [110], [74, 0], [711], [901], [98, 0], [801], [94, 1], [110], [71], [33, 0], [33, 0], [95, 0], [65, 1], [52], [51], [50], [75, 1], [521]]

def solve(data):
  ret = ""
  for i in range(len(data)):
    if (33 <= data[i][0] <= 126) and (len(data[i]) == 2):
      if data[i][1] == 0:
        ret += chr(data[i][0])
      elif data[i][1] == 1:
        ret += chr(int(str(data[i][0])[::-1]))
    else:
      if (data[i][0] < 33) or (data[i][0] > 126):
        ret += chr(int(str(data[i][0])[::-1]))
      else:
        ret += chr(data[i][0])
  return ret
  
print(solve(jumbled_data))
