#setup all the necessary imports
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flash import Flask, jsonify

#make the engine from the other notbook for this assignment
#basically we are pulling straight from the other notebook here
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)
session

#do the Flask setup, which is necessary to do in a python file
#instead of a .ipynb in order to run
app = Flask(__name__)
@app.route('/')
def home:
    return(
    f"Welcome to David's Climate Analysis API!"
    f"All Available Routes:"
    f"/api/v1.0/precipitation"
    f"/api/v1.0/precipitation"
    f"/api/v1.0/stations"
    f"/api/v1.0/tobs"
    f"/api/v1.0/<start>"
    f"/api/v1.0/<start>/<end>"
    )

@app.route('/api/v1.0/precipitation')
def precipitation_query():
    #converts the query results to a dictionary usind date as the key
    #and prcp as the value
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()
    results._asdict()
    return jsonify(results)
        
@app.route('/api/v1.0/stations')
def stations():
    #return a list of the stations
    results = session.query(station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def tobs():
    #get tobs data as a list
    import datetime as df
    year_results = df.date(2017, 8, 23) - dt.timedelta(days=365)
    last_year = session.query(measurement.station,measurement.tobs).\
            filter(measurement.station == active_station).\
            filter(measurement.date >= year_results).all()
    temp_list= []
        for row in last_year:
            row_dict = {}
            row['date'] = last_year[0]
            row["tobs"] = last_year[1]
            temp_list.append(row)
        
    return jsonify(temp_list)
        
@app.route('/api/v1.0/<start>')
def start_date(start):
    #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    import datetime as df
    year_results = df.date(2017, 8, 23) - dt.timedelta(days=365)
    starting = session.query(func.min(measurement.tobs), func.avg(measurements.tobs)func.max(measurements.tobs)).\
        filter(measurement.date >= start).all()
    return jsonify(starting)
    
    
@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    import datetime as df
    year_results = df.date(2017, 8, 23) - dt.timedelta(days=365)
    start_end = session.query(func.min(measurement.tobs), func.avg(measurements.tobs)func.max(measurements.tobs)).\
        filter(measurement.date >= start).all().filter(measurements.date <= end).all()
    final = list(np.ravel(start_end))
    return jsonify(starting)    

if __name__ == '__main__':
    app.run
