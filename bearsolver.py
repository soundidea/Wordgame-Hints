import argparse
import sys
from collections import Counter
from functools import partial

def word_matches(letters, must_have, word):
  wc = Counter(word.lower())
  return (wc & must_have == must_have) and (letters & wc == wc)

def solve(words, letters, must_have, nice_to_have):
  mhc = Counter(must_have)
  word_filter = partial(word_matches, Counter(letters), mhc)
  matches = sorted(filter(word_filter, words), key=len, reverse=True)
  if (nice_to_have):
    nthc = Counter(nice_to_have)
    matches = sorted(matches, key=lambda w: sum(((Counter(w) - mhc) & nthc).values()), reverse=True)
  return matches

def process_args(argv):
  parser = argparse.ArgumentParser(description='Solve me a bear.')
  parser.add_argument('--words', metavar='FILENAME', required=True,
    help='Filename of a word list.')
  parser.add_argument('--letters', metavar='ABC', required=True,
    help='All the visible letters.')
  parser.add_argument('--must_have', metavar='ABC',
    help='Letters that must be used.')
  parser.add_argument('--nice_to_have', metavar='ABC',
    help='Letters that we\'d like to include. If this is present, the results are sorted to '
    'prioritize words containing the greatest number of these letters.')
  args = parser.parse_args(argv)
  with open(args.words, 'r') as wordfile:
    words = wordfile.read().splitlines()
  lc = Counter(args.letters.lower())
  if args.must_have:
    mhc = Counter(args.must_have.lower())
    if lc & mhc != mhc:
      raise ValueError(
        'All characters in --must_have must be present in --letters.')
    lc = lc - mhc
  return (
    words,
    args.letters.lower(),
    args.must_have.lower() if args.must_have else None,
    args.nice_to_have.lower() if args.nice_to_have else None)

if __name__ == "__main__":
  words, letters, must_have, nice_to_have = process_args(sys.argv[1:])
  print solve(words, letters, must_have, nice_to_have)
