import time
import asyncio

from receive_data_api import get_wines_sync, get_wines_async
from post_data_api import post_wines_sync, post_wines_async
from delete_data_api import delete_wines_sync, delete_wines_async, wines_indices

def test_sync(number_of_tests=10, number_of_wines=100):
    res_post = []
    res_get = []
    res_delete = []

    for _ in range(number_of_tests):
        # POST
        start_time = time.time()
        post_wines_sync(number_of_wines)
        end_time = time.time()

        duration = end_time - start_time
        res_post.append(duration)

        added_wines_idx = wines_indices()

        # GET
        start_time = time.time()
        get_wines_sync(added_wines_idx)
        end_time = time.time()

        duration = end_time - start_time
        res_get.append(duration)

        # DELETE
        start_time = time.time()
        delete_wines_sync(added_wines_idx)
        end_time = time.time()

        duration = end_time - start_time
        res_delete.append(duration)


    test_result = {
        'number_of_tests': number_of_tests,
        'get': res_get,
        'post': res_post,
        'delete': res_delete
    }
    return test_result

def test_async(number_of_tests=10, number_of_wines=100):
    res_post = []
    res_get = []
    res_delete = []

    for _ in range(number_of_tests):
        # POST
        start_time = time.time()
        asyncio.run(post_wines_async(number_of_wines))
        end_time = time.time()

        duration = end_time - start_time
        res_post.append(duration)

        added_wines_idx = wines_indices()

        # GET
        start_time = time.time()
        asyncio.run(get_wines_async(added_wines_idx))
        end_time = time.time()

        duration = end_time - start_time
        res_get.append(duration)

        # DELETE
        start_time = time.time()
        asyncio.run(delete_wines_async(added_wines_idx))
        end_time = time.time()

        duration = end_time - start_time
        res_delete.append(duration)


    test_result = {
        'number_of_tests': number_of_tests,
        'get': res_get,
        'post': res_post,
        'delete': res_delete
    }
    return test_result


if __name__ == '__main__':
    NUM_TESTS = 3
    NUM_WINES = 50

    sync_results = test_sync(number_of_tests=NUM_TESTS, number_of_wines=NUM_WINES)
    async_results = test_async(number_of_tests=NUM_TESTS, number_of_wines=NUM_WINES)

    average_get_sync = sum(sync_results['get']) / sync_results['number_of_tests']
    average_get_async = sum(async_results['get']) / async_results['number_of_tests']

    average_post_sync = sum(sync_results['post']) / sync_results['number_of_tests']
    average_post_async = sum(async_results['post']) / async_results['number_of_tests']

    average_delete_sync = sum(sync_results['delete']) / sync_results['number_of_tests']
    average_delete_async = sum(async_results['delete']) / async_results['number_of_tests']

    print(f'GET: {average_get_sync}, {average_get_async}')
    print(f'POST: {average_post_sync}, {average_post_async}')
    print(f'DELETE: {average_delete_sync}, {average_delete_async}')


