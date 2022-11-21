import numpy as np
import pyodbc

class logAnalysis:
    data = pd.read_csv(r " /logs/2022-01-01.log.csv")
    df = pd.dataFrame(data)
    
    #connect to sql server
    def connectsql():
        
        conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MOBELIUM\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')
        conn = conn.cursor()
    
    #Create Table
        cursor.execute('''
                     CREATE TABLE logdata (
                     timestamp int,
                     user char(10),
                     app char(10),
                     metric1 int
                     )
                     ''')
    def insertion():
        for row in df.itertuples():
            cursor.execute('''
                             INSERT INTO logdata(timestamp, user, app, metric1)
                             VALUES (?,?,?)
                             ''',
                             row.timestamp,
                             row.user,
                             row.app,
                             row.metric1
                             )
        conn.commit()   
    
    def operation():
        cursor.execute('''
                        SELECT * FROM logdata WHERE (timestamp between '2018-01-01 00:00:00' and '2018-01-05 00:00:00') GROUP BY timestamp
                        ''')
        cursor.execute('''
                        SEELCT * FROM logdata WHERE (timestamp between '2018-01-01 00:00:00' and '2018-01-05 00:00:00') and app = app1 GROUP BY timestamp
                        ''')                
        cursor.execute('''
                        SEELCT * FROM logdata WHERE (timestamp between '2018-01-01 00:00:00' and '2018-01-05 00:00:00') and app = app1 GROUP BY timestamp
                        ''')
                        
query = logAnalysis()
query.connectsql()
query.insertion()
query.operation()
