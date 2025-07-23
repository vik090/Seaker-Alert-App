from sqlalchemy import create_engine, Column, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Metric(Base):
    __tablename__ = 'metrics'

    timestamp = Column(DateTime, primary_key=True, default=datetime.datetime.utcnow)
    cpu = Column(Float)
    ram_used = Column(Float)
    ram_total = Column(Float)
    disk_used = Column(Float)
    disk_total = Column(Float)
    uptime = Column(Float)
    temperature = Column(String)

# DB setup
engine = create_engine('sqlite:///metrics.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_metrics(data):
    record = Metric(
        cpu=data["CPU (%)"],
        ram_used=data["RAM Used (GB)"],
        ram_total=data["RAM Total (GB)"],
        disk_used=data["Disk Used (GB)"],
        disk_total=data["Disk Total (GB)"],
        uptime=data["Uptime (hours)"],
        temperature=str(data["Temperature (°C)"])
    )
    session.add(record)
    session.commit()

def get_last_n_records(n=20):
    return session.query(Metric).order_by(Metric.timestamp.desc()).limit(n).all()
