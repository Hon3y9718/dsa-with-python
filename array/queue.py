## Queue is a list with limitations on how it can be used. It is a FIFO (First In First Out) data structure.

class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self._items = []

    def push(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        # Removing from the front of a list
        return self._items.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def print(self):
        """Print the current state of the queue."""
        print("Queue:", self._items)


# --- Example Usage ---
q = Queue()

q.push("Alice")
q.print()  
q.push("Bob")
q.print()  
q.push("Charlie")
q.print()  

print("Front item:", q.peek())      # Output: Alice
q.print()  
print("Dequeued:", q.pop())         # Output: Alice
q.print()  
print("Dequeued:", q.pop())         # Output: Bob
q.print()  
print("Queue size:", q.size())      # Output: 1
q.print()  