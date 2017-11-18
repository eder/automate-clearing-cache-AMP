import csv
import requests
from multiprocessing.dummy import Pool as ThreadPool

BASE_PATH = 'https://cdn.ampproject.org/update-ping/c/s/m.magazineluiza.com.br'
THREADS = 50

def clearCacheAMP(url):
    path = BASE_PATH + url
    print (path)
    response = requests.get(path)
    print(response)
    return response

def readFile():
    links = []
    row_count = sum(1 for row in csv.reader( open('url-AMP.csv') ) )
    with open('url-AMP.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            links.append(row['url'])
        return links

# function to be mapped over
def getParallel(urls, threads=THREADS):
    pool = ThreadPool(threads)
    results =  pool.map(clearCacheAMP, urls)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    getParallel(readFile())
