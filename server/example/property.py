from __future__ import print_function
import sys
from json import dumps

import msgpackrpc
from msgpackrpc.database import Base, Session, jsonify
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import Column, Integer, String

class Property(Base):
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True)
    description = Column(String(255))


class PropertyServer(object):
    def __init__(self):
        self.session = Session()

    def get_property(self, id):
        prop = session.query(Property).filter(Property.id == id).one()
        return jsonify(prop)

def main():
    server = msgpackrpc.Server(PropertyServer())
    server.listen(msgpackrpc.Address("localhost", 18800))
    print("start serving...")
    server.start()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        Base.metadata.create_all()
    else:
        main()
