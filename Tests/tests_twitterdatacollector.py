from DataCollectors import *

#Test calls

#Testing Build Markers method
#Correct Case
test_collector = TwitterDataCollect()
response = test_collector.buildMarkers(["#6nations","sixnations","france"])
print(test_collector.markers)
print(response)

#Passing markers string instead of list
test_collector = TwitterDataCollect()
response = test_collector.buildMarkers("6 nations")
print(test_collector.markers)
print(response)

#Passing markers int instead of list
test_collector = TwitterDataCollect()
response = test_collector.buildMarkers(5)
print(test_collector.markers)
print(response)

#Passing markers empty parameters
test_collector = TwitterDataCollect()
response = test_collector.buildMarkers()
print(test_collector.markers)
print(response)
