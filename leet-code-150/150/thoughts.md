# Approach

## Initial thoughts

Knowing that this was a simple stack problem, I knew it was a simple single pass through iteration. Order of operations is adhered to by nature of the reverse notation and the only thing I needed to check was whether or not the next character was a number.

## Initial attempt

I began with initializing a list to serve as a stack and then got started on the for loop. The idea was that I would append to the stack if the token was an integer, and I would perform a simple operation based on the character if it was not an integer.

## Obstacles

The first obstacle I ran into was deciding how I wanted to perform the operations. I could simply run if/else or match/case statements, but I really didn't want to write all of that. So I went the route of storing the keys and functions inside a dictionary in order to make it look nice and write a little less. 

The second obstacle I ran into was then checking if the character was a number when the token started with a "-" (e.g "-11"). If I had thought about it a bit longer, I would has seen a very simple solution of checking if the character matched with a key inside the dictionary. Instead I went the convoluted route of using the ValueError received when trying to int("-11") vs int("-") in order to decide whether to push the integer or perform the operation. Occasionally being blind to the obvious answer is a mood.

The last obstacle was the fact that I needed to truncate division to 0, which I had forgotten how to do but was a simple fix nonetheless. 

## Things I would do differently

Aside from the obvious "use the dictionary I created" change, I am not too sure of how to speed this up. I could use stack[-1] instead of sum(stack) as I forgot to change that. I could also remove the redundant int(x) in the try block.