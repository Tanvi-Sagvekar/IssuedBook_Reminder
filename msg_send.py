import datetime
import pywhatkit
import pywhatkit as pwt
import mysql
import mysql.connector

#Function to send Whatsapp message 
def send_whatsapp_message(mobile_number,message):
    #Ensure phone nubee includes country code
    #if not all(phone_number.startswith('+') for phone_number in phone_numbers):
    if not mobile_number.startswith('+'):
        mobile_number='+91' + mobile_number
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
        pywhatkit.sendwhatmsg(mobile_number, message, send_time.hour, send_time.minute)
        #pwt.sendwhatmsg(mobile_number, message, send_time.hour, send_time.minute)
        #pywhatkit to send whatsapp message
        #pwt.sendwhatmsg(phone_number,message,datetime.datetime.now().hour,datetime.datetime.now().minute + 1)
        #pwt.sendwhats_multiple(phone_numbers,message,datetime.datetime.now().hour,datetime.datetime.now().minute + 1)
#today date 
today_date=datetime.datetime.today().strftime('%Y-%m-%d')

#Connect to database
conn=mysql.connector.connect(
    host='localhost',
    user="root",
    password="shravani@2008",
    database='booktable')
try:
    with conn.cursor() as cursor:
        #Retrive phone nubers of all students
        cursor.execute("SELECT mobile_number FROM issued_books where return_date = %s",(today_date,))
        rows=cursor.fetchall()
        if rows:
            #phone_numbers= [row[0] for row in phone_numbers]
            #Message to be sent to all students
            msg_to_all_students = "This is a reminder from library to you about submission of book."
            for row in rows:
                #msg = f"Reminder:{row[0]}"
                send_whatsapp_message(row[0], msg_to_all_students)
                print("WhatApp message sent:",msg_to_all_students)
        
       


finally:
    conn.close()

