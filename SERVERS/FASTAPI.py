from fastapi import FastAPI

app = FastAPI()


DATAS = {
    '0123':{"STATS": "NO","BAL":"1000"},
    '0827': {"STATS": "NO","BAL":"1000"},
    "1234":{"STATS": "YES","BAL":"121"},
    "12345":{"STATS": "YES","BAL":"300"},
    "54321":{"STATS": "NO","BAL":"0"},
    "123321":{"STATS": "NO","BAL":"0"},
    "1111":{"STATS": "YES","BAL":"0"}
    
    
}

 
@app.get("/")
async def first_api():
    return DATAS
 
@app.get("/datas/mydatas")
async def myfavebal():
    return{"BAL": "My Balance"}

@app.get("/datas/{BAL_id}")
async def read_api(BAL_id):
    return{"BAL":BAL_id}