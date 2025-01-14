from typing import List, Tuple
from agent.graph import build_graph

graph = build_graph()
config = {"configurable": {"thread_id": 1}}


class ChatBot:
    """
    A class to handle chatbot interactions by utilizing a pre-defined agent graph. The chatbot processes
    user messages, generates appropriate responses.

    Methods:
        respond(chatbot: List, message: str) -> Tuple:
            Processes the user message through the agent graph, generates a response, appends it to the chat history,
            and writes the chat history to a file.
    """
    @staticmethod
    def respond(chatbot: List, message: str) -> Tuple:
        """
        Processes a user message using the agent graph, generates a response, and appends it to the chat history.
        The chat history is also saved to a memory file for future reference.

        Args:
            chatbot (List): A list representing the chatbot conversation history. Each entry is a tuple of the user message and the bot response.
            message (str): The user message to process.

        Returns:
            Tuple: Returns an empty string (representing the new user input placeholder) and the updated conversation history.
        """
        # The config is the **second positional argument** to stream() or invoke()!
        events = graph.stream(
            # {"messages": [("company", message)]}, config, stream_mode="values"
            {"company": message}, config, stream_mode="values"
        )
        print(f'======> {events}')
        for event in events:
            event["info"][-1].pretty_print()

        chatbot.append(
            (message, event["info"][-1].content))

        return "", chatbot
