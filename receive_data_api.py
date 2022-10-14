"""
Compare sync and async data retrieval from Wines API:
http://kseporque.pythonanywhere.com/vinotheque/api/v1/docs/
"""
#import time
import aiohttp
import asyncio
import requests
from requests.auth import HTTPBasicAuth
from settings import URL, USERNAME, PASSWORD

# Sync function (100 requests)
def get_wines_sync(indices):
    res = [None] * len(indices)
    idx = 0
    for id in indices:
        response = requests.get(URL+f'wines/{id}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
        #print(f'Response status: {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            #print(data)
            res[idx] = data
        idx += 1
    return res



# Async function
async def get_url(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        #print(f'Response status: {response.status}')
        if response.status == 200:
            data = response.json()
            #print(data)
            return await response.json()

async def get_wines_async(indices):
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(USERNAME, PASSWORD)) as session:
        tasks: List[asyncio.Task] = []
        for id in indices:
            url = URL+f'wines/{id}'

            tasks.append(
                asyncio.ensure_future(get_url(session, url))
            )
        return await asyncio.gather(*tasks)

#
# ## Test sync get-requests
# start_time = time.time()
# data_list = get_wines_sync()
# end_time = time.time()
#
# print(f"Sync execution time: {end_time - start_time} seconds")  #88 seconds
# print([d for d in data_list if d is not None])
#
# ## Test async get-requests
# start_time = time.time()
# data_list = asyncio.run(get_wines_async())
# end_time = time.time()
#
# print(f"Async execution time: {end_time - start_time} seconds")  #23 seconds
# print([d for d in data_list if d is not None])
