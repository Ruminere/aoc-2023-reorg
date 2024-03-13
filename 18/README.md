# Problem 18
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 2262 | 700 |
| Time | 00:40:19 | 00:43:41 |

I did not realize this was just Pick's at first, so I tried flood-fill. However, my code was buggy and slow, so while it was running (and gave me the correct answer) I realized it was just Shoelace, so I searched it up [and copied the solution that would cost me the least time in terms of preprocessing](https://code.activestate.com/recipes/578047-area-of-polygon-using-shoelace-formula/). It still didn't work and I was confused as to why the test input kept returning 42, but realized it was finding the area, not the number of total points. At that point I realized it was an application of Pick's Theorem.

Had I realized what it was from the very start, I probably would've gotten leaderboard, considering that the times weren't very fast (especially for part 2). Oh well.