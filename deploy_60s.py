from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SimpleModel:
    def predict(self, features):
        risk = sum(features) / len(features) if features else 0
        return {
            "fraud_probability": float(risk),
            "is_fraud": risk > 0.7,
            "confidence": min(abs(risk - 0.5) * 2, 1.0)
        }

model = SimpleModel()

class PredictionRequest(BaseModel):
    features: list

@app.get("/")
def health():
    return {"status": "healthy", "message": "Model deployed!"}

@app.post("/predict")
def predict(request: PredictionRequest):
    return model.predict(request.features)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
