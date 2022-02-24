import re, sys

def possible_words(all_words, greens, yellows, greys):
  """greens and yellows are sets of tuple(idx,letter).
     greys is a set of letters."""
  words = all_words[:]
  for i,l in greens:
    if l in greys:
      # special case, we have a letter in the right place and we know for sure it's not repeated
      words = list(filter(lambda w: l not in w or w[i] == l, words))
      greys -= set(l)
    else:
      words = list(filter(lambda w: w[i] == l, words))
  for i,l in yellows:
    if l in greys:
      # just discard the grey if it's also a yellow.
      # TODO: find a way to use this additional information, i.e. the letter appears exactly once and no more.
      greys -= set(l)
    words = list(filter(lambda w: l in w and w[i] != l, words))
  for l in greys:
    words = list(filter(lambda w: l not in w, words))
  return words

def convert_guess(guess):
  """Convert a guess into 3 arrays needed for input to possible_words().
     Each guess is 5 letters followed by 5 numbers (e.g. "abcde01020").
     The number value signifies:
       0 - letter not present
       1 - letter is present but in the wrong place (yellow)
       2 - letter is present in the right place (green)."""
  greens, yellows, greys = set(), set(), set()
  if not re.match(r'^[a-z]{5}[0-2]{5}$', guess):
    raise ValueError('"%s": guess must be 5 letters followed by 5 numbers in the range 0-2.' % guess)
  for idx, l in enumerate(zip(guess[:5], guess[5:])):
    if l[1] == '0':
      greys |= set(l[0])
    elif l[1] == '1':
      yellows |= set([(idx, l[0])])
    else:
      greens |= set([(idx, l[0])])
  return greens, yellows, greys

if __name__ == '__main__':
  words = [w.strip() for w in open('words.txt').readlines()]
  greens, yellows, greys = set(), set(), set()
  for guess in sys.argv[1:]:
    g,y,gr = convert_guess(guess.lower())
    greens |= g
    yellows |= y
    greys |= gr
  print(possible_words(words, greens, yellows, greys))
