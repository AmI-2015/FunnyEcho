'''
Created on 06/mag/2015

@author: Fulvio
'''

import mysql.connector

def insertTranslation(before, after):
    sql = "INSERT INTO translation (original, modified) VALUES (%s, %s)"
    
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='funnyecho')
    
    cursor = conn.cursor()
    
    cursor.execute( sql, (before, after) )
    lastid = cursor.lastrowid
    
    cursor.close()
    conn.commit()
    conn.close()
    return lastid


def getAllTranslations():
    sql = "SELECT id, original, modified FROM translation"
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='funnyecho')
    cursor = conn.cursor()
    cursor.execute(sql)
    
    translations = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return translations

def getTranslation(txtid):
    sql = "SELECT id, original, modified FROM translation WHERE id=%s"
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='funnyecho')
    cursor = conn.cursor()
    cursor.execute(sql, (txtid,) )
    
    translations = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return translations


if __name__ == '__main__':
    insertTranslation("a", "b")
    
    translations = getAllTranslations()
    print translations