from openai import OpenAI
from decouple import config

client = OpenAI(api_key=config("OPENAI_API_KEY"))


def get_ai_response(session):
    """
    Gather all the messages from the DB for this session,
    format them as OpenAI wants, then call the API and get the reply.
    """

    # 1. Get all messages in chronological order
    messages = session.messages.order_by("created_at")

    # 2. Format them for OpenAI
    openai_msgs = [{"role": msg.role, "content": msg.content} for msg in messages]

    # 3. Call the API using the new SDK format
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=openai_msgs,
        temperature=0.7,
        max_tokens=200,
    )

    # 4. Extract the assistant's reply
    reply = response.choices[0].message.content
    return reply
