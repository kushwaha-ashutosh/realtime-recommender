# Real-Time Recommendation System (Streaming ML Pipeline)

A production-style real-time recommendation system that ingests user events, updates features via a streaming pipeline, and serves personalized recommendations through a scalable API.

This project demonstrates end-to-end ownership of:

- Event-driven architecture
- Streaming data pipelines
- Feature engineering
- Model training
- Online inference
- API deployment
- Testing and production readiness

---

## Architecture Overview

```
User Events
    ↓
Event Producer
    ↓
Streaming Pipeline (Apache Beam)
    ↓
Feature Store (SQLite / BigQuery)
    ↓
Model Service (FastAPI)
    ↓
Recommendation API
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10 |
| Streaming | Apache Beam |
| Feature Store | SQLite (local), BigQuery (prod) |
| Model | Embedding-based recommender |
| API | FastAPI |
| Containerization | Docker |
| Cloud | Google Cloud Run |
| CI/CD | GitHub Actions |
| Testing | Pytest |

---

## Features

- Real-time event ingestion
- Streaming feature updates
- Embedding-based recommendation model
- Stateless inference API
- Structured logging
- Environment-based configuration
- Unit and integration tests
- Container-ready for Cloud Run deployment

---

## Project Structure

```
realtime-recommender/
│
├── model/
│   ├── train.py
│   └── artifacts/
│
├── services/
│   ├── event-producer/
│   ├── streaming-pipeline/
│   └── model-service/
│
├── tests/
├── requirements.txt
└── README.md
```

---

## Local Setup Instructions

### 1. Create virtual environment

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python model/train.py
```

### 4. Start event producer

```bash
python services/event-producer/producer.py
```

### 5. Run streaming pipeline

```bash
python services/streaming-pipeline/pipeline.py
```

This creates:

```
features.db
```

### 6. Start the API

```bash
uvicorn services.model-service.app.main:app --reload
```

### 7. Test endpoints

**Health:**

```
http://127.0.0.1:8000/health
```

**Recommendations:**

```
http://127.0.0.1:8000/recommendations?user_id=10
```

---

## Running Tests

```bash
pytest
```

---

## Deployment (Cloud Run)

### Build container

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/recommender-api
```

### Deploy

```bash
gcloud run deploy recommender-api \
  --image gcr.io/PROJECT_ID/recommender-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Design Trade-offs

| Decision | Chosen | Alternative | Reason |
|----------|--------|-------------|--------|
| Streaming pipeline | Apache Beam | Batch jobs | Real-time personalization |
| Feature store | BigQuery | Redis/Feast | Simpler architecture |
| Model type | Embedding-based | Deep learning | Lower latency, easier deployment |
| Inference service | Cloud Run | GKE | Lower operational overhead |

---

## Failure Handling

| Scenario | Mitigation |
|----------|------------|
| Missing user features | Cold-start recommendations |
| Model load failure | API fails fast at startup |
| Pipeline failure | Auto-restart in Dataflow |
| Traffic spikes | Cloud Run auto-scaling |

---

## Limitations

- Uses synthetic data instead of real user behavior
- Feature store is SQLite locally (not distributed)
- No A/B testing or ranking layer
- Model retraining not automated

---

## Future Improvements

- Replace SQLite with Redis or BigQuery online store
- Add real-time feature caching
- Implement ranking model
- Add model retraining pipeline
- Introduce A/B testing framework
- Add monitoring dashboards

---

## Key Learning Outcomes

- Designed a real-time streaming ML architecture
- Built end-to-end data → model → API pipeline
- Deployed stateless inference service
- Implemented production-style logging and testing

---

## Author

Your Name  
GitHub: https://github.com/kushwaha-ashutosh

---

## License

MIT