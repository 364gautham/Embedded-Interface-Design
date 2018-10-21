import sqlite3 as sq
import datetime
import sys
import signal

def signal_handler(sig, frame):
    conn.close()
    print "Signal handler\n"
    sys.exit(0)

conn = sq.connect('project2.db')

conn.execute("INSERT INTO SENSOR_VAL (TEMP_C, TEMP_F, HUMID, TIMESTAMP) \
    VALUES (100, 200, 300, '"+str(datetime.datetime.now())+"')");
    
conn.commit()
c = conn.cursor()

cursor = c.execute("SELECT TEMP_C, TEMP_F, HUMID, TIMESTAMP FROM SENSOR_VAL")
for row in cursor:
    print row[0], row[1], row[2], row[3]

c.execute("SELECT MAX(TEMP_F) FROM SENSOR_VAL AS MAX_HUMID")
for l in c.fetchone():
    print l

c.execute("SELECT MIN(TEMP_C) FROM SENSOR_VAL AS MIN_TEMPC")
for element in c.fetchone():
    print element

c.execute("SELECT * FROM SENSOR_VAL WHERE HUMID IS (SELECT MAX(HUMID) FROM SENSOR_VAL)")
element = c.fetchone()
print element[0], element[1], element[2], element[3]

signal.signal(signal.SIGINT, signal_handler)
while(1):
       pass 
conn.close()
