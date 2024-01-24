#!/usr/bin/python3
jumbled_data = [[611], [101, 0], [411], [411], [111, 0], [411], [76, 1], [84, 0], [70], [321], [80], [411], [84, 1], [95, 0], [52], [611], [95, 0], [711], [110], [74, 0], [711], [901], [98, 0], [801], [94, 1], [110], [71], [33, 0], [33, 0], [95, 0], [65, 1], [52], [51], [50], [75, 1], [521]]

def jumble(string):
  bigset = []
  value = []
  thing = [[] for i in range(len(string))]
  for i in range(len(string)):
    thing[i].append(ord(string[i]))
    thing[i].append(int(str(ord(string[i]))[::-1]))
  for j in range(len(thing)):
    value.append(max(thing[j]))
    if 33 <= thing[j][0] <= 126:
      if 33 <= int(str(thing[j][0])[::-1]) <= 126:
        if max(thing[j]) != thing[j][0]:
          value.append(1) # Swapped num with reverse in range
        else:
          value.append(0) # Not swapped num with reverse in range
    bigset.append(value)
    value = []
  return bigset

def main():
  print("Think you unjumbled the flag?")
  n = str(input("Enter the flag here to validate: "))
  if jumble(n) == jumbled_data:
    print("Correct! Submit the flag you just inputted for points.")
  else:
    print("Incorrect! Try again.")

if __name__ == "__main__":
  main()
