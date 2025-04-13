# Your Friend STEVE

## 🚀 About
CompanionBot is an AI-powered robotic companion built on a modified RC car platform that assists children with difficulties through engaging conversations and autonomous interaction.

_Developed for Bitcamp 2025_

![CompanionBot Prototype](image_link_here)

## 💡 Inspiration
Children with difficulties often benefit from consistent, patient interaction and engagement. Our team recognized that AI companionship could provide additional support to these children by offering a friendly, non-judgmental presence that can follow, interact, and communicate with them. We wanted to create an accessible, mobile companion that could autonomously engage with children while maintaining appropriate interaction distance.

## ⚙️ What it does
CompanionBot is an interactive robotic companion that:
- Autonomously follows children using computer vision
- Maintains optimal conversation distance through real-time calculations
- Engages in natural conversations powered by Gemini 2.0 Flash
- Displays emotions on a screen to enhance social connection
- Responds with voice feedback using text-to-speech technology
- Navigates independently to find and approach users

## 🔧 How we built it
- **Hardware**: Raspberry Pi 5, modified RC car chassis, camera module, Bluetooth speaker, display screen
- **Vision System**: OpenCV for person detection, distance calculation, and tracking
- **Control System**: RPI.GPIO for interfacing with the RC car's motor controls
- **Conversation AI**: Gemini 2.0 Flash for natural language processing and conversation
- **Speech**: PyTTS for text-to-speech conversion
- **Emotion Display**: HTML/CSS/JavaScript frontend connected to a Flask server
- **Integration**: Python scripts for coordinating all components and systems

## 🏆 Challenges we ran into
- **Reverse engineering the RC car**: We had to carefully disassemble and analyze the existing control systems to integrate our own controls without damaging functionality
- **Power management**: Running a Raspberry Pi, display, camera, and motors simultaneously required careful power distribution and optimization
- **Autonomous navigation**: Developing algorithms that could reliably follow users while avoiding obstacles proved challenging
- **Latency reduction**: Minimizing delay between vision processing, decision making, and motor control required significant optimization
- **Audio clarity**: Ensuring the robot's speech remained audible in different environments required testing various speaker placements

## ✅ Accomplishments that we're proud of
- Successfully reverse-engineered and repurposed a commercial RC car for AI-powered autonomy
- Created a fully integrated system that combines vision, speech, movement, and emotional display
- Developed efficient distance-maintaining algorithms that keep the robot at the perfect conversation distance
- Built a modular design that allows for easy component replacement and upgrades
- Achieved natural-feeling conversational interactions using Gemini 2.0 Flash

## 📚 What we learned
- Hardware integration techniques between consumer electronics and custom robotics
- Real-time computer vision processing on resource-constrained devices
- Effective strategies for human-robot interaction design
- Power and performance optimization for mobile robotic platforms
- Interdisciplinary collaboration across hardware, software, and design disciplines

## 🔮 What's next
- Adding obstacle avoidance capabilities using additional sensors
- Implementing activity recognition to better understand user context
- Creating a companion mobile app for caregiver monitoring and control
- Expanding the emotional display capabilities with more nuanced expressions
- Developing specialized conversation modules for different therapeutic contexts
- Improving battery life with more efficient power management

## 🛠️ Getting Started

### Prerequisites
```
- Raspberry Pi 5 with Raspberry Pi OS installed
- Python 3.9+
- OpenCV 4.5+
- Web browser for emotion display (Chromium recommended)
- Modified RC car chassis with accessible control pins
- Raspberry Pi compatible camera module
- Bluetooth speaker
- Display screen (7" minimum recommended)
- Power bank with at least 10,000mAh capacity
```

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/companionbot.git

# Navigate to the project directory
cd companionbot

# Install dependencies
pip install -r requirements.txt

# Configure your Gemini API key
export GEMINI_API_KEY=your_api_key_here

# Start the emotion display server
python emotion_server.py &

# Run the main robot control program
python companionbot.py
```

## 📝 Usage

### Basic Operation
1. Power on the CompanionBot using the main switch on the chassis
2. Wait approximately 30 seconds for all systems to initialize
3. The emotion display will show a "Ready" face when the system is operational
4. Place the bot near the intended user
5. The bot will automatically detect the person and approach them
6. Once at conversation distance, the bot will introduce itself and begin interaction
7. The user can speak naturally to the bot, which will respond via its speaker

### Control Options
```bash
# To temporarily pause autonomous movement while keeping conversation active
python companionbot.py --stationary

# To run in quiet mode (text-only conversations on display)
python companionbot.py --quiet

# To run with debugging information displayed
python companionbot.py --debug
```

## 🔗 Links
- [GitHub Repository](your-repo-link)
- [Demo Video](your-video-link)
- [Project Website](your-website-link)

## 📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## 🙏 Acknowledgments
- Google for providing access to the Gemini 2.0 Flash API
- OpenCV community for computer vision libraries and resources
- Raspberry Pi Foundation for creating accessible computing platforms
- Bitcamp organizers and sponsors for the opportunity to develop this project
- All the children and families who provided feedback during our testing phase
