"""
OOP implementation of the solution. 
OVERENGINEERED LOL
"""
from enum import IntEnum

class InputReader:
  def __init__(self, filepath: str) -> None:
    self._path = filepath
  
  def __iter__(self):
    for line in open(self._path):
      yield line.strip()
  
  def get_number_of_lines(self):
    with open(self._path) as f:
      return len(f.readlines())


class LetterType(IntEnum):
  """
  Enum representation of a letter being uppercase
  or lowercase. 
  """
  UPPERCASE = 1
  LOWERCASE = 2

  @classmethod
  def get_conversion_factor(cls, letter_type):
    """
    0-26 range is reached by subtracting 96 from the lowercase ascii value
    27-52 range is reached by subtracting 38 from uppercase ascii value
    """
    if letter_type == cls.LOWERCASE:
      return 96
    elif letter_type == cls.UPPERCASE:
      return 38
    else:
      return None


class RuckSackItem:
  """
  Item that can be placed into a rucksack. Calculates the priority
  of the rucksack. 
  """
  def __init__(self, item: str) -> None:
    self.item = item
    self._type = LetterType.UPPERCASE \
      if item.isupper() else LetterType.LOWERCASE

  def _convert_item_to_priority(self):
    """
    Calculates the priority of the item by converting the character 
    to it's ASCII presentation then subtracting the conversion factor
    depending on Lettertype
    """
    conversion_factor = LetterType.get_conversion_factor(self._type)
    return ord(self.item) - conversion_factor
  
  def get_priority(self):
    """
    Returns the priority of the item. 
    """
    return self._convert_item_to_priority()


class RuckSack:
  def __init__(self, rawString: str) -> None:
    self._rawString = rawString
    self._split_contents()

  def _split_contents(self) -> None:
    """
    Divides the rawString into 2 equal parts.
    """
    middle = len(self._rawString) // 2
    self._compartment1 = self._rawString[0:middle]
    self._compartment2 = self._rawString[middle:]
  
  def find_common_character(self):
    """
    Finds the common character of the two compartments otherwise
    returns None.
    """
    common_character = [c for c in self._compartment1 if c in self._compartment2 ]
    if common_character:
      return RuckSackItem(common_character[0])
    return None


class Solution:
  def solve_part_1(self):
    reader = InputReader("./input.txt")
    priority_sum = 0
    for i, line in enumerate(reader):
      rucksack = RuckSack(line)
      common_char = rucksack.find_common_character()
      if common_char:
        priority_sum += common_char.get_priority()
    return priority_sum
  
  def solve_part_2(self):
    reader = InputReader("./input.txt")
    priority_sum = 0
    count = 0
    temp = []
    for line in reader:
      if count != 3:
        temp.append(line)
        count += 1
      else:
            priority_sum += self._part_2_find_common_item_in_group(temp)
            temp.clear()
            temp.append(line)
            count = 1

    priority_sum += self._part_2_find_common_item_in_group(temp)
    return priority_sum

  def _part_2_find_common_item_in_group(self, items: list[str]):
    base = set(items[0])
    for j in base:
      if j in items[1] and j in items[2]:
        item = RuckSackItem(j)
        return item.get_priority()


if __name__ == "__main__":
  solution = Solution()
  print(solution.solve_part_1())
  print(solution.solve_part_2())

