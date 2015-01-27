from temboo.core.session import TembooSession
from temboo.Library.Instagram import SearchLocations
import numpy as np
import time
import os
import json

def getLocationIDsInsideMainlandChina():
    locationIDs = set()

    # Create a session with your Temboo account details
    session = TembooSession("chenlian", "myFirstApp", “key”)

    # Instantiate the Choreo
    searchLocationsChoreo = SearchLocations(session)

    # Get an InputSet object for the Choreo
    searchLocationsInputs = searchLocationsChoreo.new_input_set()

    # Get latitudes and longitudes in mainland China
    latsLongsInMainland = getMainlandChinaLatitudeAndLongitude()
    for lat in latsLongsInMainland:
        for lon in latsLongsInMainland[lat]:
            # Set the Choreo inputs
            searchLocationsInputs.set_Distance("5000")
            searchLocationsInputs.set_Latitude(str(lat))
            searchLocationsInputs.set_Longitude(str(lon))
            searchLocationsInputs.set_ClientID(“key”)

            # Execute the Choreo
            searchLocationsResults = searchLocationsChoreo.execute_with_results(searchLocationsInputs)

            # Get the Choreo outputs
            IDOutput = json.loads(searchLocationsResults.get_Response())
            # print len(IDOutput["data"])
            if len(IDOutput["data"]) == 0:
                continue
            for i in xrange(len(IDOutput["data"])):
                locationIDs.add(IDOutput["data"][i]["id"])
                print IDOutput["data"][i]["name"]
            start = time.time()
            elapedTime = 0.2
            while time.time() - start < elapedTime:
                continue
    print locationIDs
    return locationIDs

def getMainlandChinaLatitudeAndLongitude():
    mapOfMainland = dict()

    for lat in np.arange(40.212, 39.735, -0.04):  # Beijing
        mapOfMainland[lat] = np.arange(116.096, 116.620, 0.04)
    for lat in np.arange(31.379, 30.787, -0.04):  # Shanghai
        mapOfMainland[lat] = np.arange(121.130, 121.815, 0.04)
    for lat in np.arange(23.464, 22.524, -0.04):  # Guangzhou
        mapOfMainland[lat] = np.arange(113.147, 114.064, 0.04)
    return mapOfMainland

def writeFile(filename, contents, mode="wt"):
    # wt = "write text"
    with open(filename, mode) as fout:
        fout.write(contents)

def writeLocationIDs():
    path = "data" + os.sep + "locationIDs.txt"

    # create the temp dir, if it is not there
    if (not os.path.exists("data")):
        os.makedirs("data")

    # remove old file, if it is there
    if (os.path.exists(path)):
        os.remove(path)

    contents = ""

    locationIDs = getLocationIDsInsideMainlandChina()
    for id in locationIDs:
        contents += str(id) + " "

    # add new file
    writeFile(path, contents)

writeLocationIDs()