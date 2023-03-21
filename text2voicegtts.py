from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(text_list, output_file):
    # Create a list of gTTS audio segments for each text string and language
    audio_segments = []
    for text, lang in text_list:
        tts = gTTS(text, lang=lang)
        temp_file = f"{text[:10]}.mp3" # create a temporary file name
        tts.save(temp_file)
        audio_segments.append(AudioSegment.from_mp3(temp_file))
    
    # Concatenate the audio segments into a single audio file
    combined_audio = audio_segments[0]
    for segment in audio_segments[1:]:
        combined_audio = combined_audio + segment
    
    # Export the combined audio to an MP3 file
    combined_audio.export(output_file, format="mp3")
    
    # Delete the temporary audio files
    for temp_file in os.listdir():
        if temp_file.endswith(".mp3") and temp_file.startswith("try") == False:
            os.remove(temp_file)


text_list = [("Hello, how are you?", 'en'), ("Comment ça va?", 'fr'), ("你好吗？", 'zh')]
paragraph = [("U.S. stocks gave up nearly all of their gains for the year Friday, \
             extending a weeklong slump of nearly 5%, following the collapse of SVB Financial  (SIVB) - \
             Get Free Report, a California-based tech lender that's shaken confidence in the domestic financial sector \
             and sent investors fleeing from risk markets around the world.  Meow","en"),
            ("Silicon Valley Bank's collapse, confirmed Friday by the effective takeover of its \
            $209 billion in assets by the Federal Deposit Insurance Corporation (FDIC) at the behest \
            of California regulators, could be one of the largest in U.S. history and the biggest since Washington Mutual in 2008.\
            SVB Financial shares, which plunged 60.4% yesterday -- the most in two decades --\
            were marked 45.5% lower in pre-market trading before being halted by Nasdaq officials prior to the opening bell.","en"),
            ("你好吗？","zh"),
            (" Comment ça va?","fr")]

text_to_speech(paragraph,"try_file.mp3")