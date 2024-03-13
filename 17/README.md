# Problem 17
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 11337 | 10511 |
| Time | 13:39:14 | 14:13:42 |

Ranking and time honestly don't really matter at this point because I gave up on doing the problems when they dropped. I just find them intriguing, in a way.

## Speeds
Part 1:
```
real    0m13.656s
user    0m12.720s
sys     0m0.636s
```

Part 2:
```
real    2m25.111s
user    2m13.997s
sys     0m0.701s
```

## Thoughts
This one took a while since I didn't realize that the closed set should also include the direction and number of times the direction had been done consecutively. I got it shortly afterwards, although the solution was pretty slow.

But then came part 2. It's honestly hilarious how long part 2 takes. I kept debugging because I didn't realize I set the end coordinates to check as though the grid were a square because I thought the program was looping too much. But it didn't actually matter, since my actual input was a square. It did at least help me debug me checking for end and turning conditions, though.

But this was fun. It's been a while since I implemented Dijkstra.