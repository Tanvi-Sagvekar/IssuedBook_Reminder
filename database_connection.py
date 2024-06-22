import mysql
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL Database
conn = mysql.connector.connect(host='localhost', user='root', password='shravani@2008', database='booktable')
cursor = conn.cursor()

def issue_book(name, book_name, mobile_number):
    issue_date = datetime.now().strftime('%Y-%m-%d')  # Get current date as issue date
    return_date = (datetime.now() + timedelta(days=0)).strftime('%Y-%m-%d')  # Calculate return date (14 days later)
    
    # Insert data into the database
    sql = "INSERT INTO issued_books (name, book_name, mobile_number, issue_date, return_date) VALUES (%s, %s, %s, %s, %s)"
    val = (name, book_name, mobile_number, issue_date, return_date)
    cursor.execute(sql, val)
    conn.commit()
    
    print("Book issued successfully!")
    print("Issue Date:", issue_date)
    print("Return Date:", return_date)

# Example usage:
name = input("Enter your name: ")
book_name = input("Enter the name of the book: ")
mobile_number = input("Enter your mobile number: ")

issue_book(name, book_name, mobile_number)

# Close the database connection
conn.close()
