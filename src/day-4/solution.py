import re

def part_1():
  counter = 0
  with open("./input.txt") as f:
    for i in f.readlines():
      short_ids = re.findall('[0-9]+', i)
      if int(short_ids[0]) >= int(short_ids[2]) and int(short_ids[1]) <= int(short_ids[3]):
        counter += 1
        continue
      if int(short_ids[0]) <= int(short_ids[2]) and int(short_ids[1]) >= int(short_ids[3]):
        counter += 1
        continue
  return counter


def part_2():
  counter = 0
  with open("./input.txt") as f:
    for i in f.readlines():
      short_ids = re.findall('[0-9]+', i)
      for i in range(int(short_ids[0]), int(short_ids[1]) + 1):
        if i in range(int(short_ids[2]), int(short_ids[3]) + 1):
          counter +=1
          break 
  return counter


def main():
  print(part_1())
  print(part_2())

if __name__ == "__main__":
  main()