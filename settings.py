SECRET_KEY = 'hey_now_this_is_no_secret'

#celery
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = "redis"
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_PORT = 6379
CELERY_REDIS_DB = 0
