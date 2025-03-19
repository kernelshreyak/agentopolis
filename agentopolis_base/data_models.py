from sqlalchemy import Column, String,Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,Mapped
import os
import uuid
from dotenv import load_dotenv

Base = declarative_base()

load_dotenv()

# Database Configuration
DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy Models
class WorldModel(Base):
    __tablename__ = "worlds"

    world_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)


class WorldActionModel(Base):
    __tablename__ = "world_actions"

    worldaction_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    resource_name = Column(String, nullable=False)
    agent_slug = Column(String, nullable=False)
    action = Column(String, nullable=False)
    resource_value = Column(Integer, nullable=False,default=0)
    world: Mapped["WorldModel"] = relationship(
        "WorldModel",
        back_populates="worldactions",
        cascade="all, delete",
    )

class ScenarioResponseModel(Base):
    __tablename__ = "scenario_responses"

    scenario_response_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    scenario_response_report = Column(String, nullable=False)
    world: Mapped["WorldModel"] = relationship(
        "WorldModel",
        back_populates="scenarioresponses",
        cascade="all, delete",
    )

def create_tables():
    engine = create_engine(DATABASE_URL)

    print(f"""Creating {len(Base.metadata.tables)} tables...""")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")