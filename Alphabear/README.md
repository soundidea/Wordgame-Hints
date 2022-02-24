# Bear Solver
A quick & dirty command-line tool for generating solutions for Alphabear puzzles.

## Parameters
|Param | Description |
------ | ----------- |
| --words=FILENAME | a file containing the list of words. On Macs and \*nixen, a good candidate is /usr/share/dict/words |
| --letters=ABCD | all the letters you can see on the board. All of them, even repetitions. |
| --must_have=ABCD | (optional) a list of the letters you must have in your solutions. This is usually going to be the ones with a current score of 1, but you might want to include one or two from the 2's that look like they're going to cause you trouble in the next turn. |
| --nice_to_have=ABCD | (optional) another list of letters that you'd like to see in the solutions if possible. This is usually going to be the ones with a current score of 2. |

## Examples
Let's say your board looks like this iTunes screenshot:

![](http://a2.mzstatic.com/us/r30/Purple5/v4/0d/8f/33/0d8f3362-ec3f-bd50-31bb-0be7c4718a23/screen322x572.jpeg)
```
$ python bearsolver.py --words=/usr/share/dict/words --letters=hetetlelachahcates
['castellate', 'catalecta', 'catastate', 'Chaetetes', 'Chechehet', 'echelette', 
'Hallstatt', 'saltcatch', 'teethache', 'aesthete', 'asellate', 'Athecata', 'athe
cate', 'Cactales', 'Calathea', 'castelet', 'catalase', ...
```

Or this one:

![](http://a4.mzstatic.com/us/r30/Purple7/v4/ae/4c/8b/ae4c8bbc-910d-cca6-ab70-e4bfb9cb2947/screen322x572.jpeg)
```
$ python bearsolver.py --words=/usr/share/dict/words --letters=fwnokeiwahfiss --
must_have=kno --nice_to_have=fwe
['knowe', 'kenosis', 'Kossean', 'Nesokia', 'Kiowan', 'soaken', 'Wikeno', 'Kohen'
, 'Koine', 'koine', 'oaken', 'snoek', 'snoke', 'snowk', 'soken', 'wakon', 'keno'
, 'know', 'Wishoskan', 'hinoki', 'inkosi', 'kishon', 'Hokan', 'ikona', 'Konia', 
'kosin', 'honk', 'kino', 'kona', 'nako', 'sonk', 'kon']
```

I'm sure you get the idea.

## Sort order of results
Results are sorted in decreasing order of size. If --nice_to_have is specified, then they are then sorted again in decreasing order of how many nice-to-have letters are in the word.

You won't always want to choose the first word in the list. Alphabear might not recognize it, or it might be strategically unwise for you to use that word, say if it's going to reveal too many 1-point skull-and-crossbones tiles on the next round, or you're trying to finish a game and you'd be left with a few tiles that don't spell any words.
