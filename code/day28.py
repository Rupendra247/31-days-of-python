# Day 28: Virtual Environments 
# Goal: Isolate your project dependencies.

# Concept: Every project needs its own "space" so that libraries from one project don't conflict with another.

"""
Day 28: Virtual Environments
Concept: Virtual environments (venv) create a folder that stores specific 
versions of libraries for your project.

Commands to use in your terminal:
1. Create: python -m venv venv
2. Activate (Windows): venv\Scripts\activate
3. Activate (Mac/Linux): source venv/bin/activate
4. Install package: pip install requests

Why it matters: It prevents 'dependency hell' where updating one project 
breaks another. Always use a venv for every project in your GitHub!
"""

# Example of using a package inside your virtual environment
# import requests 
# response = requests.get('https://api.github.com')