from sqlalchemy.orm import Session
from models import Component, Category, Manufacturer, Build

# CRUD для Component
def create_component(db: Session, component_data: dict):
    db_component = Component(**component_data)
    db.add(db_component)
    db.commit()
    db.refresh(db_component)
    return db_component

def get_components(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Component).offset(skip).limit(limit).all()

def get_component(db: Session, component_id: int):
    return db.query(Component).filter(Component.id == component_id).first()

def update_component(db: Session, component_id: int, component_data: dict):
    db_component = db.query(Component).filter(Component.id == component_id).first()
    if db_component:
        for key, value in component_data.items():
            setattr(db_component, key, value)
        db.commit()
        db.refresh(db_component)
    return db_component

def delete_component(db: Session, component_id: int):
    db_component = db.query(Component).filter(Component.id == component_id).first()
    if db_component:
        db.delete(db_component)
        db.commit()
    return db_component

# CRUD для Category
def create_category(db: Session, category_data: dict):
    db_category = Category(**category_data)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def update_category(db: Session, category_id: int, category_data: dict):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        for key, value in category_data.items():
            setattr(db_category, key, value)
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# CRUD для Manufacturer
def create_manufacturer(db: Session, manufacturer_data: dict):
    db_manufacturer = Manufacturer(**manufacturer_data)
    db.add(db_manufacturer)
    db.commit()
    db.refresh(db_manufacturer)
    return db_manufacturer

def get_manufacturers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Manufacturer).offset(skip).limit(limit).all()

def get_manufacturer(db: Session, manufacturer_id: int):
    return db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()

def update_manufacturer(db: Session, manufacturer_id: int, manufacturer_data: dict):
    db_manufacturer = db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if db_manufacturer:
        for key, value in manufacturer_data.items():
            setattr(db_manufacturer, key, value)
        db.commit()
        db.refresh(db_manufacturer)
    return db_manufacturer

def delete_manufacturer(db: Session, manufacturer_id: int):
    db_manufacturer = db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if db_manufacturer:
        db.delete(db_manufacturer)
        db.commit()
    return db_manufacturer

# CRUD для Build
def create_build(db: Session, build_data: dict):
    db_build = Build(**build_data)
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build

def get_builds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Build).offset(skip).limit(limit).all()

def get_build(db: Session, build_id: int):
    return db.query(Build).filter(Build.id == build_id).first()

def update_build(db: Session, build_id: int, build_data: dict):
    db_build = db.query(Build).filter(Build.id == build_id).first()
    if db_build:
        for key, value in build_data.items():
            setattr(db_build, key, value)
        db.commit()
        db.refresh(db_build)
    return db_build

def delete_build(db: Session, build_id: int):
    db_build = db.query(Build).filter(Build.id == build_id).first()
    if db_build:
        db.delete(db_build)
        db.commit()
    return db_build

def add_component_to_build(db: Session, build_id: int, component_id: int):
    build = db.query(Build).filter(Build.id == build_id).first()
    component = db.query(Component).filter(Component.id == component_id).first()
    if build and component:
        build.components.append(component)
        db.commit()
        db.refresh(build)
    return build

def remove_component_from_build(db: Session, build_id: int, component_id: int):
    build = db.query(Build).filter(Build.id == build_id).first()
    component = db.query(Component).filter(Component.id == component_id).first()
    if build and component:
        build.components.remove(component)
        db.commit()
        db.refresh(build)
    return build
