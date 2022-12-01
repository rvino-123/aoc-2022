def line_file_generator(lines):
  for l in lines:
    yield l.replace("\n", "")

def part_1():
  max_calories = 0
  elf_inventory = []
  with open('./input.txt', 'r') as f:
    for line in line_file_generator(f):
      if line == "":
        max_calories = max(max_calories, sum(elf_inventory))
        elf_inventory.clear()
      else:
        elf_inventory.append(int(line))

  return max_calories

def part_2():
  all_elves_total_calories = []
  current_elf_inventory = []
  with open('./input.txt', 'r') as f:
    for line in line_file_generator(f):
      if line == "":
        all_elves_total_calories.append(sum(current_elf_inventory))
        current_elf_inventory.clear()
      else:
        current_elf_inventory.append(int(line))
  return sum(sorted(all_elves_total_calories, reverse=True)[0:3])

def main():
  print("Part 1 Answer: {} ".format(part_1()))
  print("Part 2 Answer: {} ".format(part_2()))


if __name__ == "__main__":
  main()

# Ways to improve it
# 1. Reading the text and summing the inventory of each elf should be a seperate function as 
# to not violate the DRY principle. 
# 2. In part 2, I use the sorted method to sort the whole list, perhaps it would be better to only keep a list
# of size 3 sorted, compare the current elf total to the last array and sort as needed until the end. 