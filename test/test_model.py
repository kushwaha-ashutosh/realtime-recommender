import os
import pickle
from services.model_service.app.model import Recommender


def test_model_loads():
    assert os.path.exists("model/artifacts/model.pkl")


def test_recommendations_returned():
    model = Recommender()
    recs = model.recommend(user_id=1)

    assert isinstance(recs, list)
    assert len(recs) > 0
    assert "item_id" in recs[0]
    assert "score" in recs[0]
