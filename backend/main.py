# ============================================================
#  main.py
#  This is the main FastAPI server
#  It imports all nodes and runs them one by one
# ============================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from state import create_state
from chain import edu_chain
# from web_search_node import web_search_node
# from structured_plan_node import structured_plan_node
# from time_allocation_node import time_allocation_node

app = FastAPI()

app.add_middleware(          
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------------
# Input Model
# What the user sends to us
# ----------------------------
class UserInput(BaseModel):
    topic: str
    time_commitment: str   # e.g. "2 hours per day"
    description: str
    level: str             # e.g. "beginner", "intermediate", "advanced"


# ----------------------------
# Main API Endpoint
# Your project mate's backend calls this
# ----------------------------
@app.post("/generate-plan")
def generate_plan(user_input: UserInput):

    # Step 0: Create the state object
    state = create_state(
        topic=user_input.topic,
        time_commitment=user_input.time_commitment,
        description=user_input.description,
        level=user_input.level
    )

    result = edu_chain.invoke(state)

    # Step 4: Return the final result
    return {
        "topic": state["topic"],
        "level": state["level"],
        "time_commitment": state["time_commitment"],
        "final_plan": state["structured_plan_with_time_allocation"],
         "recommended_videos": state["recommended_videos"]
    }


# ----------------------------
# Run the server
# Open terminal and type: python main.py
# ----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
