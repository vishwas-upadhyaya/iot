# IoT Audio/Visual Processing App

## Project Overview
This project is a Django-based web application focused on processing audio and visual inputs. It provides functionalities such as extracting text from images (OCR), summarizing or generating text based on extracted content, and converting the resulting text back to speech. It integrates cloud services for storage and advanced ML APIs for natural language processing.

## Deep Technical Details (Architecture, Pipeline)
- **Architecture:** 
  - A Django web framework backend managing the application flow, routing, and database models.
  - Django Views handle image uploads and trigger the ML pipeline.
- **Data Pipeline & Processing:** 
  - **OCR (Optical Character Recognition):** Uses `easyocr` to extract text from user-uploaded images.
  - **Natural Language Processing:** Integrates with the `cohere` API to process and summarize the extracted text.
  - **Text-to-Speech (TTS):** The processed text is converted into audio using Google Text-to-Speech (`gTTS`).
  - **Cloud Integration:** Uses `boto3` for handling file storage on AWS S3, facilitating the storage and retrieval of audio files.
  - **Speech-to-Text:** Whisper (OpenAI) support is included for transcribing audio to text.

## Tech Stack
- **Framework:** Django
- **Machine Learning & APIs:** 
  - `easyocr` (for image-to-text)
  - `cohere` (for text generation and summarization)
  - `gTTS` (Google Text-to-Speech)
  - `openai-whisper` (for speech-to-text)
- **Cloud & Utilities:**
  - `boto3` (AWS SDK for Python)
  - `environ` (for environment variable management)
  - PyTorch / Transformers (underlying ML framework dependencies)
