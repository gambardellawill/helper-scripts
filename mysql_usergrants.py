#!/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
import argparse
import mysql.connector as mysql

parser = argparse.ArgumentParser('Helper script that retrieves grants and privileges for a specific user on a MySQL database.')

parser.add_argument('-y', '--host', dest='db_host', type=str, required=True, help='')
parser.add_argument('-p', '--password', dest='db_password', type=str, required=True, help='')
parser.add_argument('-u', '--user', dest='db_user', type=str, required=True, help='')
# parser.add_argument('-s', '--schema', type=str, required=False)


if __name__ == "__main__":
    args = parser.parse_args()

    user_under_analysis = sys.stdin.buffer.readline().decode('utf-8').replace('\n', '')

    db = mysql.connect(
        host=args.db_host,
        user=args.db_user,
        password=args.db_password
    )

    cursor = db.cursor(raw=True)

    try:
        cursor.execute("SHOW GRANTS FOR \'{}\'@\'%\'".format(user_under_analysis))
    except Exception as e:
        print(e)
        exit(1)

    rows = cursor.fetchall()

    db.disconnect()

    # PRINT SECTION
    print('{}:'.format(user_under_analysis))
    for row in rows:
        print(row[0].decode('utf-8'))