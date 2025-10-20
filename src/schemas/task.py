"""
Pydantic schemas for Task validation and serialization.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    """Base schema for Task with common attributes."""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    completed: bool = False
    priority: str = Field(default="medium", pattern="^(low|medium|high)$")


class TaskCreate(TaskBase):
    """Schema for creating a new task."""
    pass


class TaskUpdate(BaseModel):
    """Schema for updating a task (all fields optional)."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[str] = Field(None, pattern="^(low|medium|high)$")


class TaskResponse(TaskBase):
    """Schema for task response."""
    id: int
    user_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)
