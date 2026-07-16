# Day 15: File I/O
# Goal: Read from and write to external files.

# Concept: Using the with statement (Context Manager) is the safest way to handle files because it automatically closes the file, even if an error occurs.

# Day 15: File I/O
# 'w' mode writes (overwrites), 'a' mode appends, 'r' mode reads.

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Day 15: Learning File I/O.\n")
    file.write("Python makes file handling simple!")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print("--- File Content ---")
    print(content)