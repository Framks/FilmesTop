
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/films-top'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = 6379
    CACHE_DEFAULT_TIMEOUT = 300