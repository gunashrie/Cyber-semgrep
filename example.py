import sqlite3
from html import escape  # Import escape function to properly encode output
 
# Hardcoded secret
api_key = "secret_value"  # This line will be flagged by Semgrep as a warning
 
def get_user(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Unsanitized SQL query - this should trigger a blocking issue (ERROR)
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # This line will be flagged by Semgrep as an error
 
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
 
    # Proper output encoding: Use html.escape to prevent XSS vulnerability
    safe_result = [escape(str(record)) for record in result]  # Safely encode each record in the result
    return safe_result
 
# Example of output encoding
user = get_user("admin")
 
# Use properly encoded data for output to prevent XSS
print(user)  # This line should be flagged by Semgrep for missing output encoding (before fix)

