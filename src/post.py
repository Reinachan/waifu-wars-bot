import requests

from src.constants import USERNAME, PASSWORD, KITSUID  # type: ignore

req = requests.Session()


def post_text(round: str | int, battle: str | int) -> str:
    return f"""
Waifu War 2022
Round “{round}”
Battle “{battle}”
https://waifuwars.madao-king.xyz/

Info:
- We will be holding 3 battles a day, each from a different Tier
- You need to login using your Kitsu account to be able to vote
- Please be respectful for other people's choices
- This battle will last 24 hours
- Results are viewable on the results page of the site
- If you are experiencing technical difficulties please contact Gakamine
- Discord link: https://discord.gg/WYvcaFnF3c
"""


def authenticate() -> str | None:
    res = req.post('https://kitsu.io/api/oauth/token',
                   json={
                       "grant_type": "password",
                       "username": USERNAME,
                       "password": PASSWORD
                   },
                   headers={
                       "Content-Type": "application/json"
                   })

    if not res.ok:
        print('failed authenticating')
        return None

    return res.json()['access_token']


def post_image(token: str):
    image_response = req.post(
        url='https://kitsu.io/api/edge/uploads/_bulk',
        files={
            "files[]": ('battle.jpg', open('generated/battle.jpg', 'rb'))
        },
        headers={
            "Authorization": f"Bearer {token}"
        },
        data={
            'upload': ''
        }
    )

    if not image_response.ok:
        print("failed uploading image")
        return False

    return image_response.json()['data'][0]["id"]


def post(round=1, battle=1) -> bool:

    token = authenticate()

    if not token:
        return False

    battle_post = {
        "data": {
            "attributes": {
                "content": post_text(round, battle),
                "spoiler": False
            },
            "relationships": {
                "uploads": {
                    "data": [
                        {
                            "id": post_image(token),
                            "type": 'uploads'
                        }
                    ]
                },
                "user": {
                    "data": {
                        "id": KITSUID,
                        "type": "users"
                    }
                }
            },
            "type": "posts"
        }
    }

    req.post('https://kitsu.io/api/edge/posts',
             json=battle_post,
             headers={
                 "Authorization": f"Bearer {token}",
                 "Content-Type": 'application/vnd.api+json'
             })

    return True
