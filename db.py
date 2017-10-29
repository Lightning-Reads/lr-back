import mysql.connector
from mysql.connector import errorcode



def db_connect():
    try:
        global cnx
        cnx = mysql.connector.connect(user='textanalysis', password='textanalysissis',
                                  host='2fast2furiouz.no-ip.info',
                                  database='textanalysis')                    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")

        else:
            print(err)
            
def db_counterup(categoryselected, mediatype):
    print categoryselected
    cursor = cnx.cursor(dictionary=True)
    #result = cursor.execute('SELECT * FROM core WHERE category=?', categoryselected)
    query = "SELECT * FROM core WHERE category = %s LIMIT 1"
    cursor.execute(query, (categoryselected,))
    result = cursor.fetchone()

    if result is not None:
        print "%s, %s, %s" % (result["pic"], result["wiki"], result["id"], )
        resid = result["id"]
        
        newmediatypeval = result[mediatype] + 1
        query = "UPDATE core SET " + mediatype + " = %s WHERE id = %s"
        
        cursor.execute(query, (newmediatypeval,resid))
    else:
        query = "INSERT INTO core (category) VALUES (%s)"
        cursor.execute(query, (categoryselected,))
    cnx.commit()
    return "OK"
        
def db_counterdown(categoryselected, mediatype):
    print categoryselected
    cursor = cnx.cursor(dictionary=True)
    #result = cursor.execute('SELECT * FROM core WHERE category=?', categoryselected)
    query = "SELECT * FROM core WHERE category = %s LIMIT 1"
    cursor.execute(query, (categoryselected,))
    result = cursor.fetchone()

    if result is not None:
        print "%s, %s, %s" % (result["pic"], result["wiki"], result["id"], )
        resid = result["id"]
        
        newmediatypeval = result[mediatype] - 1
        query = "UPDATE core SET " + mediatype + " = %s WHERE id = %s"
        cursor.execute(query, (newmediatypeval,resid))
    else:
        query = "INSERT INTO core (category) VALUES (%s)"
        cursor.execute(query, (categoryselected,))
    cnx.commit()

def db_getAllCounter(categoryselected):
    print categoryselected
    cursor = cnx.cursor(dictionary=True)
    #result = cursor.execute('SELECT * FROM core WHERE category=?', categoryselected)
    query = "SELECT * FROM core WHERE category = %s LIMIT 1"
    cursor.execute(query, (categoryselected,))
    result = cursor.fetchone()

    if result is not None:
       return result
            
db_connect()
#db_counterup("test", "pic")
#db_addcategory("test")

    