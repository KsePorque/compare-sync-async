# Compare Sync Async
The idea of this project is to perform tests to compare the speed for sync and async requests.
I perform test using my own API for managing wines collections, developed as a part of Portfolio project: http://kseporque.pythonanywhere.com/ 

<br><br>
<strong>Libraries:</strong> aiohttp, asyncio, requests

# Project files
* To send GET-requests (sync/async): receive_data_api.py 
* To send POST-requests (sync/async): post_data_api.py 
* To send DELETE-requests (sync/async): delete_data_api.py
<br>
Tests to measure and compare time that requests take are launched from <strong>main.py</strong> <br>
Settings to connect to api: settings.py <br>

Note: code does not implement additional checks (like whether or not API is accessible). It is supposed, that all the requests are ok.

# Results
Asyncronious requests in average improve performance 3 times

## GET requests (50 requests)
Sync: ~45 seconds <br>
Async: ~13 seconds 

## POST requests (50 requests)
Sync: ~40 seconds <br>
Async: ~13 seconds

## GET requests (50 requests)
Sync: ~48 seconds <br>
Async: ~13 seconds 
