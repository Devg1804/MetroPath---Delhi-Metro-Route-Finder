from sqlalchemy import Column, Integer, String
from ..utils.db import Base

class Line(Base):
    __tablename__ = "lines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Line(id={self.id}, name={self.name})>"
