from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from controller import data_folder
from platform import system


if system() == "Darwin":
    engine = create_engine(f"sqlite:////{data_folder}/data.db")
else:
    engine = create_engine(f"sqlite:///{data_folder}/data.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sentTo = relationship("Report", backref="sender", lazy="dynamic")

    def __repr__(self):
        return f"<Account | {self.name}>"


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("accounts.id"))
    name = Column(String(100))
    number = Column(String(20))
    username = Column(String(100))
    status = Column(String(140))

    def __repr__(self):
        return f"<{self.name} | {self.status}>"


# #TODO - NOT COMPLETED
#
# class Settings(Base):
#     __tablename__ = "settings"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     number = Column(String(20))
#     username = Column(String(100))
#     status = Column(String(140))
#
#     def __repr__(self):
#         return f"<{self.name} | {self.status}>"


Base.metadata.create_all(bind=engine)



