from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified.")
    purpose: str = Field(description="The purpose of the file, e.g. 'main application logic', 'data processing module', etc.")


class Plan(BaseModel):
    name: str = Field(description="The naame of the app to be built.")
    description: str = Field(description="A brief description of the app to be built.")
    techstack: str = Field(description="The tech stack to be used for the app.")
    features: list[str] = Field(description="A list of features that the app should have, e.g. 'user_authentication', 'data_visualization', etc.")
    files: list[File] = Field(description="A list of files to be created, each with a 'path' and 'purpose'.")

# Class for each implementation task
class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified.")
    task_description: str = Field(description="A brief description of the task to be performed on the file, e.g. 'add user authenttication', 'implement data processing logic', etc.")

# Class on the implementation steps for all the tasks.
class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(description="A list of stps to be taken to implement the task.")
    model_config = ConfigDict(extra="allow")

class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description = "The plan for the task to be implemented.")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")