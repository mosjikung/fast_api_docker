from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database configuration connect to postgresql
#
DATABASE_URL = "postgresql://postgres:root@localhost/popcat"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    json_serializer=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# JWT Configuration

SECRET_KEY = "lemoncode21"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

SECRET_KEY_WEB = 'zYb08w1Nrv'
ALGORITHM_WEB = 'HS256'
