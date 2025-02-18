from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ChatMessage(Base):
    """聊天记录表"""
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender = Column(String(100))
    message = Column(Text)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

def init_db():
    """初始化数据库（需先创建data目录）"""
    engine = create_engine(f"sqlite:///{Config.PathConfig.DB_PATH}")
    Base.metadata.create_all(engine)
