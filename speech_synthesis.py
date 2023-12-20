import os
import azure.cognitiveservices.speech as speechsdk
from gpt_conversation import *


# Global variables
SPEECH_KEY = 'e3761f73794c4924832c44e4f9414f30'
SPEECH_REGION = 'eastus'

# Syntehsis from text method
def SynFromText(text):
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("GPT-3.5 Turbo: {}\n".format(text))
        # print("Output file saved at {}".format(output_file_path))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))


# Basic variables
voice_name = 'zh-CN-XiaoxiaoNeural'
output_mode = 'speaker'

# Set key and region
speech_config = speechsdk.SpeechConfig(SPEECH_KEY, SPEECH_REGION)

# Set output file path
output_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "speech_output.wav")

# Set output mode
if output_mode == 'speaker':
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
elif output_mode == 'file':
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file_path)

# Set language and voice
speech_config.speech_synthesis_voice_name = voice_name

# Initialize speech syntehsizer
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Initialize conversation
conversation = []
# # System settings (optional)
# conversation.append({'role': 'user', 'content': user_input})
# conversation = TrackContext(conversation)

input_text_list = []

while True:
    user_input_text = input("User (type STOP to end): ")
    print()
    if user_input_text.upper() == 'STOP':
        break

    input_text_list.append(user_input_text)
    response_text = GenResponse(conversation, user_input_text)
    SynFromText(response_text.lstrip())
