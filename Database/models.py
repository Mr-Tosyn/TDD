from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos' # This is the name of the table in the database
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
    

    
    
