"""
main.py
-------

Entry point for running the LangChain agent with Mem0-backed memory.

This module demonstrates:
- Interactive conversational usage with persistent memory
- Predefined example executions for testing and demos
- Comprehensive logging and graceful error handling

Execution Modes:
1. Interactive Chat: Continuous user-agent conversation
2. Example Queries: Predefined test scenarios using tools and APIs
"""

import traceback
from langchain.messages import HumanMessage

from agent import invoke_agent_with_memory
from cred import USER_ID
from prompt import system_prompt, user_query_1, user_query_2, user_query_3
from logger_config import setup_logger

logger = setup_logger(__name__)


def interactive_chat(user_id: str = USER_ID) -> None:
    """
    Run an interactive chat session with memory persistence.

    This function starts a REPL-style loop where the user can
    continuously interact with the agent. Each interaction
    is enhanced with long-term memory via Mem0 and logged
    for observability and debugging.

    Args:
        user_id (str): Unique identifier used to isolate
            and persist user-specific memory.

    Features:
        - Persistent memory across turns
        - Graceful handling of keyboard interrupts
        - Clean exit commands (`exit`, `quit`, `bye`)
        - Structured logging for every conversation turn

    Returns:
        None
    """
    logger.info("=" * 70)
    logger.info("INTERACTIVE CHAT MODE STARTED")
    logger.info(f"User ID: {user_id}")
    logger.info("=" * 70)

    # Display welcome banner
    print("\n" + "=" * 70)
    print(" AI Agent with Memory - Interactive Chat")
    print("=" * 70)
    print("\nAvailable commands:")
    print("  - Type your question normally to chat")
    print("  - 'exit', 'quit', 'bye' - End the conversation")
    print("  - 'clear' - View your conversation history")
    print("\nTools available: Math Calculator, Date Utility, Weather, Text Analysis")
    print("-" * 70 + "\n")

    conversation_count = 0

    # Main interactive loop
    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                print("  Please enter a message.\n")
                continue

            # Exit commands
            if user_input.lower() in {"exit", "quit", "bye", "q"}:
                print("\n Thanks for chatting! Your conversation has been saved to memory.")
                logger.info(
                    f"User ended conversation. Total turns: {conversation_count}"
                )
                break

            # Informational command
            if user_input.lower() == "clear":
                print(
                    f"\n You've had {conversation_count} conversation turns in this session.\n"
                )
                continue

            logger.info(
                f"[Turn {conversation_count + 1}] User query: {user_input}"
            )

            messages = {
                "messages": [
                    system_prompt,
                    HumanMessage(content=user_input),
                ]
            }

            print("\n Agent is thinking...", end="\r")

            response = invoke_agent_with_memory(messages, user_id)

            assistant_response = response["messages"][-1].content
            print("\r" + " " * 30 + "\r", end="")
            print(f"Agent: {assistant_response}\n")

            conversation_count += 1
            logger.info(
                f"[Turn {conversation_count}] Agent response delivered successfully"
            )

        except KeyboardInterrupt:
            print("\n\n  Interrupted by user (Ctrl+C)")
            print(" Exiting chat. Your conversation has been saved.\n")
            logger.warning(
                "Chat interrupted by KeyboardInterrupt (Ctrl+C)"
            )
            break

        except KeyError as exc:
            logger.error(
                f"[ERROR] KeyError - missing expected key: {exc}",
                exc_info=True,
            )
            print(
                f"\n Error: Missing data in response - {exc}"
            )
            print("Please try rephrasing your question.\n")

        except Exception as exc:
            logger.error(
                f"[ERROR] Unexpected error: {exc}",
                exc_info=True,
            )
            logger.debug(
                f"Full traceback:\n{traceback.format_exc()}"
            )
            print(f"\n An error occurred: {exc}")
            print("Please try again or type 'exit' to quit.\n")

    logger.info("=" * 70)
    logger.info("INTERACTIVE CHAT SESSION ENDED")
    logger.info(f"Total conversation turns: {conversation_count}")
    logger.info("=" * 70)


def run_example_queries() -> None:
    """
    Execute predefined example queries using the agent.

    This function runs a fixed set of demonstration queries
    showcasing:
    - Mathematical reasoning
    - Multi-tool orchestration
    - External API usage (e.g., weather)

    It is intended for:
    - Smoke testing
    - Demos
    - Debugging tool integrations

    Returns:
        None
    """
    logger.info("=" * 70)
    logger.info("RUNNING EXAMPLE QUERIES WITH MEMORY")
    logger.info("=" * 70)

    examples = [
        ("Math Calculation", user_query_1),
        ("Multi-Tool Usage", user_query_2),
        ("Weather API", user_query_3),
    ]

    for idx, (title, query) in enumerate(examples, start=1):
        try:
            logger.info(f"[EXAMPLE {idx}] Starting: {title}")
            logger.info(f"[EXAMPLE {idx}] Query: {query.content}")

            messages = {
                "messages": [
                    system_prompt,
                    query,
                ]
            }

            response = invoke_agent_with_memory(
                messages, user_id=USER_ID
            )

            print(f"\n--- Example {idx}: {title} ---")
            print(response["messages"][-1].content)

            logger.info(f"[EXAMPLE {idx}] Completed successfully")

        except Exception as exc:
            logger.error(
                f"[EXAMPLE {idx}] Failed: {exc}",
                exc_info=True,
            )
            print(f"\n--- Example {idx} FAILED ---")
            print(f"Error: {exc}\n")

    logger.info("=" * 70)
    logger.info("ALL EXAMPLE QUERIES COMPLETED")
    logger.info("=" * 70)


if __name__ == "__main__":
    """
    Application entry point.

    Prompts the user to select between:
    - Interactive chat mode
    - Example query execution

    Defaults to interactive mode on invalid input.
    """
    print("\n LangChain Agent with Mem0")
    print("Select mode:")
    print("  1. Interactive Chat (recommended)")
    print("  2. Run Example Queries")

    try:
        choice = input("\nEnter choice (1 or 2): ").strip()

        if choice == "1":
            interactive_chat(USER_ID)
        elif choice == "2":
            run_example_queries()
        else:
            print(" Invalid choice. Running interactive chat by default.")
            interactive_chat(USER_ID)

    except KeyboardInterrupt:
        print("\n\n Exiting application.")
        logger.info("Application terminated by user")
