from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
DATABASE_DEFAULT = env.db_url('DATABASE_URL')
GOOGLE_API_KEY = env('GOOGLE_API_KEY')
