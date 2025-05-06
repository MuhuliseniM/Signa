# Signa – South African Sign Language Assistant

**Signa** is an AI-powered assistant that helps bridge communication gaps between hearing individuals and the Deaf community using live speech recognition and visual sign language playback.

The app listens to spoken phrases, converts them to text using **Azure Speech-to-Text**, matches them against a predefined phrase map, and plays an animated **sign language avatar video** to interpret the message visually.

---

## Project Goals

- Provide Deaf users with real-time access to spoken communication
- Promote inclusivity in classrooms, clinics, and public spaces
- Lay the foundation for two-way interaction: voice-to-sign and sign-to-voice

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (basic)
- **Backend**: Python (Flask)
- **AI Service**: Azure Cognitive Services (Speech-to-Text API)
- **Animation**: DeepMotion (for sign language avatar generation)
- **Environment Handling**: python-dotenv

---

## Note on Avatars

The current avatar videos are **placeholders** created using DeepMotion from self-recorded signing clips. In the full version, we plan to connect Signa to a **verified South African Sign Language (SASL) video bank** or 3D avatar system to ensure accuracy and inclusivity.

---
