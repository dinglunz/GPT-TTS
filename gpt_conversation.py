import openai

API_KEY = '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'
openai.api_key = API_KEY
model_id = 'gpt-3.5-turbo'

def TrackContext(conversation):
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    # # Additional info
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)

    return conversation


def GenResponse(conversation, user_input):
    conversation.append({'role': 'user', 'content': user_input})
    conversation = TrackContext(conversation)
    return conversation[-1]['content']


