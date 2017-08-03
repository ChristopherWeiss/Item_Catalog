from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Item 
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)



# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def homepage():
	all_items = session.query(Item.category).distinct()
	return render_template('homepage.html', items = all_items)

@app.route('/catalog/<category>/items')
def displayCategory(category):
	categoryItems = session.query(Item).filter_by(category = category)
	return render_template('displayCategory.html', items=categoryItems, category = category)
@app.route('/catalog/<category>/<itemname>')
def displayItem(category, itemname):
	item = session.query(Item).filter_by(category = category).filter_by(name=itemname).one()
	return render_template('displayItem.html', item = item)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)