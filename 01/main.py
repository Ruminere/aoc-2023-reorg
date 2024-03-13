import sys, re

def __main__():
    filename = "actual"
    fh = open(filename + ".in")
    ans1 = 0
    ans2 = 0
    for line in fh:
        raw = line.strip()

        # part 1
        digits = re.findall(r'\d+', raw)
        ans1 += int(digits[0][0]) * 10 + int(digits[-1][-1])

        # part 2 - I need to relearn regex
        nums = []
        words = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10}
        for i in range(len(raw)):
            current_char = raw[i]

            if (current_char.isnumeric()):
                nums.append(int(current_char))
                continue

            for word in words.keys():
                if raw[i] == word[0] and word in raw[i:i+5]:
                    nums.append(words[word])
                    break
        ans2 += nums[0] * 10 + nums[-1]
    fh.close()
    print("1:", ans1)
    print("2:",ans2)

# ==================================================

__main__()