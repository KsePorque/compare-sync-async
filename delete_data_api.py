"""
Compare sync and async data deletion from Wines API:
http://kseporque.pythonanywhere.com/vinotheque/api/v1/docs/
"""
#import time
import aiohttp
import asyncio
import requests
from requests.auth import HTTPBasicAuth
from settings import URL, USERNAME, PASSWORD


# returns the list of id of the wines that should be deleted
# I will only delete test data added while testing
def wines_indices():
    response = requests.get(URL + f'wines', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    wines_id = []
    if response.status_code == 200:
        data = response.json()
        wines_id = [wine['id'] for wine in data if wine['name']=="test name"]
    return wines_id

# Sync function (200 delete-requests)
def delete_wines_sync(wines_id):
    if not wines_id:
        wines_id = wines_indices()
    #print(f'{len(wines_id)} records will be removed')
    for id in wines_id:
        response = requests.delete(URL+f'wines/{id}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
        #print(f'Response status: {response.status_code}')


# Async function
async def delete_url(session: aiohttp.ClientSession, url: str):
    async with session.delete(url) as response:
        print(f'Response status: {response.status}')
        #return await response


async def delete_wines_async(wines_id):
    if not wines_id:
        wines_id = wines_indices()
    print(f'{len(wines_id)} records will be removed')
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(USERNAME, PASSWORD)) as session:
        tasks: List[asyncio.Task] = []
        for id in wines_id:
            url = URL + f'wines/{id}'
            tasks.append(
                asyncio.ensure_future(delete_url(session, url))
            )
        return await asyncio.gather(*tasks)


# # Test sync delete-requests
# start_time = time.time()
# delete_wines_sync()
# end_time = time.time()
#
# print(f"Sync execution time: {end_time - start_time} seconds")  #175 seconds


# ## Test async post-requests
# start_time = time.time()
# asyncio.run(delete_wines_async())
# end_time = time.time()
#
# print(f"Async execution time: {end_time - start_time} seconds")  #50 seconds

