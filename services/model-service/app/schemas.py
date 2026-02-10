from pydantic import BaseModel
from typing import List


class Recommendation(BaseModel):
    item_id: int
    score: float


class RecommendationResponse(BaseModel):
    user_id: int
    recommendations: List[Recommendation]
