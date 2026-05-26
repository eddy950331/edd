 Import os

import subprocess

import hashlib

import sqlite3

import requests

import json

import ast

import secrets


# =========================

# Hardcoded Secrets

# =========================

# FIX: Use environment variables instead of hardcoding sensitive data in source code.

PASSWORD = os.getenv("APP_PASSWORD", "default_fallback_if_needed")

API_KEY = os.getenv("APP_API_KEY", "")


users = []


# =========================

# SQL Injection

# =========================

def login(username, password):

# In a real app, hash the incoming password and compare it to a hashed DB entry.

conn = sqlite3.connect("test.db")

cursor = conn.cursor()


# FIX: Use parameterized queries (?) to prevent SQL injection.

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, password))

result = cursor.fetchone()

conn.close()

return bool(result)


# =========================

# Command Injection

# =========================

def ping_host(ip):

# FIX: Use subprocess.run with a list of arguments to avoid shell injection.

# Note: Further validation on the 'ip' string is still recommended.

subprocess.run(["ping", "-c", "1", ip], capture_output=True)


# =========================

# Unsafe subprocess

# =========================

def run_command(cmd_list):

# FIX: Removed shell=True. Expects a list like ["ls", "-l"] instead of a string.

subprocess.run(cmd_list, capture_output=True)


# =========================

# Weak Hash Algorithm

# =========================

def hash_password(password):

# FIX: Upgraded from MD5 to SHA-256.

# Note: For real user passwords, use a slow hashing algorithm like bcrypt or Argon2.

return hashlib.sha256(password.encode()).hexdigest()


# =========================

# Predictable Random

# =========================

def generate_token():

# FIX: Use the 'secrets' module for cryptographically secure random numbers.

return secrets.randbelow(9000) + 1000 # Generates between 1000 and 9999


# =========================

# Dangerous Pickle Load

# =========================

def load_user_data(file):

# FIX: Switched from pickle to JSON. Unpickling untrusted data can lead to Remote Code Execution.

with open(file, "r") as f:

return json.load(f)


# =========================

# Division by Zero

# =========================

def divide(a, b):

# FIX: Added a safeguard to prevent ZeroDivisionError crashes.

if b == 0:

raise ValueError("Cannot divide by zero.")

return a / b


# =========================

# Unused Variable & Duplicate Code

# =========================

# FIX: Removed the confusing 'calculate()' function and deleted 'add_numbers2'.

def add_numbers(a, b):

result = a + b

return result


# =========================

# Infinite Recursion

# =========================

def recursive(count=0):

# FIX: Added a base case to prevent the recursion from running infinitely.

if count >= 5:

return count

return recursive(count + 1)


# =========================

# Bare Except

# =========================

def safe_exception():

# FIX: Catch a specific exception instead of blindly catching everything.

try:

x = 1 / 0

except ZeroDivisionError:

pass


# =========================

# Hardcoded URL

# =========================

def call_api():

# FIX: Upgraded HTTP to HTTPS to prevent man-in-the-middle attacks.

url = "https://secure-api.com/data"

try:

response = requests.get(url, timeout=5)

response.raise_for_status()

return response.text

except requests.RequestException:

return None


# =========================

# File Resource Leak

# =========================

def read_file():

# FIX: Used a context manager ('with' statement) to ensure the file is closed automatically.

with open("test.txt", "r") as f:

return f.read()


# =========================

# Unsafe Eval

# =========================

def calculate_input(user_input):

# FIX: Used ast.literal_eval to safely evaluate Python data structures instead of arbitrary code.

try:

return ast.literal_eval(user_input)

except (ValueError, SyntaxError):

return None


# =========================

# Global Variable Abuse

# =========================

# FIX: Avoided globals. Passed the state as a parameter and returned the modified state.

def increase(current_count):

return current_count + 1


# =========================

# Long Function

# =========================

def optimized_function():

# FIX: Replaced repetitive lines of code with a simple loop.

for i in range(1, 21):

print(f"line{i}")


# =========================

# Unreachable Code

# =========================

def test_return():

# FIX: Removed the print statement that existed after the return statement.

return True


# =========================

# None Comparison

# =========================

def check_none(value):

# FIX: Used 'is' instead of '==' when comparing to None. Simplified the logic.

return value is None


# =========================

# Mutable Default Argument

# =========================

def append_item(item, items=None):

# FIX: Default argument is now None. The list is initialized inside the function.

if items is None:

items = []

items.append(item)

return items


# =========================

# Main

# =========================

if __name__ == "__main__":

# Removed the debug_mode and print_credentials functions entirely as they leaked sensitive info.

print(hash_password("mypassword"))

print(generate_token())

safe_exception()

print(calculate_input("2 + 2")) 
