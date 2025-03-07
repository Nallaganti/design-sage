import openai
from typing import List

class OpenAIService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = openai.OpenAI(api_key=api_key)  # ✅ Correct way to initialize client

    async def generate_feed_design(self, prompt: str) -> str:
        """
        Generate feed design using OpenAI API
        """
        try:
            response = self.client.chat.completions.create(  # ✅ Correct API method
                model="gpt-4o-mini",  # ✅ Use a valid model
                messages=[
                    {"role": "system", "content": "You are an Interviewer. Explain the flowchart."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating feed design: {str(e)}"

    # async def get_feed_suggestions(self, current_design: str) -> List[str]:
    #     """
    #     Get suggestions for improving the feed design
    #     """
    #     try:
    #         response = await openai.ChatCompletion.acreate(
    #             model="gpt-3.5-turbo",
    #             messages=[
    #                 {"role": "system", "content": "You are a helpful assistant that provides feed design suggestions."},
    #                 {"role": "user", "content": f"Please provide suggestions to improve this feed design: {current_design}"}
    #             ]
    #         )
    #         suggestions = response.choices[0].message.content.split('\n')
    #         return [s.strip() for s in suggestions if s.strip()]
    #     except Exception as e:
    #         return [f"Error getting suggestions: {str(e)}"] 