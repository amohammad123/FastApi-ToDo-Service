from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional

class TaskBaseSchema(BaseModel):
    title: str = Field(..., max_length=150, min_length=5, description='title of the task')
    description: Optional[str] = Field(None, max_length=500, description='description of the task')
    is_completed :bool = Field(..., description='state of the task')

class TaskCreateSchema(TaskBaseSchema):
    pass

class TaskUpdateSchema(TaskBaseSchema):
    pass

class TaskResponseSchema(TaskBaseSchema):
    id: int = Field(..., description='id of the task')

    created_date: datetime = Field(..., description='created date of the task')
    updated_date: datetime = Field(..., description='updated date of the task')