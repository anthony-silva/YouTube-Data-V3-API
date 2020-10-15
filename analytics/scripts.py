'''
# uses time to grasp basic concepts of concurrency and multithreading

import time 
import concurrent.futures 

start = time.perf_counter()
def do_something(seconds):
    print('Sleeping {} second(s)...'.format(seconds))
    time.sleep(seconds) 
    return 'Done sleeping...{}'.format(seconds)

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 2, 3, 4, 5]
    results = executor.map(do_something, secs)
      
    for result in results:
        print(result)


finish = time.perf_counter()    
print('Finished in {} second(s)'.format(round(finish-start, 2)))
'''




'''
# example for using multiple processes using sleep for examples

import multiprocessing 
import time 
import concurrent.futures

start = time.perf_counter() 

def do_something(seconds):
    print('Sleeping {} second(s)...'.format(seconds))
    time.sleep(seconds)
    return 'Done sleeping...{}'.format(seconds)

# Use concurrent.futures to shorten code
with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

# code executed after process are finished
finish = time.perf_counter()
print('Finished in {} second(s)'.format(round(finish-start, 2)))

'''



import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')







'''
# example executing threads concurrently
# useful for i/o, not computation heavy threads 

import multiprocessing 
import requests
import time
import concurrent.futures
import threading

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    print(threading.active_count())


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
'''



'''
# Try, Except, Else, Finally, Error Handling

try:
    f = open('textfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')

try:
    f = open('text_file.txt')
    if f.name == 'text_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('File is corrupt.')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')
    '''