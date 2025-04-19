


from src.main.app import app


@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API"}

if __name__ == "__main__":
    import uvicorn
    
    # Update the host and port if needed
    # uvicorn.run("src.main.app:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run("src.main.app:app", host="127.0.0.1", port=8000, reload=True)