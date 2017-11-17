import csv
import requests
from multiprocessing.dummy import Pool as ThreadPool

DOMAIN = 'https://cdn.ampproject.org/update-ping/c/s/m.magazineluiza.com.br'

def clearCacheAMP(url):
    path = DOMAIN + url
    print (path)
    r = requests.get(path)
    print(r)
    return r



def readFile():
    with open('url-AMP.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            clearCacheAMP(row['url'])

# function to be mapped over
def getParallel(threads=2):
    pool = ThreadPool(threads)
    results = pool.map( clearCacheAMP, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    readFile()
