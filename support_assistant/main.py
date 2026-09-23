#import libraries
from fastapi import FastAPI

from graph import graph
from models import AskRequest, AskResponse


app = FastAPI(title="Zepto Support Assistant")

# Ask endpoint

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    result = graph.invoke({
        "query": request.query,
        "intent": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0
    })

    return AskResponse(
        answer=result["answer"],
        sources=result["sources"],
        confidence=result["confidence"]
    )

# Run FastAPI server

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
