import pickle
import numpy as np

import os

MODEL_PATH = os.getenv("MODEL_PATH", "model/artifacts/model.pkl")


class Recommender:
    def __init__(self):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)

        self.user_emb = model["user_embeddings"]
        self.item_emb = model["item_embeddings"]

    def recommend(self, user_id, top_k=5):
        user_vector = self.user_emb[user_id]
        scores = self.item_emb @ user_vector

        top_items = np.argsort(scores)[-top_k:][::-1]

        return [
            {"item_id": int(i), "score": float(scores[i])}
            for i in top_items
        ]
