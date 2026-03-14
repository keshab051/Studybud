from web_search_node import web_search_node
from structured_plan_node import structured_plan_node
from time_allocation_node import time_allocation_node
from langchain_core.runnables import RunnableLambda

web_search = RunnableLambda(web_search_node)
structured_plan = RunnableLambda(structured_plan_node)
time_allocation = RunnableLambda(time_allocation_node)

edu_chain = web_search | structured_plan  | time_allocation 
