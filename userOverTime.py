import os
import datetime
import time
from temboo.Library.Instagram import GetRecentMediaForLocation
from temboo.core.session import TembooSession

def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

def readLocationIDs():
    path = "data" + os.sep + "locationIDs.txt"
    contents = readFile(path)
    IDList = contents.split()
    return IDList

# helper function to obtain UNIX timestamp
def getUNIXTimestamp(year, month):
    d = datetime.datetime(year, month, 0, 0, 0, 0, 0)
    return time.mktime(d.timetuple())

def getDateDistributionData():
    # Create a session with your Temboo account details
    session = TembooSession("chenlian", "myFirstApp", “key”)

    # Instantiate the Choreo
    getRecentMediaForLocationChoreo = GetRecentMediaForLocation(session)

    # Get an InputSet object for the Choreo
    getRecentMediaForLocationInputs = getRecentMediaForLocationChoreo.new_input_set()

    IDList = readLocationIDs()
    totalMedia = dict()
    for year in xrange(2011, 2015):
        for month in xrange(1, 13):
            timeStart = getUNIXTimestamp(year, month)
            timeEnd = getUNIXTimestamp(year, month+1) if (month != 12) else getUNIXTimestamp(year+1, 1)
            title = str(year) + "," + str(month)

            totalMedia[title] = 0  # set the total amount of current month media to 0
            for id in IDList:
                # Set the Choreo inputs
                getRecentMediaForLocationInputs.set_LocationID(id)
                getRecentMediaForLocationInputs.set_MaxTimestamp(str(timeEnd))
                getRecentMediaForLocationInputs.set_ClientID(“key”)
                getRecentMediaForLocationInputs.set_MinTimestamp(str(timeStart))

                # Execute the Choreo
                getRecentMediaForLocationResults = getRecentMediaForLocationChoreo.execute_with_results(getRecentMediaForLocationInputs)

                # As "latitude" just occur once in one post, we use this to count the amount of media of the month
                totalMedia[title] += getRecentMediaForLocationResults.get_Response().count("latitude")
    return totalMedia

def writeMediaOverDate():
    path = "data" + os.sep + "MediaAmountOverDate.txt"

    # create the temp dir, if it is not there
    if (not os.path.exists("data")):
        os.makedirs("data")

    # remove old file, if it is there
    if (os.path.exists(path)):
        os.remove(path)

    contents = ""

    dateMediaData = getDateDistributionData()
    for date in dateMediaData:
        contents += date + ": " + str(dateMediaData[date])

    # add new file
    writeFile(path, contents)

def writeFile(filename, contents, mode="wt"):
    # wt = "write text"
    with open(filename, mode) as fout:
        fout.write(contents)

writeMediaOverDate()