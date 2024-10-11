from sqlalchemy.schema import CreateTable
from app.models.task import Task
from app.models.user import User


print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))
