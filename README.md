# YouTube Transcript Extractor Streamlit App

![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🚀 Project Overview

This is a simple Streamlit web application that allows users to extract transcripts from YouTube videos. Just provide a YouTube video URL, select your desired language, and get the clean text transcript without timestamps.

## ✨ Features

*   **Extracts transcripts** from YouTube videos.
*   **Supports multiple languages**, including auto-generated captions.
*   **Removes timestamps** for a clean text output.
*   **User-friendly interface** built with Streamlit.

## 🛠️ Tech Stack

*   **Python**
*   **Streamlit**
*   **youtube-transcript-api**

## ⚙️ Local Setup

To run this application locally:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    `requirements.txt` contains:
    ```
    streamlit
    youtube-transcript-api
    ```

4.  **Run the Streamlit app**:
    ```bash
    streamlit run youtube_transcript_app.py
    ```

## 🚀 Deployment (e.g., Streamlit Cloud)

This app can be easily deployed to platforms like Streamlit Cloud. Ensure all necessary files (`youtube_transcript_app.py`, `requirements.txt`) are pushed to your GitHub repository.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---