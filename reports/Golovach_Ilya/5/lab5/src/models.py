from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Связь многие-ко-многим между Build и Component
build_component = Table(
    'build_component', Base.metadata,
    Column('build_id', Integer, ForeignKey('builds.id')),
    Column('component_id', Integer, ForeignKey('components.id'))
)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    components = relationship("Component", back_populates="category")

class Manufacturer(Base):
    __tablename__ = "manufacturers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    website = Column(String(200))
    components = relationship("Component", back_populates="manufacturer")

class Component(Base):
    __tablename__ = "components"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    category = relationship("Category", back_populates="components")
    manufacturer = relationship("Manufacturer", back_populates="components")
    builds = relationship("Build", secondary=build_component, back_populates="components")

class Build(Base):
    __tablename__ = "builds"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250))
    total_price = Column(Float)
    components = relationship("Component", secondary=build_component, back_populates="builds")
