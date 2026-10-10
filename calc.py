import sqlite3

def average(nums):
    return sum(nums) / len(nums)

def find_user(db, name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return db.execute(query).fetchall()
