from __future__ import print_function
import sys

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
        prop = self.session.query(Property).filter(Property.id == id).one()
        return jsonify(prop)

def main():
    server = msgpackrpc.Server(PropertyServer())
    server.listen(msgpackrpc.Address("localhost", 18800))
    print("start serving...")
    server.start()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        Base.metadata.create_all()
        
        import string
        import random
        def string_generator(size=12, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        session = Session()
        for i in range(100):
            session.add(Property(description=string_generator()))
        session.commit()
        print("data table and data is prepared.")
    else:
        main()
