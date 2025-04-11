from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..utils.db import Base

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    lines = relationship("StationLine", back_populates="station", cascade="all, delete")

    def __repr__(self):
        return f"<Station(id={self.id}, name={self.name})>"
