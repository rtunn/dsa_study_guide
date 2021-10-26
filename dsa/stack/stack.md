# Stack

A stack is essentially a LIFO queue.

## Use Cases

### Balancing brackets

Push opening brackets to the stack. If a closing bracket is encountered, check if top of stack is the matching opening bracket. If so, pop from the stack and continue. Else, the brackets are not balanced.

### Two Stack Queue

A FIFO queue may be implemented using two stacks.

Enqueue: push each item to stack 1.

Dequeue:

-   If stack 2 is empty, for each item in stack 1, pop the item from stack 1 then push the item to stack 2.
-   Finally, pop from stack 2

### Track Minimum in Window

-   Given a list of non-negative integers, append a 0 to the end of the list.
-   Create an empty stack
-   Iterate over the list
-   declare j = i
-   While the i-th item of the list is greater than or equal to the item on the top of the stack, pop from stack
-   Push a tuple to the stack containing the item and either its index if item less than top of stack, or the index of the last popped stack item
-   During iteration, i - j gives the size of the window
-   The top of the stack is the local minimum for the window from j to i
