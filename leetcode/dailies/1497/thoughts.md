# Approach

## Problem

![Problem 1497](problem_image.png)

## Initial thoughts

I have to somehow get this code to check for pairs using some sort of method that works for every number.

## Initial attempt

Thankfully, the first hint gave me a frequency formula that allows for easy pair checking: "((x % k) + k) % k". Using this, all you have to do is find when the frequencies are sums of k or are equal to 0. To do this initially, I used a set, but that was short sighted. I quickly switched to a dictionary, but then I had to deal with the logic.

## Obstacles

The main issue was deciding how exactly to deal with pairs. I could go through them one by one and delete them, but that is a little slow. I ended up with logic that checks when the array would fail the condition. If there were an uneven amount of 0s, then it would fail. If a + b = k, but the number of a did not equal the number of b, then it would also fail. Finally, if there were any leftover numbers c that didn't have a pair to add up to k, then it would also fail.

## Conclusion/Things I would do differently

I saw a really cool oneliner that could have been really cool if it worked in all cases. The person just summed the array and checked if the remainder of the sum and k was 0. Genius, or it would have been if it actually worked. Regardless, though, that served to once again remind me just how easy it is to fall into a certain mindset of finding a specific type of solution and forgetting that there are many other, sometimes easier, ways to solve it.

## Score

![LeetCode Score](score_image.png)