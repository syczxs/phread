import redis

r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
r.set('name', 'xiaoming')

print(r.get('name'))