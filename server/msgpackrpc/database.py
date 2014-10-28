from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+oursql://localhost/test')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)

def jsonify(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object.
    """
    json = {}
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json[col.name] = getattr(model, col.name)
    return dumps([json])