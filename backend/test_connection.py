from backend.app.core.database import engine

try:
    with engine.connect() as connection:
        print("Successfully connected to DevTrackDB!")
except Exception as error:
    print("Database connection failed:")
    print(error)