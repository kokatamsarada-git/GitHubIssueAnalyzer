
from ast import main
import asyncio
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from graph.graph_builder import graph


async def main():
    messages = []
    print("Github issue analyser and email notifier (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        
        if not user_input or user_input.lower() in ("quit", "exit"):
            break
        
        messages.append(HumanMessage(content=user_input))
        # state = {
        #     "user_query": user_input,
        #     "owner": "",
        #     "repo": "",
        #     "issue_number": 0,
        #     "issue": "",
        #     "analysis": "",
        #     "email_status": ""
        # }

        result = await graph.ainvoke({"messages": messages})
       # print(result["messages"])
        messages = result["messages"]
        #print(f"\n Email Status: {result['email_status']}\n")
        print(f"\nAgent: {messages[-1].content}\n")


if __name__ == "__main__":
    asyncio.run(main())