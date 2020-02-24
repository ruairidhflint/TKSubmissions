## Draw/model out inserting a new element into a linked list with only one element.

First step, create a new instance of the node/item class with the value being the new value and 
the pointer pointing to None.

On the Linked List class, we currently only have one item. That means the head value on the linked
list should point to the one item in the list as well as the tail value. 
Assuming we are inserting a value on to the end of the linked list, we must do several things.
First, the new tail value of the list is our new Node.
Secondly, we access the head value (also the previous tail value) and change it's pointer from None
to our new Node. 

## Draw/model out how to traverse through a linked list in order to find a target value.

I'm not sure what the obvious or common solution is, but I asusme it would be something along the lines
of starting at the head, checking the value, if the value is not None or the value itself, we
then access the next node in the list via the pointer. We repeat the process until the pointer is
pointing to None/Null (which would indicate the end of the list). If we reach that point, the
item is not in the Linked List. Otherwise we would stop when we hit the target value. It seems like
a fair spot to use either iterative or recursive as there is a clear set of base cases (find target value or find None).


## Draw/model out how to traverse through a linked list in order to find the maximum value in the linked list.

Similarly to the above, given Linked Lists are not inherently sorted, I think we would traverse through the list
in much the same manor, checking the current value and then moving onto the next via the pointer until we reached
None. We could also keep a temporary variable that is updated each time we move onto a new node IF the value
of the node is greater than the current instance. When we get to the end, we would have the highest value.




