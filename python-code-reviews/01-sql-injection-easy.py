"""
Review 01: SQL Injection Detection (Easy)
Scenario: Simple parameterized query check
"""

import sqlite3

class DatabaseQuery:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def get_user_by_id(self, user_id):
        """
        VULNERABLE: String concatenation in SQL query
        """
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def get_user_by_name(self, name):
        """
        SECURE: Parameterized query using placeholder
        """
        query = "SELECT * FROM users WHERE name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()
    
    def delete_user(self, user_id):
        """
        VULNERABLE: Direct string formatting
        """
        query = f"DELETE FROM users WHERE id = {user_id}"
        self.cursor.execute(query)
        self.conn.commit()
    
    def close(self):
        self.conn.close()


# Issue: get_user_by_id() allows SQL injection
# Recommendation: Use parameterized queries for all user input
