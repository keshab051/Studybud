def create_state(topic, time_commitment, description, level):
    return {
        "topic": topic,
        "time_commitment": time_commitment,
        "description": description,
        "level": level,
        "web_search_result": "",                     
        "structured_plan": "",                      
        "structured_plan_with_time_allocation": ""   
    }
