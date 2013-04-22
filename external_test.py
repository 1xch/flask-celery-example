#testing basic celery setup
import requests
import random

for i in range(100):
    p = {'x':random.randrange(1,10000000), 'y':random.randrange(1,1000000000)}
    r = requests.get('http://localhost:5000/test', params = p)
    print r.json()
    r2 = requests.get("http://localhost:5000/test/result/{}".format(r.json()['goto']) )
    print r2.json()

