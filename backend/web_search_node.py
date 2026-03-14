from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()


def web_search_node(state: dict) -> dict: 
    query = f"{state['topic']} learning plan for {state['level']} level"
 
    result = search_tool.run(query)
 
    state["web_search_result"] = result

    return state
