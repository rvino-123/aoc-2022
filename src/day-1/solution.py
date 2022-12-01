def line_file_generator(lines):
  for l in lines:
    yield l.replace("\n", "")


def main():
  max_calories = 0
  elf_inventory = []
  with open('./input.txt', 'r') as f:
    for line in line_file_generator(f.readlines()):
      if line == "":
        max_calories = max(max_calories, sum(elf_inventory))
        elf_inventory.clear()
      else:
        elf_inventory.append(int(line))
  
  return max_calories


if __name__ == "__main__":
  main()