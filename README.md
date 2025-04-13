# 🤖 SNOM - AI Robot Buddy for Neurodiverse Children

## 🚀 About

**SNOM** is an emotionally intelligent, AI-powered robotic companion designed to support neurodiverse children—especially those with autism—in developing social skills, emotional understanding, and self-confidence.

Built to act as a best friend, SNOM follows children around, engages in adaptive conversations, and provides a safe, non-judgmental presence throughout their day.

Developed at **Bitcamp 2025**, SNOM blends cutting-edge tech with deep empathy to empower children and give parents peace of mind.

---

## 💡 Inspiration

The silent struggles of neurodiverse children navigating a world that often feels overwhelming—and the quiet heartbreak of parents who long to help—led us to create SNOM.

We envisioned a gentle buddy who always listens, never judges, and understands kids just the way they are.

SNOM is born from **empathy**, built with **intention**, and powered by the belief that **every child deserves a friend who truly sees them.**

---

## ⚙️ What It Does

SNOM is a smart, mobile, and empathetic robot that:

- 🤝 Autonomously follows children using real-time computer vision for companionship and safety.
- 📏 Maintains optimal conversation distance using dynamic calculations.
- 🧠 Uses **Gemini 2.0 Flash** to engage in natural, mood-aware conversations.
- 🎭 Visually displays emotions on a screen to encourage social understanding.
- 🔊 Speaks using lifelike voice feedback powered by text-to-speech tech.
- 🧭 Navigates independently to locate and follow users while avoiding obstacles.
- 🌱 Helps children identify, express, and manage emotions through conversation and interaction.

---

## 🔧 How We Built It

### 🧰 Hardware
- **Raspberry Pi 5** – Brain of SNOM, coordinating vision, movement, and speech.
- **Modified RC Car Chassis** – Provides smooth and flexible mobility.
- **Camera Module** – Enables person detection and tracking using OpenCV.
- **Bluetooth Speaker** – Provides natural voice feedback.
- **Display Screen** – Shows SNOM’s emotional expressions.
- **Power Bank (10,000mAh)** – Ensures extended runtime on the go.

### 💻 Software
- **Vision System** – Built with OpenCV for object tracking and real-time distance estimation.
- **Motor Control** – Uses `RPI.GPIO` for movement commands.
- **Conversation AI** – Integrated with **Gemini 2.0 Flash** for dynamic dialogue.
- **Speech Output** – Handled via `pyttsx3` for engaging voice interaction.
- **Emotion Display** – HTML/CSS/JS frontend served via Flask to display expressive emotions.

---

## 🤝 How TerpAI Helped Us

- Fine-tuned GenAI models to support emotional awareness in conversations.
- Built personalized child personas for meaningful, relatable interactions.
- Helped us understand real-world needs of parents and children with autism.
- Supported the development of an empathy-first solution.
- Enhanced our business plan and future scalability roadmap.

---

## 🧗‍♂️ Challenges We Faced

- 🔩 **Hardware Firsts** – Tackling hardware as CS students was a bold step!
- 🔧 **Reverse Engineering** – Modifying an RC car without compromising its internals.
- ⚡ **Power Optimization** – Managing multiple modules running concurrently.
- 🧠 **Real-Time Logic** – Ensuring smooth decision-making and movement.
- 🔈 **Audio Clarity** – Maintaining speech quality in different environments.

---

## ✅ Accomplishments

- 🛠️ Fully reverse-engineered and repurposed an RC car for autonomous tracking.
- 🤖 Integrated AI, speech, vision, and emotional expression into one cohesive system.
- 🧠 Developed mood-based conversations powered by **Gemini 2.0 Flash**.
- 💬 Built an engaging, empathetic tool that truly connects with children.
- 👪 Created a product that gives peace of mind to parents while fostering growth in kids.

---

## 📚 What We Learned

- How to merge software logic with real-world hardware mechanics.
- Practical experience with real-time vision processing under constraints.
- Human-robot interaction design and emotion-centered UX.
- Power management and optimization techniques.
- Most importantly: **empathy-first design transforms lives.**

---

## 🔮 What’s Next for SNOM

- 🌍 **Global Reach** – Make SNOM accessible to families worldwide.
- 🧠 **Advanced Personalization** – Adapt SNOM to unique personalities.
- 👩‍⚕️ **Therapeutic Integration** – Partner with educators and therapists.
- 📱 **Mobile App** – Let parents monitor and customize SNOM via a companion app.
- 🔋 **Better Battery Life** – Optimize SNOM’s energy usage.
- 🧠 **Smarter Conversations** – Continuously evolve emotional intelligence models.

---

## 🛠️ Getting Started

### 📦 Prerequisites
- Raspberry Pi 5 (with Raspberry Pi OS)
- Python 3.9+
- OpenCV 4.5+
- Chromium browser (for emotion display)
- RC car chassis (modified)
- Compatible Pi camera module
- Bluetooth speaker
- Display screen (7"+ recommended)
- Power bank (10,000mAh or higher)

