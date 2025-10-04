from fastapi import FastAPI
from contextlib import asynccontextmanager

from tasks.routes import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('project started')
    yield
    print('project ended')


tags_metadata = [
    {
        'name': 'tasks',
        'description': 'Tasks API',
        'externalDocs': {
            'description': 'Tasks API',
            'url': 'https://google.com'
        }
    }
]

app = FastAPI(lifespan=lifespan, openapi_tags=tags_metadata,
              title="Todo application",
              summary="Deadpool's favorite app. Nuff said.",
              description='description ddddddddddd',
              version="0.0.1",
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": "Deadpoolio the Amazing",
                  "url": "http://x-force.example.com/contact/",
                  "email": "dp@x-force.example.com",
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              )

app.include_router(tasks_router)
