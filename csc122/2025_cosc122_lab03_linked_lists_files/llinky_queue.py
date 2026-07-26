"""Queue data structure implemented with a linked list.

Check out the comments/code at the end of this module
for how to run the provided doctests.

"""

import doctest
import os

os.environ['TERM'] = 'linux'  # Suppress ^[[?1034h


class Node:
    """
    A simple node for a linked list.

    >>> n1 = Node('a')
    >>> print(n1.item)
    a
    >>> print(n1.next_node)
    None
    >>> n2 = Node('b')
    >>> n1.next_node = n2
    >>> print(n1.next_node.item)
    b
    >>> print(n2.next_node)
    None
    >>> print(n1.next_node.next_node)
    None
    """

    def __init__(self, item):
        self.item = item
        self.next_node = None


class Queue:
    """ Implements a Queue using a Linked List"
    >>> q = Queue()
    >>> len(q)
    0
    >>> print(q)
    Queue: head/front -> None
    >>> result = q.dequeue()
    Traceback (most recent call last):
    ...
    IndexError: Can't dequeue from empty queue.
    >>> print(len(q))
    0
    >>> result2 = q.dequeue()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    IndexError: Can't dequeue from empty queue.
    >>> q.enqueue('a')
    >>> print(q)
    Queue: head/front -> a -> None
    >>> q.head.item
    'a'
    >>> print(q.head.next_node)
    None
    >>> len(q)
    1
    >>> q.enqueue('b')
    >>> print(q)
    Queue: head/front -> a -> b -> None
    >>> q.head.next_node.item
    'b'
    >>> q.enqueue('c')
    >>> print(q)
    Queue: head/front -> a -> b -> c -> None
    >>> len(q)
    3
    >>> q.dequeue()
    'a'
    >>> print(q)
    Queue: head/front -> b -> c -> None
    """

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        """Add an item onto the tail of the queue.
        Note: The front of the queue is stored at the head of the list
        so adding to the rear requires finding the end of the list
        """
        # ---start student section---
        pass
        # ===end student section===

    def dequeue(self):
        """Remove an item from the head of the queue and return it.
        If queue is empty you should raise an IndexError as per
        the comment below."""
        # use the following line to raise error when queue is empty
        # raise IndexError("Can't dequeue from empty queue.")
        # ---start student section---
        pass
        # ===end student section===

    def is_empty(self):
        """ returns True if the queue is empty """
        # ---start student section---
        pass
        # ===end student section===

    def __len__(self):
        """ Returns the length --- calling len(q) will invoke this method """
        # ---start student section---
        pass
        # ===end student section===

    def __str__(self):
        """Returns a string representation of the list for the queue starting
        from the beginning of the list. Items are separated by ->
        and ending with -> None
        eg, Queue: head/front -> a -> b -> None
        See doctests in class docstring
        """
        result = 'Queue: head/front'
        current = self.head
        while current is not None:
            result += ' -> ' + str(current.item)
            current = current.next_node
        result += ' -> None'
        return result


def run_tests():
    """ Runs some tests. Feel free to add more... """
    # change to False to get less doctest output
    with_verbose = True

    # Can enter an infinite loop if your Queue isn't implemented correctly
    result = doctest.testmod()
    if with_verbose:
        print(result)


if __name__ == '__main__':
    run_tests()
