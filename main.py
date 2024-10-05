# AIzaSyBOaP-EgweOFeftWqjR7AFnu3qVojCHjac


import streamlit as st
import requests
import random

# YouTube Data API key
API_KEY = "AIzaSyBOaP-EgweOFeftWqjR7AFnu3qVojCHjac"

 
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

# Predefined list of educational topics
EDUCATIONAL_TOPICS = [
    "web development", "machine learning", "data science", "programming", 
    "python", "artificial intelligence", "software engineering", 
    "cloud computing", "cybersecurity", "blockchain", "algorithms"
]

# List of motivational quotes
MOTIVATIONAL_QUOTES = [
    "Believe in yourself and all that you are.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Start where you are. Use what you have. Do what you can."
]

# Function to get top YouTube videos for a query excluding short videos
def get_top_youtube_videos(query, max_results=10):
    params = {
        'part': 'snippet',
        'q': query,
        'key': API_KEY,
        'type': 'video',
        'maxResults': max_results,
        'order': 'relevance',  # Order by relevance
        'videoDuration': 'medium'  # Exclude short videos, allow medium and long videos
    }
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    results = response.json()

    videos = []
    if "items" in results:
        for video in results['items']:
            video_title = video['snippet']['title']
            video_id = video['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_thumbnail = video['snippet']['thumbnails']['high']['url']
            video_description = video['snippet']['description']
            publish_time = video['snippet']['publishedAt']
            videos.append((video_title, video_url, video_thumbnail, video_description, publish_time))
    return videos

# Function to check if the query is educational
def is_educational_topic(query):
    query = query.lower()
    for topic in EDUCATIONAL_TOPICS:
        if topic in query:
            return True
    return False

# Streamlit app title
st.title("Learning Resource Finder")

# Description
st.write("Ask any educational topic you're interested in, and I'll find the best YouTube videos to help you learn!")

# User input for the topic with auto-search feature
topic = st.text_input("What would you like to learn about? (e.g., Web Development, Machine Learning)")

# If the user types a query (auto-search effect)
if topic:
    # Check if the topic is educational
    if is_educational_topic(topic):
        st.write(f"Searching for the top videos on: {topic}")
        
        # Get the top videos for the topic excluding short videos
        videos = get_top_youtube_videos(topic)
        
        if videos:
            st.write(f"Here are the top YouTube videos for learning about {topic}:")
            # Display videos in a YouTube-like layout
            for video_title, video_url, video_thumbnail, video_description, publish_time in videos:
                st.markdown("---")
                col1, col2 = st.columns([1, 4])

                # Display video thumbnail in the first column
                with col1:
                    st.image(video_thumbnail, use_column_width=True)

                # Display video title, link, and description in the second column
                with col2:
                    st.markdown(f"### [{video_title}]({video_url})")
                    st.markdown(f"*Published on: {publish_time[:10]}*")
                    st.write(video_description)

        else:
            st.write("Sorry, I couldn't find any videos on that topic. Please try a different one.")
    else:
        # Show a motivational quote if the query is not educational
        st.write("This doesn't seem like an educational topic. Here's a motivational quote for you:")
        st.write(f"**{random.choice(MOTIVATIONAL_QUOTES)}**")

# Footer with copyright notice
st.markdown("---")
st.write("© 2024 Rajan Kumar. All rights reserved.")
