"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()  # Using a set for O(1) average-case lookups
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Justification:
# A set is the best choice here because it allows O(1) average insert and lookup time.
# We only need to know if a value has been seen before, so the hash-based properties
# of sets make this task efficient. Runtime is O(n), where n is the length of product_ids.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()  # Deque gives O(1) append and popleft

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None

# Justification:
# A queue (implemented with deque) is ideal because tasks are processed in FIFO order.
# Deque operations append() and popleft() both run in O(1) time, unlike lists where removing
# from the front would cost O(n). This makes deque the efficient choice here.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.unique_values = set()  # Set automatically handles uniqueness

    def add(self, value):
        self.unique_values.add(value)

    def get_unique_count(self):
        return len(self.unique_values)

# Justification:
# A set is the best fit since it only stores unique elements and avoids duplicates automatically.
# Insertions are O(1) average case, and getting the unique count is O(1) because len() is constant time.
