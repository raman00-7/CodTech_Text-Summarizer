# 📝 Task 1 – Text Summarization Tool (CodTech Internship)

This project is part of my CodTech Artificial Intelligence Internship.  
It focuses on summarizing lengthy articles using Natural Language Processing (NLP) techniques with a simple web interface.

## 🔧 Objective
To create a Python tool that takes a long paragraph or article and returns a concise, meaningful summary using a pre-trained NLP model.

## 💡 Features

- Pre-loaded paragraph with auto-generated summary
- Text area for user-defined input
- "Summarize" button to generate new summaries
- Spinner animation during processing
- Lightweight model for fast results

## 🚀 Technologies Used

| Tool / Library              | Purpose                           |
|----------------------------|---------------------------------|
| `Streamlit`                 | Web interface                   |
| `Hugging Face Transformers`| Pre-trained summarization models|
| `Python`                   | Core scripting                  |

## 📁 File Structure

```
Task1_Text_Summarizer/
├── Task1_Text_Summarizer.py   # Streamlit app
└── README.md                  # Project documentation
```

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/raman00-7/Text-Summarizer.git
cd Text-Summarizer/Task1_Text_Summarizer
```

2. **Create virtual environment (optional but recommended)**
```bash
python -m venv .venv
source .venv/bin/activate  # For macOS/Linux
```

3. **Install dependencies**
```bash
pip install streamlit transformers
```
## ▶️ Run the App

```bash
streamlit run Task1_Text_Summarizer.py
```
## 🧪 Example

### Input:
> Artificial Intelligence (AI) is revolutionizing the modern world...

### Output Summary:
> AI is transforming industries with automation. NLP helps machines understand human language...

## 📚 Resources

- [Hugging Face Model: distilbart-cnn](https://huggingface.co/sshleifer/distilbart-cnn-12-6)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Transformers Library](https://huggingface.co/docs/transformers)

## 📌 Internship Info
- 🔖 Domain: Artificial Intelligence
- 🏢 Company: CodTech
- 📁 Task: Text Summarization using NLP
- 🗓️ Submitted by: *Raman Kumar*
