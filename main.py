import csv
import requests
from multiprocessing.dummy import Pool as ThreadPool
from concurrent.futures import ThreadPoolExecutor, wait

DOMAIN = 'https://cdn.ampproject.org/update-ping/c/s/m.magazineluiza.com.br'

def clearCacheAMP(url):
    path = DOMAIN + url
    print (path)
    r = requests.get(path)
    print(r)
    return r



def readFile():
    row_count = sum(1 for row in csv.reader( open('url-AMP.csv') ) )
    with open('url-AMP.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clearCacheAMP(row['url'])
            row_count -= 1
            print(row_count)

# function to be mapped over
def getParallel(threads=4):
    pool = ThreadPool(threads)
    results = pool.map(clearCacheAMP, url)
    pool.close()
    pool.join()
    return results


def getParallel2():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(readFile)]
        wait(futures)

if __name__ == "__main__":
    getParallel2()
