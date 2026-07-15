# Day 29: Debugging & Logging 
# Goal: Find and fix errors like a professional.

# Concept: Move away from print() statements. Use the logging module to keep a record of what your program is doing at different severity levels.

"""
Day 29: Debugging & Logging
Concept: Logging allows you to track code execution. 
Levels: DEBUG (info for devs), INFO (normal ops), WARNING, ERROR, CRITICAL.

Why it matters: When your program crashes on a user's machine, 
you can check the log file to see exactly what happened.
"""
import logging

# Configure the logger to save to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data):
    logging.info(f"Processing data: {data}")
    try:
        result = 10 / data
        logging.info("Calculation successful.")
    except ZeroDivisionError:
        logging.error("Failed: Division by zero attempted!")

process_data(0)
# Check 'app.log' in your folder to see the generated record!