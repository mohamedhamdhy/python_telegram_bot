from sqlalchemy import Column, Integer, String, LargeBinary, Text, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, index=True)  # Now BigInteger is defined
    file_name = Column(String, nullable=True)
    file_type = Column(String)  # "text", "pdf", "image", "video", "document"
    content = Column(LargeBinary, nullable=True)  # binary data for files
    text_content = Column(Text, nullable=True)  # for plain text notes
