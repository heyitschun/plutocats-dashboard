from env_vars import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.engine.url import make_url

database_url = make_url(str(DATABASE_URL))
engine = create_engine(database_url)