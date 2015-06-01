#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Database connection using pandas
"""

from recommender import app
from sqlalchemy import create_engine
import pandas as pd



def coxn_str():
    server = app.config['DB_SERVER']
    username = app.config['DB_SERVER']
    password = app.config['DB_SERVER']
    database = app.config['DB_SERVER']
    port = app.config['DB_PORT']

    return 'postgresql://%s:%s@%S:%s/%s' % (username, password, server, port, database)

def fetch_data(query):
    engine = create_engine(coxn_str())