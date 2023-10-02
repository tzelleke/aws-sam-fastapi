from app.core.config import get_settings

summary = "A simple FastAPI application in AWS Lambda."

license = {
    "name": "MIT License",
    "identifier": "MIT",
}

_github_repo = "https://github.com/tzelleke/aws-sam-fastapi"

description = f"""
This is a simple FastAPI application that can be used as a template for other
applications.

It serves a **Vue 3 Single Page Application** as the applications frontend
from the `/` path.

The frontend communicates with the FastAPI backend.

[→ View the frontend for this application]({get_settings().root_path}/).

The application is deployed **serverless** in AWS Lambda using the
[Mangum adapter](https://mangum.io/).

You can find the source code on [GitHub]({_github_repo}).
"""
