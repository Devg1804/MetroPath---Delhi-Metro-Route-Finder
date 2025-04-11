from sqlalchemy import Column, Integer, ForeignKey
from ..utils.db import Base

class StationLine(Base):
    __tablename__ = "station_lines"

    station_id = Column(Integer, ForeignKey("stations.id", ondelete="CASCADE"), primary_key=True)
    line_id = Column(Integer, ForeignKey("lines.id", ondelete="CASCADE"), primary_key=True)

    def __repr__(self):
        return f"<StationLine(station_id={self.station_id}, line_id={self.line_id})>"
