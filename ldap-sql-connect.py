#!/usr/bin/python

import time
import ldap
import ldap.modlist
import mysql.connector


row = 0
load = 0
mydb = 0

def add_user(row, a):

    modlist = {
        "objectClass": ["inetOrgPerson", "posixAccount", "shadowAccount"],
        "uid": ["test"],
        "createTimestamp": ["20190426085007Z"],
        "displayName": ["Moreno Cosani"],
        "userPassword": ["root"],
        "uidNumber": ["5000"],
        "gidNumber": ["10000"],
        "loginShell": ["/bin/bash"],
    }
    dn = "uid=test,ou=People,dc=roederer,dc=fr"                                            #MODIFIER LE DN (chemin)

    try:
        load.add_s(dn, ldap.modlist.addModlist(modlist))
        print("Utilisateur added")
    except:
        print("Erreur, verifiez votre dn, et controler que son uid n'existe pas deja")
        return 84

def main():
    try:
        global load
        global row
        print("Connexion au LDAP...")
        time.sleep(1)
        load = ldap.initialize("ldap://127.0.0.1")                      #Modifier l'ip LDAP
        load.simple_bind_s("cn=admin,dc=roederer,dc=fr", "root")
        print ("LDAP connected!\nConnexion a la BDD...")
        time.sleep(1)
    except ldap.LDAPError as e:
        print (e)
    try:
        global mydb
        mydb = mysql.connector.connect(
            host="10.10.45.2",
            user="stagiaire",
            passwd="DjfU78Fj76f65",
            db="RoedererEntreprises"
        )
        print("BDD connected!", mydb)
        sql_select_Query = "SELECT * FROM RoedererEntreprises.SBYN_ENTERPRISE_DETAIL INNER JOIN TMP_SITEWEB_USER ON SBYN_ENTERPRISE_DETAIL.LID = TMP_SITEWEB_USER.LID WHERE SBYN_ENTERPRISE_DETAIL.GESTIONNAIRE = 'ROEDERER'"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        a=0
        for row in records:
            a = a + 1
            print("------")
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[6])
        add_user(row, a)

        print("Total de rows : ", cursor.rowcount)
    except:
        print("Erreur BDD (verifiez l'host, le user, ou le passwd...)")


main()