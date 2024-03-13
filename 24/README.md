# Problem 24
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 1614 | 3992 |
| Time | 01:04:04 | 10:58:50 |

I just barely missed the palindrome ranking (3993) for part 2!

Part 1 was straightforward enough once I actually understood what was happening. However, I misread the question twice; first I thought it was asking for how many hailstones *didn't* intersect, and then I didn't realize there was a boundary that the stones could collide in. That cost me quite some time, but at least the linear algebra was fun to implement (after just having taken the class last semester). I coded it generally enough since I thought part 2 was going to be the same as part 1, but with z-coordinates considered.

Part 2 marked my first time using sympy; I had to do quite a lot of Googling, but the implementation wasn't bad either. I was dreading having to calculate for all 300 lines, but then I realized the system was overconstrained, so the first three lines would suffice as I would have a system of 9 equations with 9 unknowns. Sympy was very clean—it'd be nice to explore it more in the future.