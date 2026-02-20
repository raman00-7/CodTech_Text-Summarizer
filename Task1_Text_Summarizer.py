import streamlit as st
from transformers import pipeline

# Cache and load the summarization model
@st.cache_resource(show_spinner=True)
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

st.title("📝 Text Summarization Tool")
st.write("This tool summarizes long paragraphs using a pre-trained NLP model.")

# Default paragraph
default_text = (
    "Artificial Intelligence (AI) is revolutionizing the modern world by introducing automation into processes "
    "that were previously handled manually. From healthcare and education to transportation and finance, AI is "
    "enabling more accurate predictions, smarter decision-making, and improved efficiencies. In particular, "
    "Natural Language Processing (NLP), a subfield of AI, is allowing machines to understand and generate human "
    "language. Applications like text summarization, sentiment analysis, and machine translation are becoming "
    "increasingly common in both consumer and enterprise products. As AI continues to evolve, it is crucial to "
    "ensure its development is guided by ethical principles to maximize benefits and minimize risks to society."
)

# Text area with default text
article = st.text_area("Enter your text here:", value=default_text, height=250)

# Display initial summary for default text
if article == default_text:
    with st.spinner("Generating summary..."):
        summary = summarizer(default_text, max_length=70, min_length=30, do_sample=False)
    st.subheader("🔹 Summary")
    st.write(summary[0]['summary_text'])

# Summarize on button click
if st.button("Summarize"):
    if article.strip():
        with st.spinner("Generating summary..."):
            summary = summarizer(article, max_length=70, min_length=30, do_sample=False)
        st.subheader("🔹 Summary")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to Summarize.")
