# Compare Sync Async
The idea of this project is to perform tests to compare the speed for sync and async requests.
I perform test using my own API for managing wines collections, developed as a part of Portfolio project: http://kseporque.pythonanywhere.com/ 

# Results
## GET requests (amount: 100 requests)
Sync: ~100 seconds <br>
Async: ~25 seconds 

## POST requests (amount: 100 requests)
Sync: ~65 seconds 
Async: ~25 seconds
