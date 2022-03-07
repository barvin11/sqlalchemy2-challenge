# %matplotlib inline
# from matplotlib import style
# style.use('fivethirtyeight')
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import flask
from flask import Flask, jsonify
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine,reflect = True)
# View all of the classes that automap found
base.classes.keys()
# Save references to each table
Measurement = base.classes.measurement
Station = base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
        f"Pages to visit: <br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>/<end> <br/>"
    
    )   
@app.route("/api/v1.0/precipitation")
def precipitation():
    one_year_prior = dt.date(2017,8,23) - dt.timedelta(days = 365)
    date_precip = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= one_year_prior,Measurement.prcp != None).\
    order_by(Measurement.date).all()   
    return jsonify(dict(date_precip))

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    list_stations = session.query(Station.station).all()
    return jsonify(list(list_stations))

@app.route("/api/v1.0/tobs")
def tobs():
    one_year_prior = dt.date(2017,8,23) - dt.timedelta(days = 365)
    date_tobs = session.query(measurement.tobs).\
    filter(measurement.date >= one_year_prior,measurement.station == 'USC00519281').\
    order_by(measurement.date).all()
    return jsonify(list(date_tobs))

#@app.route
if __name__ == '__main__':
    app.run(debug = True)