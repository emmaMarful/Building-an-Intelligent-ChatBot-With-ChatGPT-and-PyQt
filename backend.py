import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me a joke about manchester united")
    print(response)