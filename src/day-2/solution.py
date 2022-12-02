# Very sick and tired today, so my brain can only muster up this solution :(
game = {
  'part_1': {
    'letter_points_map': {
      'X': 1,
      'Y': 2,
      'Z': 3,
    },
    'winning_combinations': [('A', 'Y'), ('B', 'Z'), ('C', 'X')],
    'draw_combinations': [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
  }, 
  'part_2': {
    'letter_points_map': {
      'X': {
        'A': 3,
        'B': 1,
        'C': 2
      },
      'Y': {
        'A': 4,
        'B': 5,
        'C': 6
      },
      'Z': {
        'A': 8,
        'B': 9,
        'C': 7,
      }
    }, 

  },

}

def read_input(file_path):
  for row in open(file_path, 'r'):
    row = row.strip().replace(" ", "")
    yield (row[0], row[1])


def part1():
  score = 0
  for game_round in read_input('./input.txt'):
    points_from_play = game['part_1']['letter_points_map'][game_round[1]]
    if game_round in game['part_1']['winning_combinations']:
      score += 6 + points_from_play
    elif game_round in game['part_1']['draw_combinations']:
      score += 3 + points_from_play
    else:
      score += points_from_play

  return score

def part2():
  score = 0
  for game_round in read_input('./input.txt'):
    score += game['part_2']['letter_points_map'][game_round[1]][game_round[0]]

  return score

def main():
  print(part1())
  print(part2())
  

if __name__ == "__main__":
  main()