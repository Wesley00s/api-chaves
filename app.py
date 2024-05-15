import uvicorn
from starlette.middleware.cors import CORSMiddleware

from controllers import app
from database import *


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    create_table_chave()
    create_table_registro()
    create_table_user()

    uvicorn.run(app, host="192.168.0.128", port=8080)
