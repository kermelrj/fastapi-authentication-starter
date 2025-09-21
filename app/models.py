import uuid

from sqlalchemy import Column, UUID, String, DateTime, func
from sqlalchemy.orm import validates
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address, "Provided email is not valid"
        return address