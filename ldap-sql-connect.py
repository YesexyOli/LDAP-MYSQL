#!/usr/bin/python


import ldap
import ldap.modlist
import mysql.connector

load = 0
mydb = 0

def main():
    try:
        global load
        load = ldap.initialize("ldap://127.0.0.1")                                           #Modifier l'ip LDAP
        load.simple_bind_s("cn=admin,dc=roederer,dc=fr", "root")
        print ("LDAP connected! Connexion a la BDD...")
    except ldap.LDAPError as e:
        print (e)
    try:
        global mydb
        mydb = mysql.connector.connect(
            host="",
            user="stagiaire",
            passwd=""
        )
        print("BDD connected!", mydb)
    except:
        print("Erreur BDD (verifiez l'host, le user, ou le passwd...)")


main()