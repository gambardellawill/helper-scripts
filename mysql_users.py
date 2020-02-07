# -*- coding: utf-8 -*-

import argparse
import mysql.connector as mysql

parser = argparse.ArgumentParser('Helper script that prints all available users on a MySQL database.')

parser.add_argument('-y', '--host', dest='host', type=str, required=True, help='')
parser.add_argument('-p', '--password', dest='password', type=str, required=True, help='')
parser.add_argument('-u', '--user', dest='user', type=str, required=True, help='')
# parser.add_argument('-s', '--schema', type=str, required=False)


if __name__ == "__main__":
    args = parser.parse_args()

    db = mysql.connect(
        host=args.host,
        user=args.user,
        password=args.password
    )

    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("SELECT User FROM mysql.user")
    except:
        print("Unable to run commands. Please check if your user has the right privileges")
        exit(1)

    rows = cursor.fetchall()

    db.disconnect()

    users = []

    for row in rows:
        print(row.get('User').decode('utf-8'))
    