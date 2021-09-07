{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e2fda03",
   "metadata": {},
   "outputs": [],
   "source": [
    "#setup all the necessary imports\n",
    "%matplotlib inline\n",
    "from matplotlib import style\n",
    "style.use('fivethirtyeight')\n",
    "import matplotlib.pyplot as plt \n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flash import Flask, jsonify\n",
    "\n",
    "#make the engine from the other notbook for this assignment\n",
    "#basically we are pulling straight from the other notebook here\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "Base = automap_base\n",
    "# reflect an existing database into a new model\n",
    "Base = automap_base()\n",
    "# reflect the tables\n",
    "Base.prepare(engine, reflect=True)\n",
    "measurement = Base.classes.measurement\n",
    "station = Base.classes.station\n",
    "session = Session(engine)\n",
    "session\n",
    "\n",
    "#do the Flask setup, which is necessary to do in a python file\n",
    "#instead of a .ipynb in order to run\n",
    "app = Flask(__name__)\n",
    "@app.route('/')\n",
    "def home:\n",
    "    return(\n",
    "    f\"Welcome to David's Climate Analysis API!\"\n",
    "    f\"All Available Routes:\"\n",
    "    f\"/api/v1.0/precipitation\"\n",
    "    f\"/api/v1.0/precipitation\"\n",
    "    f\"/api/v1.0/stations\"\n",
    "    f\"/api/v1.0/tobs\"\n",
    "    f\"/api/v1.0/<start>\"\n",
    "    f\"/api/v1.0/<start>/<end>\"\n",
    "    )\n",
    "\n",
    "@app.route('/api/v1.0/precipitation')\n",
    "def precipitation_query():\n",
    "    #converts the query results to a dictionary usind date as the key\n",
    "    #and prcp as the value\n",
    "    session = Session(engine)\n",
    "    results = session.query(measurement.date, measurement.prcp).all()\n",
    "    results._asdict()\n",
    "    return jsonify(results)\n",
    "        \n",
    "@app.route('/api/v1.0/stations')\n",
    "def stations:\n",
    "    #return a list of the stations\n",
    "    results = session.query(station.station).all()\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations)\n",
    "\n",
    "@app.route('/api/v1.0/tobs')\n",
    "def min_max_timeframe(start, end):\n",
    "    #results = session.query(func.min(measurement.tobs), func.avg(measurements.tobs)func.max(measurements.tobs))f\n",
    "@app.route('/api/v1.0/<start>')\n",
    "def min_max_timeframe(start, end):\n",
    "    #results = session.query(func.min(measurement.tobs), func.avg(measurements.tobs)func.max(measurements.tobs))f\n",
    "@app.route('/api/v1.0/<start>/<end>')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
