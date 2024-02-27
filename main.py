from fastapi import FastAPI
from os import listdir
from os.path import isfile, join
import importlib
import uvicorn
from config.db import MySQLConnector

app = FastAPI(
    title="Sample CRUD",
    description="A sample CRUD to inherit this into ypur app.",
    version="1.0.0"
)
mysql_connector = MySQLConnector()

# Dynamically import all route files from the routes directory
routes_dir = "api/routers"
route_files = [f for f in listdir(routes_dir) if isfile(join(routes_dir, f)) and f.endswith(".py")]

for route_file in route_files:
    module_name = f"api.routers.{route_file[:-3]}"  # Strip ".py" extension
    print('module_name',module_name)
    route_module = importlib.import_module(module_name)
    app.include_router(route_module.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
