"""
Compare sync and async data posting to Wines API:
http://kseporque.pythonanywhere.com/vinotheque/api/v1/docs/
"""
#import time
import aiohttp
import asyncio
import requests
from requests.auth import HTTPBasicAuth
from settings import URL, USERNAME, PASSWORD

def generate_new_wines(number_of_wines):
    dummy_wine = {
        "name": "test name",
        "wine_type": 2,
        "year": 2022,
        "country": 93
    }
    return [dummy_wine] * number_of_wines


# Sync function (100 post-requests)
def post_wines_sync(number_of_wines=100):
    for wine in generate_new_wines(number_of_wines):
        response = requests.post(URL+f'wines/', auth=HTTPBasicAuth(USERNAME, PASSWORD), data=wine)
        #print(f'Response status: {response.status_code}')


# Async function
async def post_url(session: aiohttp.ClientSession, url: str, data):
    async with session.post(url, data=data) as response:
        #print(f'Response status: {response.status}')
        return await response.json()

async def post_wines_async(number_of_wines=100):
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(USERNAME, PASSWORD)) as session:
        tasks: List[asyncio.Task] = []
        url = URL + f'wines/'
        for wine in generate_new_wines(number_of_wines):
            tasks.append(
                asyncio.ensure_future(post_url(session, url, wine))
            )
        return await asyncio.gather(*tasks)


# # Test sync post-requests
# start_time = time.time()
# post_wines_sync()
# end_time = time.time()
#
# print(f"Sync execution time: {end_time - start_time} seconds")  #65-72 seconds
#
#
# ## Test async post-requests
# start_time = time.time()
# asyncio.run(post_wines_async())
# end_time = time.time()
#
# print(f"Async execution time: {end_time - start_time} seconds")  #24 seconds
#
