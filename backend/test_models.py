from backend.app.core.database import Base
from backend.app.models import User, Project, Task

print("Registered models:")

for table in Base.metadata.sorted_tables:
    print(f"- {table.name}")

print("\nAll models loaded successfully!")