from DataCollectors.twitterdatacollect import *
import pytest

#Test calls

#Testing Build Markers method
#Correct Case
def tests_correct_case():
    test_collector = TwitterDataCollect()
    response = test_collector.buildMarkers(["#6nations","sixnations","france"])
    assert test_collector.markers == ['#6nations', 'sixnations', '#sixnations', 'france', '#france']
    assert response == True


#Passing markers string instead of list
def tests_markers_str():
    test_collector = TwitterDataCollect()
    response = test_collector.buildMarkers("6 nations")
    assert test_collector.markers == []
    assert response == False

#Passing markers int instead of list
def tests_markers_int():
    test_collector = TwitterDataCollect()
    response = test_collector.buildMarkers(5)
    assert test_collector.markers == []
    assert response == False


#Passing markers empty parameters
def tests_markers_empty():
    test_collector = TwitterDataCollect()
    response = test_collector.buildMarkers()
    assert test_collector.markers == []
    assert response == False
