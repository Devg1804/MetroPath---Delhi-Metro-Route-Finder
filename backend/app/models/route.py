from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from ..utils.db import Base

class Route(Base):
    __tablename__ = "routes"

    source_id = Column(Integer, ForeignKey("stations.id", ondelete="CASCADE"), primary_key=True)
    destination_id = Column(Integer, ForeignKey("stations.id", ondelete="CASCADE"), primary_key=True)
    distance = Column(DECIMAL(5,2), nullable=False)

    def __repr__(self):
        return f"<Route(source={self.source_id}, destination={self.destination_id}, distance={self.distance})>"
