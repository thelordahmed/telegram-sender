from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
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
    sentTo = relationship("ContactsAnony", backref="sender", lazy="dynamic")
    sentDate = Column(DateTime)
    sentCounter = Column(Integer, default= 0)

    def __repr__(self):
        return f"<Account | {self.name}>"


class ContactsAnony(Base):
    """
    * this table will hold the data exported from the excel sheet,
      then status field will be updated according to sending status.
    * tablewidget data on the interface will be fetched from here.
    * starting a new session will clear this table data.
    """
    __tablename__ = "contacts anonymouse"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("accounts.id"))
    name = Column(String(100))
    number = Column(String(20))
    username = Column(String(100))
    status = Column(String(140))

    def __repr__(self):
        return f"<{self.name} | {self.status}>"


class ContactsFamiliar(Base):
    """
    * this table will hold the data exported from the excel sheet,
      then status field will be updated according to sending status.
    * tablewidget data on the interface will be fetched from here.
    * starting a new session will clear this table data.
    """
    __tablename__ = "contacts familiar"
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey("accounts.id"))
    name = Column(String(100))
    number = Column(String(20))
    username = Column(String(100))
    status = Column(String(140))

    def __repr__(self):
        return f"<{self.name} | {self.status}>"



class Settings(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True)
    usernameModeAnony = Column(Integer)
    usernameModeFamiliar = Column(Integer)
    textFirstAnony = Column(Integer)
    textFirstFamiliar = Column(Integer)
    messages = Column(Integer)
    attachFamiliar = Column(String(300))
    attachAnony = Column(String(300))
    asCaptionAnony = Column(Integer)
    asCaptionFamiliar = Column(Integer)
    messageAnony = Column(Text)
    messageFamiliar = Column(Text)

    def __repr__(self):
        return f"<Settings Object 'id:{self.id}'>"


Base.metadata.create_all(bind=engine)



