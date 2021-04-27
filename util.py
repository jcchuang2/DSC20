"""
DSC 20 Final Project Utility File

Please copy and paste your Stack and Queue implementation from Lab 10.
"""


class Collection:
    """
    A class to abstract the common functionalities of Stack and Queue.
    This class should not be initialized directly.
    """

    def __init__(self):
        """ Constructor. """
        # YOUR CODE GOES HERE #
        self.items = []
        self.num_items = 0

    def size(self):
        """ Get the number of items stored. """
        # YOUR CODE GOES HERE #
        return self.num_items

    def is_empty(self):
        """ Check whether the collection is empty. """
        # YOUR CODE GOES HERE #
        if self.num_items == 0:
            return True
        return False

    def clear(self):
        """ Remove all items in the collection. """
        # YOUR CODE GOES HERE #
        self.items = []
        self.num_items = 0


class Stack(Collection):
    """
    Stack class.
    """

    def push(self, item):
        """ Push `item` to the stack. """
        # YOUR CODE GOES HERE #
        if item == None:
            raise ValueError('item cannot be None')
        else:
            self.items.append(item)
            self.num_items += 1

    def pop(self):
        """ Pop the top item from the stack. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        """ Peek the top item. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def __str__(self):
        """ Return the string representation of the stack. """
        # YOUR CODE GOES HERE #
        if len(self.items) == 0:
            return "(bottom) (top)"
        else:
            str_item_list = [str(i) for i in self.items]
            return "(bottom) " + " -- ".join(str_item_list) + " (top)"


class Queue(Collection):
    """
    Queue class.
    """

    def enqueue(self, item):
        """ Enqueue `item` to the queue. """
        # YOUR CODE GOES HERE #
        if item == None:
            raise ValueError('item cannot be None')
        else:
            self.items.append(item)
            self.num_items += 1

    def dequeue(self):
        """ Dequeue the front item from the queue. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        else:
            self.num_items -= 1
            return self.items.pop(0)

    def peek(self):
        """ Peek the front item. """
        # YOUR CODE GOES HERE #
        if self.is_empty():
            return None
        return self.items[0]

    def __str__(self):
        """ Return the string representation of the queue. """
        # YOUR CODE GOES HERE #
        if len(self.items) == 0:
            return "(front) (rear)"
        else:
            str_item_list = [str(i) for i in self.items]
            return "(front) " + " -- ".join(str_item_list) + " (rear)"
