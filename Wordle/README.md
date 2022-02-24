# Wordle suggestion generator

This program will give you the list of 5-letter words that might still be the solution, given the guesses you've made so far.

## How it works

Each guess is encoded as the 5 letters followed by 5 numbers in the range 0-2:

0. Gray: The letter does not appear in the solution.
0. Yellow: The letter is in the solution but not in this position.
0. Green: The letter is in the solution at this position.

Let's say you've already made two guesses "TALES" and "TWERP":

![T](https://via.placeholder.com/30/20AF20/FFFFFF?text=T)
![A](https://via.placeholder.com/30/202020/FFFFFF?text=A)
![L](https://via.placeholder.com/30/202020/FFFFFF?text=L)
![E](https://via.placeholder.com/30/AFAF20/FFFFFF?text=E)
![S](https://via.placeholder.com/30/202020/FFFFFF?text=S)

![T](https://via.placeholder.com/30/20AF20/FFFFFF?text=T)
![W](https://via.placeholder.com/30/202020/FFFFFF?text=W)
![E](https://via.placeholder.com/30/AFAF20/FFFFFF?text=E)
![R](https://via.placeholder.com/30/AFAF20/FFFFFF?text=R)
![P](https://via.placeholder.com/30/202020/FFFFFF?text=P)

These would be encoded as `tales20010` and `twerp20110`:

```shell
$ python3 possible_words.py tales20010 twerp20110
```
```shell
['tenor', 'terce', 'terfe', 'terne', 'throe', 'torte', 'tribe', 'trice', 'tride', 'trike',
'trine', 'trite', 'trode', 'troke', 'trone', 'trove', 'truce', 'tryke', 'turme']
```

The output is just the list of all words that could still be the solution, given all the guesses.
Do with that information what you will.
