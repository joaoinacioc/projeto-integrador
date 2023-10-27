import json
from flask import Flask, render_template
from services.user_service import insert_logic


def index():
    return render_template('home.html')

#def create():

def cliente():
    return render_template('cliente.html')
#    create_logic()


# insert data into table.
def insert():
    insert_logic()
