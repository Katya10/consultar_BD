#!/usr/bin/env python

#Este script sirva para leer datos de la base que conectamos local
#o en un serivor


from __future__ import print_function
from xmlrpclib import ServerProxy

SERVER = 'localhost'
DATABASE = 'base_katya'
USERNAME = 'salas-rodriguez@hotmail.com'
PASSWORD = 'agosto1993'

server = ServerProxy('http://localhost:8069/xmlrpc/common')
user_id = server.login(DATABASE, USERNAME, PASSWORD)

server = ServerProxy('http://localhost:8069/xmlrpc/object')
user_ids = server.execute(
    DATABASE, user_id, PASSWORD,
    'product.template', 'search', []
)

users = server.execute(
    DATABASE, user_id, PASSWORD,
    'product.template', 'read', user_ids, []
)

for user in users:
    print(user['id'], user['name'], user['categ_id'])