import hashlib
import os
import random
import secrets  # 改用密碼學安全的隨機數
import sqlite3
import requests

# 將 Hardcoded 敏感資訊移出，改為從環境變數讀取
PASSWORD = os.getenv("APP_PASSWORD", "default_secure_fallback")
API_KEY = os.getenv("APP_API_KEY", "default_secret_fallback")

users = []


# =========================
# SQL Injection -> 使用參數化查詢
# =========================
def login(username, password):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # 使用 ? 占位符進行參數化查詢，防止 SQL 注入
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    conn.close()

    return bool(result)


# =========================
# Command Injection -> 使用安全列表或 subprocess 代替 os.system
# =========================
def ping_host(ip):
    # 這裡只接受基本的 IP 格式檢查會更安全，並避免 shell=True
    import shlex
    import subprocess

    safe_ip = shlex.quote(ip)  # 清洗輸入
    subprocess.run(["ping", "-c", "1", safe_ip], check=False)


# =========================
# Unsafe subprocess -> 禁用 shell=True
# =========================
def run_command(cmd):
    # 傳入 List 並拿掉 shell=True
    if isinstance(cmd, str):
        import shlex

        cmd = shlex.split(cmd)
    subprocess.run(cmd, check=True)


# =========================
# Weak Hash Algorithm -> 改用 SHA-256 或 bcrypt
# =========================
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# =========================
# Predictable Random -> 改用 secrets 模組
# =========================
def generate_token():
    # secrets 適用於生成 Token 或密碼
    return secrets.randbelow(9000) + 1000


# =========================
# Dangerous Pickle Load -> 改用安全的安全格式如 JSON
# =========================
def load_user_data(file):
    import json

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


# =========================
# Division by Zero -> 加上防禦性判斷
# =========================
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# =========================
# Unused Variable -> 移除 z 與 x 的重構
# =========================
def calculate():
    x = 100
    y = 200
    return x + y


# =========================
# Duplicate Code -> 合併重複程式碼
# =========================
def add_numbers(a, b):
    result = a + b
    print("Result:", result)
    return result


# add_numbers2 直接移除，或讓它調用 add_numbers
def add_numbers2(a, b):
    return add_numbers(a, b)


# =========================
# Infinite Recursion -> 加上終止條件
# =========================
def recursive(depth=0):
    if depth > 10:
        return True
    return recursive(depth + 1)


# =========================
# Bare Except -> 指定 Exception
# =========================
def unsafe_exception():
    try:
        _ = 1 / 0
    except ZeroDivisionError as e:
        print(f"Logged Error: {e}")


# =========================
# Debug Code -> 使用 logging 模組，移除敏感資訊
# =========================
import logging

logging.basicConfig(level=logging.INFO)


def debug_mode():
    logging.debug("DEBUG MODE ENABLED")


# =========================
# Hardcoded URL -> 建議改用 https 確保傳輸安全
# =========================
def call_api():
    url = "https://secure-api.com/data"  # 使用 HTTPS
    response = requests.get(url, timeout=5)  # 加上 timeout 防止掛起
    return response.text


# =========================
# File Resource Leak -> 使用 with context manager
# =========================
def read_file():
    with open("test.txt", "r", encoding="utf-8") as f:
        data = f.read()
    return data


# =========================
# Unsafe Eval -> 禁用 eval，改用 safe_eval 或 ast.literal_eval
# =========================
def calculate_input(user_input):
    import ast

    # 僅允許安全的字面量運算，防止惡意指令執行
    try:
        return ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        return None


# =========================
# Global Variable Abuse -> 盡量避免，或透過類別封裝
# =========================
class Counter:

    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1


counter = Counter()


# =========================
# Long Function -> 拆分或精簡程式碼
# =========================
def huge_function():
    # 實際開發中應將長邏輯拆分成多個子函數
    for i in range(1, 21):
        print(f"line{i}")


# =========================
# Unreachable Code -> 移除死碼
# =========================
def test_return():
    return True


# =========================
# None Comparison -> 使用 is
# =========================
def check_none(value):
    return value is None


# =========================
# Mutable Default Argument -> 使用 None 初始化
# =========================
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


# =========================
# Sensitive Information Leak -> 移除 Hardcoded 密碼
# =========================
def print_credentials():
    # 不要直接印出敏感密碼，通常只作日誌遮罩處理
    username = "admin"
    print(username)


# =========================
# Main
# =========================
if __name__ == "__main__":
    print(login("admin", "admin"))
    ping_host("127.0.0.1")
    print(hash_password("mypassword"))
    print(generate_token())
    unsafe_exception()
    debug_mode()
    huge_function()
