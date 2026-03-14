from langchain_core.prompts import PromptTemplate
from llm_setup import llm


def time_allocation_node(state: dict) -> dict:

    prompt = PromptTemplate(
        input_variables=["structured_plan", "time_commitment"],
        template="""
You are an educational time planner.

The user can dedicate: {time_commitment} to studying.

Here is their learning plan:
{structured_plan}

Your job is to allocate time to each module based on the user's time commitment.
Be realistic and balanced.

Format your response like this:
Module 1: [Name] — Estimated Time: X days/hours
- Subtopic 1
- Subtopic 2

Module 2: [Name] — Estimated Time: X days/hours
- Subtopic 1
- Subtopic 2

At the end, write the total estimated time to complete the full plan.
"""
    )

    final_prompt = prompt.format(
        structured_plan=state["structured_plan"],
        time_commitment=state["time_commitment"]
    )
 
    response = llm.invoke(final_prompt) 
    state["structured_plan_with_time_allocation"] = response.content

    return state