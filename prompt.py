def create_prompt(purpose, tone, points):
    return f"""
You are an AI email writer.

Write based on:
Purpose: {purpose}
Tone: {tone}
Key Points: {points}

Give output in:
1. Professional Email
2. Follow-up Email
3. Short Version
4. 5 Subject Lines
"""