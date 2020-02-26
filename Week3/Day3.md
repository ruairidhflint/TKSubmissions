## Draw/model out inserting a new element into a binary search tree.

When inserting a new element into a binary tree there are effectively three potential scenarios:
The item to be inserted is bigger than the root node, the item is smaller than the root node or the item 
is equal to the root node. The latter is often up to the implementor so we will first examine options 1 and 2.

If the item to be inserted is bigger than the root node, we need to check the right hand, which is designated as the
'bigger' side. If the path points to None, or null, we insert our new element at that point. 
However, if there is an item already at that point, we run the whole thing again replacing the root node with the 
element we have encountered. This will ask us again if our new item is bigger or smaller than this item.
The pattern continues until we eventually find an empty spot for our new element to rest.

Option 2 is identival but in reverse, we are continually looking for an emoty node to place our element but
this time we are going to start off on the left.

Option 3 is up to the developer. Some binary trees stop the process if a duplication is encountered and do not 
allow it. Others just choose a set path, eg...if we encounter an identical value node, always send the new item
to the left. This keeps things consistent without having to reject values based on duplication. 

## Draw/model out how to traverse a binary search tree and get to the minimum element in the tree.

This is incredibly simple. Given the left hand side node will always be lower, we continually traverse 
the left hand side until we cannot go any deeper. The node we are currently at will be the minimum value. 
The nature of the binary search tree will mean we can only ever be at the lowest value in this situation. 

## Draw/model out how to traverse the tree in order from the smallest element in the tree to the largest element in the tree.

To traverse a tree from smallest to largest, we first need to, logically, find the smallest node. The next smallest will
be the node that has it's left value pointing to our smallest element and then the next smallest will be the right hand side
element of this node. 
So a pattern emerges! 
We print the left, the node, the right!
But we need to go right down to the bottom!
So we can recursively check that a node exists, then apply our traversal to the the left side, access the node, and then
traverse the right side. This will bubble up and eventually have all elements, from lowest to highest, traversed. 