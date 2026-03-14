from langchain_core.prompts import PromptTemplate
from llm_setup import llm


def structured_plan_node(state: dict) -> dict:

    # prompt template defination
    prompt = PromptTemplate(
        input_variables=["topic", "level", "description", "web_search_result"],
        template="""
You are an expert educational planner.

The user wants to learn: {topic}
Their level is: {level}
Their goal/description: {description}

Here is some web information about this topic:
{web_search_result}

Based on all of this, create a structured learning plan.
The plan should have clear phases or modules.
For each module, list the subtopics to study.

Format your response like this:
Module 1: [Name]
- Subtopic 1
- Subtopic 2

Module 2: [Name]
- Subtopic 1
- Subtopic 2

Keep it simple and beginner-friendly.
"""
    )

    final_prompt = prompt.format(
        topic=state["topic"],
        level=state["level"],
        description=state["description"],
        web_search_result=state["web_search_result"]
    )

   
    response = llm.invoke(final_prompt)

    state["structured_plan"] = response.content

    return state
