## Draw/model out enqueuing into a queue that uses a linked list as its underlying storage structure.

Queues use a first in, first out system. The process for enqueuing woudld involve the following steps:
1.) Checking if the linked list has a head
2.) If yes, set the current head's previous as the new value, then set the new head as the new value
    with the previous head as the next value
3.) If no, set both the head and tail as the new value with next and previous as None.

## Draw/model out dequeuing from a queue that uses a linked list as its underlying storage structure.

To dequeue, we need to return the current head, remove it and set the head's next value to the new head.
We would set the current head to a temporary variable, set the current head's next value to the head of
the list and then return the temporary variable. 
