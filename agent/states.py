from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class File(BaseModel):
    path: str = Field(
        description="The path of the file to be created or modified, e.g. 'src/App.js', 'src/components/Navbar.js', 'index.html")
    purpose: str = Field(
        description="The purpose of the file to be created, e.g. 'main application logic', 'data preprocessing module' etc. basically to understand the purpose of the files like if it is a backend file or frontend file or config file etc.")

class Plan(BaseModel):
    name: str = Field(
        description="The name of the app to be built")
    description : str = Field(
        description="A oneline description of the app to be built, e.g. 'A social media app for pet owners'")
    techstack: list[str] = Field(
        description="A list of technologies to be used, e.g. ['React', 'Node.js', 'PostgreSQL']")
    features: list[str] = Field(
        description="A list of features to be implemented, e.g. ['User authentication', 'Profile creation', 'Post creation', 'Commenting']")
    files: list[File] = Field(
        description="A list of all the files to be created, e.g. ['src/App.js', 'src/components/Navbar.js', 'src/components/Post.js']")

class ImplementationTask(BaseModel):
    file_path: str = Field(
        description="The path of the file to be created or modified, e.g. 'src/App.js', 'src/components/Navbar.js', 'index.html")
    task_description: str = Field(
        description="A detailed description of the implementation task, specifying exactly what to implement, naming the exact variables, functions, classes, or components to be created or modified, mentioning how this task depends on or will be used by previous tasks, and including integration details like imports, expected function signatures, data flow between components, etc.")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(
        description="A list of implementation tasks, ordered so that the dependencies are implemented first. Each task must be self-contained but also carry forward the relevant context from previous tasks.")
    model_config = ConfigDict(extra="allow")

class CoderState(BaseModel):
    task_plan: TaskPlan = Field(
        description="The task plan to use for this coder agent to implement.")
    current_step_idx: int = Field(
        description="The index of the current step in the implementation steps.")
    current_file_content: Optional[str] = Field(None,
        description="The current content of the file being worked or edited on, if any.")