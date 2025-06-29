import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
import re

# Set the app title
st.title("YouTube Transcript Extractor")

# Input for YouTube URL
youtube_url = st.text_input("Enter YouTube Video URL:")

def get_youtube_id(url):
    """Extracts the video ID from a YouTube URL."""
    # Standard YouTube URL
    match = re.search(r'(?:v=|youtu\.be/)([^&]+)', url)
    if match:
        return match.group(1)
    # YouTube Shorts URL
    match = re.search(r'shorts/([^?]+)', url)
    if match:
        return match.group(1)
    return None

if youtube_url:
    video_id = get_youtube_id(youtube_url)

    if video_id:
        try:
            # Get available transcript languages
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            available_languages = {
                t.language_code: t for t in transcript_list # 언어 코드를 키로 사용하도록 수정
            }

            if available_languages:
                st.subheader("Available Subtitle Languages:")

                # Display available languages to the user
                for lang_code, transcript_info in available_languages.items():
                    # 자동 생성(generated) 여부와 번역 가능(translatable) 여부를 함께 표시
                    status = []
                    if transcript_info.is_generated:
                        status.append("Auto-generated")
                    if transcript_info.is_translatable:
                        status.append("Translatable")

                    status_text = f" ({', '.join(status)})" if status else ""
                    st.write(f"- {transcript_info.language} ({transcript_info.language_code}){status_text}")

                # Allow user to select a language by its code
                # sorted(available_languages.keys())를 사용하여 목록을 정렬
                selected_lang_code = st.selectbox(
                    "Select the subtitle language to download (code):", 
                    sorted(list(available_languages.keys())) 
                )

                if selected_lang_code:
                    st.info(f"Fetching '{available_languages[selected_lang_code].language}' subtitles...")

                    try:
                        # Get transcript for the selected language
                        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[selected_lang_code])

                        # Remove time information and combine text
                        cleaned_text_lines = [item['text'] for item in transcript]
                        cleaned_text = "\n".join(cleaned_text_lines)

                        st.subheader(f"'{available_languages[selected_lang_code].language}' Subtitles (No Time Information):")
                        st.code(cleaned_text)

                    except NoTranscriptFound: 
                        # 선택한 언어의 자막이 없거나, list_transcripts에서는 있었지만 get_transcript에서 찾을 수 없을 때
                        st.error(f"The selected language '{available_languages[selected_lang_code].language}' subtitles could not be retrieved. This might occur if the language is not actually available or due to a temporary issue.")
                    except Exception as e:
                        st.error(f"An unexpected error occurred while fetching the selected language subtitles: {e}")

            else:
                st.warning("No subtitles are available for this video. This might be because the uploader did not provide them, or they are disabled.")

        except NoTranscriptFound:
            # 이 예외는 list_transcripts에서도 발생할 수 있으므로, 더 구체적인 메시지 제공
            st.warning("No subtitles were found at all for this video. This could mean they are genuinely unavailable, or the video owner has disabled them.")
        except TranscriptsDisabled:
            st.warning("Subtitles are explicitly disabled for this video by the uploader.")
        except Exception as e:
            st.error(f"An error occurred while trying to access subtitle information for this video: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")
