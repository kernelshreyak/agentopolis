from sqlalchemy import Column, String,Integer,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,Mapped,mapped_column
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
    scenarioresponses: Mapped[list["ScenarioResponseModel"]] = relationship(
        "ScenarioResponseModel",
        back_populates="world",
        cascade="all, delete",
    )


class ScenarioResponseModel(Base):
    __tablename__ = "scenario_responses"

    scenario_response_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    scenario_response_report = Column(String, nullable=False)
    world_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("worlds.world_id", ondelete="CASCADE"),
    )
    world: Mapped[WorldModel] = relationship(
        "WorldModel",
        back_populates="scenarioresponses",
        cascade="all, delete",
    )
    worldactions: Mapped[list["WorldActionModel"]] = relationship(
        "WorldActionModel",
        back_populates="scenarioresponse",
        cascade="all, delete",
    )

class WorldActionModel(Base):
    """
    Represents a single world action in the simulation.
    """

    __tablename__ = "world_actions"

    worldaction_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    """
    Unique identifier for the world action.
    """

    resource_name = Column(String, nullable=False)
    """
    The name of the resource affected by the world action.
    """

    agent_slug = Column(String, nullable=False)
    """
    The slug of the agent that performed the world action.
    """

    action = Column(String, nullable=False)
    """
    The action performed by the agent.
    """

    simulated_time_taken = Column(String, nullable=True)
    """
    The amount of time the action took to complete in the simulation.
    """

    resource_value = Column(Integer, nullable=False,default=0)
    """
    The value of the resource after the world action.
    """

    scenario_response_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("scenario_responses.scenario_response_id", ondelete="CASCADE"),
    )
    """
    The scenario response that this world action is a part of.
    """

    scenarioresponse: Mapped[ScenarioResponseModel] = relationship(
        "ScenarioResponseModel",
        back_populates="worldactions",
        cascade="all, delete",
    )
    """
    The relationship between the world action and the scenario response.
    """


def create_tables():
    engine = create_engine(DATABASE_URL)

    print(f"""Creating {len(Base.metadata.tables)} tables...""")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")