# Problem 12
| | Part 1 | Part 2 |
|---|---|---|
| Rank | 5069 | 1633 |
| Time | 1:15:40 | 1:27:58 |

I spent way too long trying to decide how to tackle this problem; in fact, I hadn't written a single line of code at 22 minutes. I knew from the get-go that this was recursion, but I didn't know whether I should split over the dots and recurse or recurse by iterating over indices. Ultimately, I chose the latter.

This thing was pretty complicated in terms of logic as well. I had to figure out which cases were actually going to contribute stuff and which might as well return nothing. I ulimately got it in the end, and then part 2 followed by applying dynamic programming so that my recursion would be more efficient. I also spent too long trying to debug my code because I forgot to clear my dictionary of cached values after processing every line I fed from the input.

Overall a fun and mentally intensive dynamic programming problem.
