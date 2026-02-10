import logging
from fastapi import FastAPI, HTTPException
from .schemas import RecommendationResponse
from .model import Recommender

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()
model = Recommender()


@app.on_event("startup")
def startup_event():
    logger.info("Recommendation service started")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/recommendations", response_model=RecommendationResponse)
def recommend(user_id: int):
    try:
        logger.info(f"Recommendation request for user {user_id}")
        recs = model.recommend(user_id)

        return {
            "user_id": user_id,
            "recommendations": recs
        }

    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        raise HTTPException(status_code=404, detail="User not found")
