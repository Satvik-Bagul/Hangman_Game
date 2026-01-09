import random


def make_phrase():
  try:
    with open("phrases.txt", "r") as fd:
      phrases = fd.read().splitlines()
    phrase = random.choice(phrases).upper()
  except FileNotFoundError:
    print("Couldn't find phrases.txt, make sure you have it in the same folder as this file.")
    return "When you gaze long into the abyss, the abyss gazes also into you".upper()
  except IndexError:
    print("phrases.txt seems to be empty. Add some phrases to it, one per line.")
  return phrase


def print_gallows(misses):
  # +---+
  # |   |
  # |  \O/
  # |   |
  # |  / \
  # |
  # |_____
  hd,bd,ll,rl,la,ra = tuple("O|/\\\\/"[:misses] + (6*" ")[misses:])
  print(f"+---+\n|   |\n|  {la}{hd}{ra}\n|   {bd}\n|  {ll} {rl}\n|\n|_____")
  print(f"Incorrect guesses made: {misses}/6")

def print_revealed_phrase(str,l):
  guess=''
  for word in str:
    if word in l:
      guess+=word
    elif word.isalpha()==False:
      guess+=word
    else:
      guess+='_'
    
  print(guess)

def return_revealed_phrase(str,l):
  guess=''
  for word in str:
    if word in l:
      guess+=word
    elif word.isalpha()==False:
      guess+=word
    else:
      guess+='_'
    
  return guess


print("Actual: ", end="") # So that the printed phrase is in the same line
print_revealed_phrase("COMP SCI@ 2025", ['C', 'P', '5'])
print("Expected: C__P _C_@ 2025")

print("Actual: ", end="") # So that the printed phrase is in the same line
print_revealed_phrase("NEW CS BUILDING! FALL 2025", ['N', 'E', '0', 'I'])
print("Expected: NE_ __ __I__IN_! ____ 2025")


def get_letter(l):
  while True:
    inp=input('Please enter a letter: ')
    guess=inp.capitalize()
    if len(inp)>1:
      print(f'"{inp}" is not a letter!')

      
    elif guess.isalpha():
      if guess in l:
        print(f'"{inp}" has already been guessed!')
      else:
        return guess
    else:
      print(f'"{inp}" is not a letter!')  

def won(str,l):
  new_str=str.split()
  check=0
  
  for i in new_str:
   for j in i:
      if j.isalpha():
        if j in l:
          check+=0
        else:
          check+=1
      else:
        continue
  if check>0:
    return False
  else:
    return True


def play_game():
  print('***Welcome to Hangman***')
  phrase=make_phrase()
  misses=0

  
  guesses=[]
 
  print_gallows(misses)
  count=0
  while misses<7:
    
    print_revealed_phrase(phrase,guesses)
    if len(guesses)<2:
      print(f'Letters guessed: {guesses}')
    else:
      sorted_guesses=sorted(guesses)
      print(f'Letters guessed: {sorted_guesses}')
    guess=get_letter(guesses)
    if guess not in phrase:
      misses+=1
      guesses.append(guess)
      print_gallows(misses)
      
      if misses==6:
        print('Game Over!')
        print(f'Solution was: {phrase}')
        break
    else:
      guesses.append(guess)
      
    
    done=return_revealed_phrase(phrase,guesses)
    if '_' not in done:
      print(done)
      print('Congratulations!')
      break

