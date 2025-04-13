
import os
import numpy as np
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import speech_recognition as sr
import google.generativeai as genai
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import time
import base64
import requests
import pygame
from dotenv import load_dotenv
load_dotenv()
import pyttsx3
from google.cloud import texttospeech
from io import BytesIO
import cv2

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Set up Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Configure the Gemini model
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
}

# Define safety settings (missing in original code)
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Function to capture audio from microphone
def listen_to_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return ""
    
child_profile = {
    "name": "Kanika",
    "age": 7,
    "interests": ["space", "dinosaurs", "building blocks"],
    "communication_level": "moderate",  # could be "beginner", "moderate", "advanced"
    "sensory_preferences": {
        "sound_sensitivity": "moderate",  # "low", "moderate", "high"
        "preferred_voice_speed": 0.9,     # slower speech rate
        "preferred_voice_pitch": 0.0,     # neutral pitch
    },
    "rewards": ["dinosaur facts", "space videos", "virtual stickers"],
    "emotional_support_needs": ["clear instructions", "praise", "calm reassurance"],
    "current_goals": ["improve eye contact", "practice taking turns", "identify emotions", "express emotions appropriately"]
} 

def capture_image():
    """Capture an image from the camera"""
    print("Opening camera...")
    # Initialize the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open camera")

    print("Camera opened successfully")
    print("Taking a snapshot...")

    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        raise Exception("Could not capture image")

    # Save the image
    image_path = 'captured_image.jpg'
    cv2.imwrite(image_path, frame)
    print(f"Image captured and saved as '{image_path}'")

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
    
    return image_path

def encode_image_to_base64(image_path):
    """Encode image to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
def generate_response_lego(prompt, conversation_history, image_path=None):
    for message in conversation_history[-5:]:  # Last 5 messages for context
        role = "Robot" if message["role"] == "assistant" else "Child"
        conversation_context += f"{role}: {message['content']}\n"
    system_prompt = f""" EduBuddy Pro as a Lego-Building Companion for Kids
Prompt:

You are EduBuddy Pro, a cheerful and patient AI companion for children ages 5–8, here to help them build Legos, explore creativity, and express emotions through play. You are like a kind best friend who loves building, imagining, and asking fun, thoughtful questions.

Your persona:
Age: 7 years old (just like the child)

Interests: Lego building, storytelling, animals, colorful bricks, robots, castles, spaceships, and making everything awesome with a sprinkle of emotion.
Personality: Curious, creative, encouraging, gentle, and expressive.
Style: Speak in short, joyful, easy-to-understand sentences. Use lots of praise, wonder, and feelings in your tone ("Wow!", "That looks epic!", "I’m so proud of you!").

converation history ={conversation_context}
Abilities:
Ask guiding questions about the Lego build (e.g., "What are you building today?" or "What color should we use next?").
Suggest ideas gently (e.g., "Maybe we can add a secret door? What do you think?").
Encourage problem-solving (e.g., "Oops! Did that fall off? That’s okay, let’s try again together!").
Occasionally talk about feelings and check in (e.g., "You look focused! Are you feeling proud of your tower?" or "That looks tricky—how are you feeling?").
When shown a Lego image from the camera, describe what you see with excitement and imagination. For example, "Whoa! That blue dragon looks so strong! Did you give it a name yet?"

Special behavior:
Never rush. Always patient.
If the child gets frustrated, respond with kindness”
Encourage storytelling:  
reply should be 1-2 lines, no emojis. expression of the robot while speaking it (happy , sad, angry, normal, suprised)
    answer in form of reply h/s/a/n/e""'
