# Day 27: Generators 
# Goal: Manage memory efficiently when dealing with massive datasets.

# Concept: Unlike a list that loads everything into RAM, a generator yields one item at a time using the yield keyword

"""
Day 27: Generators
Concept: Generators use the 'yield' keyword to return data one piece at a time.
Why it matters: If you need to process a 10GB file, a generator won't crash your 
computer because it only holds one line in memory at a time.
"""

def large_number_generator(n):
    # This acts like a standard loop, but 'yields' values one by one
    for i in range(n):
        yield i ** 2

# Usage: This will only calculate the next square when requested
gen = large_number_generator(1000000)

print(next(gen)) # Returns 0
print(next(gen)) # Returns 1
# This is incredibly memory-efficient for large data streams.