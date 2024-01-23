#!/usr/bin/python3
jumbled_data = [611, 101, 411, 411, 111, 411, 76, 84, 70, 321, 80, 411, 84, 95, 52, 611, 95, 711, 110, 74, 711, 901, 98, 801, 94, 110, 71, 33, 33, 95, 65, 52, 51, 50, 75, 521]

# REMEMBER: The reverse of a number 500, 50, and 5 is all 5. When dealing a number like that, think about which one would work...
def jumble(string):
  value = []
  thing = [[] for i in range(len(string))]
  for i in range(len(string)):
    thing[i].append(ord(string[i]))
    thing[i].append(int(str(ord(string[i]))[::-1]))
  for j in range(len(thing)):
    value.append(max(thing[j]))
  return value

def main():
  print("Think you unjumbled the flag?")
  n = str(input("Enter the flag here to validate: "))
  if jumble(n) == jumbled_data:
    print("Correct! Submit the flag you just inputted for points.")
  else:
    print("Incorrect! Try again.")

if __name__ == "__main__":
  main()
