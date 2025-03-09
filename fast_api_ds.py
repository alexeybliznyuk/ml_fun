from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import requests


app = FastAPI()


class ApiModel(BaseModel):
    data: dict

@app.post("/structure", response_model=ApiModel)
async def ds_service(request: Request):

    json_data = await request.json()
    print(json_data)
    print(type(json_data))

    api_key = "sk-GaUWHpST0Bb7wtTztNsVi88RDrM2Q26n"

# PROXY_API_KEY = os.getenv(api_key)

    url = "https://api.proxyapi.ru/deepseek/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    user_input = json_data
    
    system_prompt = "Предложи структуру курса по этому опроснику."
    conversation = [ 
        {"role": "system", "content": f"{system_prompt}"}
    ]

    conversation = conversation + user_input

    data = {
        "model": "deepseek-chat",
        "messages": conversation
    }
        

    response = requests.post(url, headers=headers, json=data)

    json_payload = response.json()

    return {"data": json_payload}
    # return {"data": data,
    #         "DS_answer" : json_payload}
    # return {"data":response.json}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
