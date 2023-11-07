import requests
from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError

from models.models import Quest
from db import session

app = FastAPI(title='Quiz questions')


def get_quests(count: int) -> dict: 
    """receiving questions about the API"""

    params = {"count": count}
    url = "https://jservice.io/api/random"
    result = requests.get(url=url, params=params)
    return result.json()[0]


def is_saving_quest(data: dict) -> bool:
    """saving questions in database"""
    
    new_quest = Quest()
    fields = ["id", "question", "answer", "created_at"]

    for field in fields:
        setattr(new_quest, field, data[field])

    try:
        session.add(new_quest)
        session.commit()
        return True
    except IntegrityError:
        return False


@app.post("/questions_num/{count}")
def quiz_question(count: int):
    check = count
    while check != 0:
        quest_data = get_quests(1)
        if is_saving_quest(data=quest_data):
            check -= 1
    last_quest = session.query(Quest).order_by(Quest.added_at.desc()).first()
    answer = session.query(Quest).order_by(Quest.added_at.desc()).filter(Quest.added_at < last_quest.added_at).first()
    return {'answer': answer}
