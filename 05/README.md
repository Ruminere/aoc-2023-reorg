# Problem 5
## Dec 5 Remarks
Part 1 was fine, but I at first tried part 2 the naive way and it took way too long for everything to be appended to my array in the first place (and I likely would've received an OverflowError at some point), much less map them to other values. Then I decded to code everything as a series of ranges and then split them, and it was the splitting that gave me the most trouble in terms of implementation (in my defense, it was 12 AM). My immediate reaction to part 2 went like this:

> Oh my goodness this was disgusting to code, thank goodness it worked first try for me when I got the algorithm down

... because I'd made sure every smaller part worked beforehand.

## Dec 18 Remarks
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 3933 | 4366 |
| Time | 00:35:15 | 02:00:12 |

I'm back to clean some of the code up, and honestly, this problem looks just as crazy as it felt when I was coding it. The multitude of commented print statements support my words.

In `main.py`, I get a part 1 solution. Then I attempt to brute force part 2, but adding the individual seeds took too long, not to say the actual mappings. Hence my decision to code a new solution within `main1.py`. The logic itself wasn't bad, it's just that implementing the code itself was absolutely crazy and took me 01:24:57.

I've decided to not clean the print statements up and preserve the craziness. It's sort of like a museum exhibit, I guess.