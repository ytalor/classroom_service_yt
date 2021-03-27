import os
import uvicorn
from dotenv import load_dotenv


config = os.environ.get("CONFIG", "dev")


if __name__ == "__main__":

    if config == "dev":
        load_dotenv()

    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)