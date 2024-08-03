import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY=st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel('gemini-1.5-pro')

def main():
    st.title("Professional LinkedIn Post Generator")

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.header("Input Data")
        
        # Input fields
        topic = st.text_input("Topic")
        key_points = st.text_area("Key Points (one per line)")
        tone = st.selectbox("Tone", ["Professional", "Friendly", "Enthusiastic", "Informative"])
        include_hashtags = st.checkbox("Include Hashtags")
        link = st.text_input("Add Link (optional)")

        # Generate button
        if st.button("Generate LinkedIn Post"):
            if topic and key_points:
                linkedin_post = generate_linkedin_post(topic, key_points, tone, include_hashtags, link)
                st.session_state.linkedin_post = linkedin_post
            else:
                st.error("Please provide a topic and key points.")

    with col2:
        st.header("LinkedIn Post Preview")
        if 'linkedin_post' in st.session_state:
            st.markdown(st.session_state.linkedin_post)

def generate_linkedin_post(topic, key_points, tone, include_hashtags, link):
    prompt = f"""
    Create a professional LinkedIn post about {topic}.
    Key points to include:
    {key_points}
    
    Tone: {tone}
    Include hashtags: {"Yes" if include_hashtags else "No"}
    Link to include: {link if link else "None"}
    
    The post should be engaging, concise, and formatted for LinkedIn.
    """

    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    main()