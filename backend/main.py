from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend working"}

# from fastapi import FastAPI
# from routes.email import router

# app = FastAPI()

# app.include_router(router)

# @app.get("/")
# def root():
#     return {"message": "AI Email Triage API Running"}