# deploy-ml-fastapi
Deploy ml model with fastapi and docker container.
## How to use ?
1. create and activate a virtual env 
```
python -m venv virtual-env
source virtual-env/bin/activate

```
2. Install requirements
```
pip install -r requirements.txt
``` 
3. Generate model dump (optional)

```
python models/generate_pipeline.py
``` 
4. Run api server 
*You can get more information on uvicorn* [here](https://www.uvicorn.org/) and FastApi [here](https://fastapi.tiangolo.com/) 
```
uvicorn main:app  --app-dir api
``` 