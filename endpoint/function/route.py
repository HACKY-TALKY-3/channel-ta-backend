from fastapi import APIRouter
from endpoint.function.entity import Method
import requests
import json
import dotenv


config = dotenv.dotenv_values('.env')


router = APIRouter(
    prefix="/function",
    tags=["function"]
)


@router.get('/')
def index():
    return {'message': 'Hello World'}



@router.put("/", summary="Receive Function Calling")
def get_function_calling(notes: Method) -> dict:
    method = notes.method

    if method == 'helloWorld':
        chat_id = notes.params['chat']['id']

        channel_id = notes.context.channel['id']

        token = requests.put(
            url="https://app-store-api.channel.io/general/v1/native/functions",
            data=json.dumps({
                "method": "issueToken",
                "params": {
                    "secret": config['SECRET_TOKEN'],
                    'channelId': channel_id
                }
            })
        ).json()['result']

        header = {
            'x-access-token': token,
        }

        data = {
            "method": "writeGroupMessage",
            "params":   {
            "channelId": channel_id,
            "groupId": chat_id,
                "dto": {
                    "plainText": "hello world!",
                "botName": "wow"
                },
            }
        }

        response = requests.put(
            url='https://app-store-api.channel.io/general/v1/native/functions',
            headers=header,
            data=json.dumps(data)
        )

        print(response.json())

        response = {
            "type": "wam",
            "attributes": {
                "appId": "app id",
                "name": "name of the wam",
                "wamArgs": {}
	        }
        }

    return response

