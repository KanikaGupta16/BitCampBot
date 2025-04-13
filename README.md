
SNOM - AI Robot Buddy for Neurodiverse Children
🚀 About
SNOM is an emotionally intelligent AI-powered robotic companion designed to support neurodiverse children, such as those with autism, in developing social skills, emotional understanding, and confidence. Built to act as a best friend, SNOM follows children around, engages in adaptive conversations, and provides a safe, non-judgmental presence.

Developed for Bitcamp 2025, SNOM combines cutting-edge technology with empathy to empower children and provide peace of mind to parents.

💡 Inspiration
The silent struggles of neurodiverse children — navigating a world that feels confusing and isolating — and the unspoken pain of parents unable to help inspired us to act. We wanted to create a tool that transforms these challenges into moments of growth, connection, and empowerment.

SNOM is born from empathy and the belief that every child deserves a friend who truly understands them.

⚙️ What it does
SNOM is an interactive robotic companion that:

Autonomously follows children using computer vision, ensuring companionship and safety.
Maintains optimal conversation distance through real-time calculations.
Engages in natural conversations powered by Gemini 2.0 Flash, tailored to the child’s mood and personality.
Displays emotions visually on a screen to enhance social connection.
Responds with voice feedback using text-to-speech technology to encourage interaction.
Navigates independently to find and approach users while avoiding obstacles.
Supports emotional growth by helping children understand and express their feelings.
🔧 How We Built It
Hardware
Raspberry Pi 5: Acts as the brain of SNOM, coordinating all hardware and software components.
Modified RC car chassis: Provides mobility and smooth navigation.
Camera module: Enables vision processing for person detection and tracking.
Bluetooth speaker: Delivers clear, friendly voice responses.
Display screen: Shows emotions visually to enhance communication.
Software
Vision System: OpenCV for person detection, distance calculation, and tracking.
Control System: RPI.GPIO for interfacing with the RC car’s motor controls.
Conversation AI: Gemini 2.0 Flash for natural language processing and adaptive conversations.
Speech: PyTTS for text-to-speech conversion, ensuring SNOM’s voice feels relatable.
Emotion Display: HTML/CSS/JavaScript frontend connected to a Flask server for displaying emotions.
Integration: Python scripts for seamless coordination of all systems.
How TerpAI Helped Us
Fine-tuned AI models for emotional intelligence.
Built personalized personas for children based on their interests and sensitivities.
Identified key challenges faced by neurodiverse children and parents to guide solution development.
Supported the creation of an empathetic, impactful design.
Assisted in developing a strong business plan for future scalability.
🏆 Challenges We Ran Into
First-Time Hardware Hack: Building a hardware-based project as computer science majors was a steep learning curve.
Reverse Engineering: Disassembling and analyzing an RC car to integrate our own controls without damaging functionality.
Power Management: Optimizing power distribution for multiple components running simultaneously.
Autonomous Navigation: Developing reliable algorithms for user tracking and obstacle avoidance.
Latency Reduction: Minimizing delays between vision processing, decision-making, and motor control.
Audio Clarity: Ensuring SNOM’s speech remained clear and audible across various environments.
✅ Accomplishments That We’re Proud Of
Successfully reverse-engineered and repurposed a commercial RC car for AI-powered autonomy.
Created a fully integrated system combining vision, speech, movement, and emotional display.
Developed efficient distance-maintaining algorithms for optimal conversation interaction.
Achieved natural-feeling conversational interactions using Gemini 2.0 Flash.
Built a tool that genuinely connects with neurodiverse children, fostering confidence and emotional growth.
📚 What We Learned
Mastered hardware-software integration techniques.
Improved skills in real-time computer vision processing on resource-constrained devices.
Developed effective strategies for human-robot interaction design.
Optimized power and performance for mobile robotic platforms.
Learned the importance of empathy-driven design for impactful solutions.
🔮 What’s Next for SNOM
Global Reach: Scaling SNOM to make him accessible to families worldwide.
Advanced Personalization: Refining SNOM’s ability to adapt to unique personalities and interests.
Therapeutic Integration: Collaborating with educators and therapists to revolutionize support for neurodiverse children.
Activity Recognition: Implementing sensors to better understand user context and actions.
Companion Mobile App: Creating an app for caregiver monitoring and control.
Improved Battery Life: Optimizing power management for extended usage.
Continuous Evolution: Leveraging feedback to refine emotional intelligence and conversational capabilities.
🛠️ Getting Started
Prerequisites
Raspberry Pi 5 with Raspberry Pi OS installed
Python 3.9+
OpenCV 4.5+
Web browser for emotion display (Chromium recommended)
Modified RC car chassis with accessible control pins
Raspberry Pi compatible camera module
Bluetooth speaker
Display screen (7" minimum recommended)
Power bank with at least 10,000mAh capacity
Installation
bash
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
Usage
Basic Operation:

Power on SNOM using the main switch on the chassis.
Wait approximately 30 seconds for all systems to initialize.
The emotion display will show a "Ready" face when operational.
Place SNOM near the intended user, and he will autonomously detect and approach them.
Engage in natural conversations with SNOM, who will respond via his speaker.
Control Options:

To temporarily pause autonomous movement while keeping conversation active:
bash
python companionbot.py --stationary
To run in quiet mode (text-only conversations on display):
bash
python companionbot.py --quiet
To run with debugging information displayed:
bash
python companionbot.py --debug
🔗 Links
GitHub Repository
Demo Video
Project Website
📜 License
This project is licensed under the MIT License - see the LICENSE.md file for details.

🙏 Acknowledgments
Google: For providing access to the Gemini 2.0 Flash API.
OpenCV Community: For computer vision libraries and resources.
Raspberry Pi Foundation: For creating accessible computing platforms.
Bitcamp Organizers and Sponsors: For the opportunity to develop this project.
Families and Children: Who provided valuable feedback during testing phases.
Does this comprehensive README file meet your expectations? Let me know if there are any additional adjustments or sections you'd like to include!

