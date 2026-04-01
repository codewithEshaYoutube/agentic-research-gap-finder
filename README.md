# 🧠 Research Agentic AI

> An autonomous AI system that reads academic papers, uncovers research gaps, suggests future directions, and answers custom queries — all in one pipeline.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://agenticresearchgap.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

## 📌 Overview

**Research Agentic AI** is an intelligent research assistant powered by large language models. Upload any academic paper (PDF), and the system autonomously summarizes it, identifies limitations, proposes future research directions, generates novel research questions, and responds to your custom queries — mimicking the reasoning process of a senior researcher.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 PDF Upload | Upload any academic paper in PDF format |
| 📝 Auto Summarization | Concise, structured summaries of complex papers |
| 🔍 Gap Identification | Automatically identifies limitations and research gaps |
| 🔭 Future Directions | Suggests meaningful next steps for the field |
| ❓ Research Questions | Generates novel, targeted research questions |
| 💬 Custom Queries | Answer any question you have about the paper |
| 🤖 Agentic Loop | Human-like multi-step reasoning pipeline |

---

## 🖥️ Live Demo

Try it instantly — no setup required:

🔗 **[agenticresearchgap.streamlit.app](https://agenticresearchgap.streamlit.app/)**

---

## 🛠️ Installation

### Prerequisites

- Python 3.9+
- An [Anthropic API key](https://console.anthropic.com/)

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ResearchAgenticAI.git
cd ResearchAgenticAI
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

5. **Run the app**

```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

---

## 📂 Project Structure

```
ResearchAgenticAI/
├── app.py                  # Streamlit frontend
├── agents/
│   ├── summarizer.py       # Paper summarization agent
│   ├── gap_finder.py       # Research gap identification agent
│   ├── question_gen.py     # Research question generator
│   └── query_agent.py      # Custom query handler
├── utils/
│   ├── pdf_parser.py       # PDF text extraction
│   └── prompt_templates.py # LLM prompt templates
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔄 How It Works

```
📄 Upload PDF
     │
     ▼
🔎 Extract & Parse Text
     │
     ▼
🧠 Agentic Reasoning Loop
     ├──► Summarize Paper
     ├──► Identify Gaps & Limitations
     ├──► Suggest Future Directions
     ├──► Generate Research Questions
     └──► Answer Custom Queries
     │
     ▼
📊 Display Results in Streamlit UI
```

The system uses a **multi-agent pipeline** where each agent specializes in a specific task, coordinated by a central reasoning loop that passes context between steps.

---

## 🧪 Example Usage

1. Open the app and upload a research paper (PDF)
2. Wait for the automatic analysis to complete
3. Browse through:
   - **Summary** — key contributions and methodology
   - **Research Gaps** — what the paper leaves unanswered
   - **Future Directions** — suggested next steps
   - **Research Questions** — novel questions for follow-up work
4. Type your own question in the **Custom Query** box for a targeted answer

---

## 📦 Dependencies

```
streamlit
anthropic
PyMuPDF
python-dotenv
langchain
```

> Full list in [`requirements.txt`](requirements.txt)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Acknowledgements

- [Anthropic](https://anthropic.com) for Claude API
- [Streamlit](https://streamlit.io) for the web framework
- The open-source research community

---

<p align="center">Built with ❤️ to accelerate scientific discovery</p>