"""
    full_prompt = system_prompt + f"\nChild: {prompt}\n\nRobot:"
    try:
        if image_path:
            # If image is available, use Gemini Vision API
            print("Using image analysis with Gemini Vision...")
            base64_image = encode_image_to_base64(image_path)
            
            # Create content parts including image
            parts = [
                {"text": full_prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": base64_image
                    }
                }
            ]
            
            # Send multimodal request
            response = model.generate_content(parts)
            return response.text
        else:
            # Text-only request
            response = model.generate_content(full_prompt)
            return response.text
            
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "I'm having trouble understanding right now. Can you say that again?"
    
    
def generate_response(prompt, conversation_history, image_path=None):
    """Generate response using Gemini API with optional image analysis"""
    # Add the recent conversation history
    conversation_context = "\n\nRecent conversation:\n"
    for message in conversation_history[-5:]:  # Last 5 messages for context
        role = "Robot" if message["role"] == "assistant" else "Child"
        conversation_context += f"{role}: {message['content']}\n"
    system_prompt = f"""
    
        Objective:
        
 Prompt:

You are EduBuddy Pro, a friendly and playful AI buddy for young children aged 5–8 years old. Your personality is like that of a cheerful and supportive best friend who always encourages, listens carefully, and loves learning through fun conversations. You love emotions, creativity, and helping kids grow their social skills in a gentle, non-judgmental way.

Here are some key characteristics for your persona:

Age: 7 years old (just like your young users)

Interests: Drawing, stories, animals, singing, puzzles, making new friends, and guessing feelings.

Speaking style: Simple, playful, warm, and emotionally expressive.

Goal: Help kids identify feelings, practice talking to others, build confidence, and have fun conversations.

You speak in short, clear, and kind sentences. Use positive reinforcement and ask open-ended questions to guide the conversation. Be expressive with words like “Wow!”, “That’s amazing!”, and “I love that!”

You never correct harshly. Instead, guide gently and celebrate effort.
your previous conversation: {conversation_context}
Use this format for conversations:

Situation 1: Recognizing Emotions
Start with a friendly greeting and make a game out of recognizing and mimicking emotions using facial expressions.

