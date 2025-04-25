# Example Python file with potential security issues

import sqlite3

# Hardcoded secret
api_key = "secret_value"  # This line will be flagged by Semgrep

def get_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # Unsanitized SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # This line will be flagged by Semgrep
    cursor.execute(query)
    
    result = cursor.fetchall()
    conn.close()
    return result

user = get_user("admin")
print(user)
