# Execute task Asynchronously.
# ThreadPoolExecutor is good for Input Output Tasks.
# ProcessPoolExecutor is good for CPU intensive Tasks.

import requests
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235'
]

workers = 10

t1 = time.perf_counter()

# This is a I/O Bound task cause its requesting from a network and writing the file into the Disk
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(f'./files/img/{img_name}', 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


# Synchronous execution tasks
# for img_url in img_urls:
#     download_image(img_url)



# Asynchronous or Concurrent execution tasks


# ThreadPoolExecutor is used because the task is I/O bound.
# max workers in python 3.8 is min (32, os.cpu_count() + 4)
#This default value preserves at least 5 workers for I/O bound tasks.
# It utilizes at most 32 CPU cores for CPU bound tasks which release the GIL.
#  And it avoids using very large resources implicitly on many-core machines.

#with ThreadPoolExecutor(max_workers=workers) as executor: # defining max workers
with ThreadPoolExecutor() as executor: # use default number of workers
    executor.map(download_image, img_urls)
    executor.shutdown(wait=True)

# ProcessPoolExecutor is used because the task cpu bound.
# with ProcessPoolExecutor() as executor: # use default number of workers
    # executor.map(function, iterable)
    # executor.shutdown(wait=True)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')