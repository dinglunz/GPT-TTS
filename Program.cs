using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;
using System;
using System.Threading.Tasks;

namespace GPT_TTS
{
    class Program
    {
        static async Task Main() {
            await SynthesizeAudioAsync();
        }

        static async Task SynthesizeAudioAsync() {
            var speechConfig = SpeechConfig.FromSubscription("e3761f73794c4924832c44e4f9414f30", "eastus");
            speechConfig.SpeechSynthesisLanguage = "zh-CH"; 
            speechConfig.SpeechSynthesisVoiceName = "zh-CN-XiaoxiaoNeural";

            var audioConfig = AudioConfig.FromWavFileOutput(@"C:\Users\wsqua\Desktop\azure-tts-output.wav");

            using var speechSynthesizer = new SpeechSynthesizer(speechConfig, audioConfig);
            await speechSynthesizer.SpeakTextAsync("你好，这是必应。我希望这些建议对你有所帮助。加油！");
        }

    }
}