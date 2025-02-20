# This file is used to create the database connection and the session object
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql://postgres:1@localhost:5432/monorepo"
Base = declarative_base()
