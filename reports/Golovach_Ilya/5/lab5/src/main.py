from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import Base
from crud import (
    create_component, get_components, get_component,
    update_component, delete_component,
    create_category, get_categories, get_category,
    update_category, delete_category,
    create_manufacturer, get_manufacturers, get_manufacturer,
    update_manufacturer, delete_manufacturer,
    create_build, get_builds, get_build,
    update_build, delete_build,
    add_component_to_build, remove_component_from_build
)
import uvicorn

app = FastAPI()

# Инициализация БД
@app.on_event("startup")
def on_startup():
    init_db()

# Dependency для работы с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинты для Component
@app.post("/components/")
def create_component_endpoint(component: dict, db: Session = Depends(get_db)):
    return create_component(db, component)

@app.get("/components/")
def get_components_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_components(db, skip=skip, limit=limit)

@app.get("/components/{component_id}")
def get_component_endpoint(component_id: int, db: Session = Depends(get_db)):
    component = get_component(db, component_id)
    if not component:
        raise HTTPException(status_code=404, detail="Component not found")
    return component

@app.put("/components/{component_id}")
def update_component_endpoint(component_id: int, component: dict, db: Session = Depends(get_db)):
    updated_component = update_component(db, component_id, component)
    if not updated_component:
        raise HTTPException(status_code=404, detail="Component not found")
    return updated_component

@app.delete("/components/{component_id}")
def delete_component_endpoint(component_id: int, db: Session = Depends(get_db)):
    component = delete_component(db, component_id)
    if not component:
        raise HTTPException(status_code=404, detail="Component not found")
    return {"message": "Component deleted"}

# Эндпоинты для Category
@app.post("/categories/")
def create_category_endpoint(category: dict, db: Session = Depends(get_db)):
    return create_category(db, category)

@app.get("/categories/")
def get_categories_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_categories(db, skip=skip, limit=limit)

@app.get("/categories/{category_id}")
def get_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@app.put("/categories/{category_id}")
def update_category_endpoint(category_id: int, category: dict, db: Session = Depends(get_db)):
    updated_category = update_category(db, category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@app.delete("/categories/{category_id}")
def delete_category_endpoint(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted"}

# Эндпоинты для Manufacturer
@app.post("/manufacturers/")
def create_manufacturer_endpoint(manufacturer: dict, db: Session = Depends(get_db)):
    return create_manufacturer(db, manufacturer)

@app.get("/manufacturers/")
def get_manufacturers_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_manufacturers(db, skip=skip, limit=limit)

@app.get("/manufacturers/{manufacturer_id}")
def get_manufacturer_endpoint(manufacturer_id: int, db: Session = Depends(get_db)):
    manufacturer = get_manufacturer(db, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return manufacturer

@app.put("/manufacturers/{manufacturer_id}")
def update_manufacturer_endpoint(manufacturer_id: int, manufacturer: dict, db: Session = Depends(get_db)):
    updated_manufacturer = update_manufacturer(db, manufacturer_id, manufacturer)
    if not updated_manufacturer:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return updated_manufacturer

@app.delete("/manufacturers/{manufacturer_id}")
def delete_manufacturer_endpoint(manufacturer_id: int, db: Session = Depends(get_db)):
    manufacturer = delete_manufacturer(db, manufacturer_id)
    if not manufacturer:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return {"message": "Manufacturer deleted"}

# Эндпоинты для Build
@app.post("/builds/")
def create_build_endpoint(build: dict, db: Session = Depends(get_db)):
    return create_build(db, build)

@app.get("/builds/")
def get_builds_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_builds(db, skip=skip, limit=limit)

@app.get("/builds/{build_id}")
def get_build_endpoint(build_id: int, db: Session = Depends(get_db)):
    build = get_build(db, build_id)
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    return build

@app.put("/builds/{build_id}")
def update_build_endpoint(build_id: int, build: dict, db: Session = Depends(get_db)):
    updated_build = update_build(db, build_id, build)
    if not updated_build:
        raise HTTPException(status_code=404, detail="Build not found")
    return updated_build

@app.delete("/builds/{build_id}")
def delete_build_endpoint(build_id: int, db: Session = Depends(get_db)):
    build = delete_build(db, build_id)
    if not build:
        raise HTTPException(status_code=404, detail="Build not found")
    return {"message": "Build deleted"}

# Эндпоинты для управления компонентами в сборке
@app.post("/builds/{build_id}/components/{component_id}")
def add_component_endpoint(build_id: int, component_id: int, db: Session = Depends(get_db)):
    build = add_component_to_build(db, build_id, component_id)
    if not build:
        raise HTTPException(status_code=404, detail="Build or Component not found")
    return build

@app.delete("/builds/{build_id}/components/{component_id}")
def remove_component_endpoint(build_id: int, component_id: int, db: Session = Depends(get_db)):
    build = remove_component_from_build(db, build_id, component_id)
    if not build:
        raise HTTPException(status_code=404, detail="Build or Component not found")
    return build

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