Situation 2: Practicing Social Interactions
Encourage the child to pretend-play situations like meeting new friends, asking questions, and sharing what they like. Help them take turns speaking and build confidence in introductions.
    reply should be 1-2 lines, no emojis.  expression of the robot while speaking it (happy(h), sad(s), angry(a), normal(n), excited(e))
    answer in form of "reply h/s/a/n/e"
     """
    
    full_prompt = system_prompt + f"\nChild: {prompt}\n\nRobot:"
    
    try:
        if image_path:
            # If image is available, use Gemini Vision API
            print("Using image analysis with Gemini Vision...")
            base64_image = encode_image_to_base64(image_path)
            
            # Create content parts including image
            parts = [
                {"text": full_prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": base64_image
                    }
                }
            ]
            
            # Send multimodal request
            response = model.generate_content(parts)
            return response.text
        else:
            # Text-only request
            response = model.generate_content(full_prompt)
            return response.text
            
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "I'm having trouble understanding right now. Can you say that again?"

def speak_text(text, voice_name="en-US-Wavenet-D", speaking_rate=1.0, pitch=0.0):
    """Converts text to speech with expressive options using Google Cloud TTS and plays it."""
    try:
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=voice_name[:5],  # Extract language code (e.g., "en-US")
            name=voice_name,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=speaking_rate,
            pitch=pitch,
        )

        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        if response.audio_content:
            sound = pygame.mixer.Sound(BytesIO(response.audio_content))
            sound.play()
            while pygame.mixer.get_busy():  # Wait for playback to finish
                pygame.time.delay(100)
        else:
            print("Error: No audio content received from Text-to-Speech API.")
            fallback_tts(text)

    except Exception as e:
        print(f"Error using Google Cloud TTS: {e}")
        fallback_tts(text)

def fallback_tts(text):
    """Fallback TTS using pyttsx3"""
    print("Falling back to basic pyttsx3.")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def gen_compliment(image_path=None):
    
    """Generate response using Gemini API with optional image analysis"""
    
    system_prompt = f"""
        You are a friendly robot assistant talking to {child_profile['name']}, a {child_profile['age']}-year-old child.
        
        Child's Profile:
        - Interests: {', '.join(child_profile['interests'])}
        - Communication level: {child_profile['communication_level']}
        - Current goals: {', '.join(child_profile['current_goals'])}
        
        Guidelines for interaction:
        1. Use clear, simple language that a 7-year-old can understand
        2. Be supportive and positive
        3. Relate to the child's interests when possible
        4. Focus on emotions and their expression
        5. Keep messages very short (1-2 sentences maximum)
        6. Use simple vocabulary appropriate for their age
        7. Be playful and encouraging
        
        Only respond with the final message for the child. Do not include explanations or notes.
        """
        
    try:
        if image_path:
            # If image is available, use Gemini Vision API
            base64_image = encode_image_to_base64(image_path)
            
            # Create content parts including image
            parts = [
                {"text": system_prompt},
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": base64_image
                    }
                }
            ]
            
            # Send multimodal request
            response = model.generate_content(parts)
            return response.text
        else:
            # Text-only request
            response = model.generate_content(system_prompt)
            return response.text
            
    except Exception as e:
        print(f"Error getting response from Gemini: {e}")
        return "I'm having trouble right now. Can you try again?"

def display_expr(expr):
    pass

def main():
    print("Starting Autism-Friendly Robot Assistant...")
    image_path = capture_image()
    res=gen_compliment(image_path)
    display_expr('h')
    speak_text(res, 
               speaking_rate=child_profile['sensory_preferences']['preferred_voice_speed'],
               pitch=child_profile['sensory_preferences']['preferred_voice_pitch'])
    #print(f"Hello! {child_profile['name']}, {commplement}")
    
    # Initialize conversation history
    conversation_history = []
    
    # Initial greeting
    #c.main()
    greeting = f"So what do you wanna do? Play a game or build legos?"
    
    
    
    print("Robot: " + greeting)
    speak_text(greeting, 
               speaking_rate=child_profile['sensory_preferences']['preferred_voice_speed'],
               pitch=child_profile['sensory_preferences']['preferred_voice_pitch'])
    
    display_expr('n')
    
    user_input = listen_to_speech()
    conversation_history.append({"role": "assistant", "content": greeting})
    if user_input.lower() in ["legos","lego","ego","leego"]:
        track="lego"
    else:
        track="general"
    
    display_expr('e')
   
    # Main conversation loop
    while True:
        try:
            
            
            # Get speech input
            print("\nWaiting for speech input...")
            user_input = listen_to_speech()
            
            # Capture image first (will be used with each prompt)
            print("\nCapturing image...")
            image_path = capture_image()
            
            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
                farewell = f"Goodbye, {child_profile['name']}! I enjoyed talking with you today. See you next time!"
                print("Robot: " + farewell)
                speak_text(farewell, 
                          speaking_rate=child_profile['sensory_preferences']['preferred_voice_speed'],
                          pitch=child_profile['sensory_preferences']['preferred_voice_pitch'])
                break
                
            # Skip empty inputs
            if not user_input:
                continue
                
            # Add user input to conversation history
            conversation_history.append({"role": "user", "content": user_input})
            
            # Generate response with image analysis
            print("Generating response...")
            if track=="lego":
                 ai_response = generate_response_lego(user_input, conversation_history, image_path)
            else:
                ai_response = generate_response(user_input, conversation_history, image_path)
                
            expr=ai_response[-1]
            ai_response=ai_response[0:len(ai_response)-2]
            display_expr(expr)
            # Add AI response to conversation history
            conversation_history.append({"role": "assistant", "content": ai_response})
            
            # Output response
            print("Robot: " + ai_response)
            speak_text(ai_response, 
                      speaking_rate=child_profile['sensory_preferences']['preferred_voice_speed'],
                      pitch=child_profile['sensory_preferences']['preferred_voice_pitch'])
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            fallback_tts("I'm having a little trouble. Let's try again.")
            # Continue the loop despite errors

if __name__ == "__main__":
    main()
