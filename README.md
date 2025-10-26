<div align="center">

# 📚 DevNotes-AI

### *Transform Your Code Into Study Notes with AI*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Core-green.svg)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**DevNotes-AI** is an intelligent tool that automatically converts your code files into comprehensive, beautifully formatted study notes using cutting-edge AI technology.

</div>

---

## 🌟 Features

### ✨ **AI-Powered Documentation**
Generate detailed, educational notes from any code file in seconds. Our AI analyzes your code and creates comprehensive explanations that read like a textbook.

### 🎯 **Multi-Provider Support**
Choose from **three powerful AI providers**:
- **Google Gemini** - Fast and efficient
- **OpenAI GPT** - Advanced reasoning
- **Anthropic Claude** - Context-aware explanations

### 🎨 **Beautiful Web Interface**
- Upload multiple files at once
- Real-time progress tracking
- Edit generated notes before finalizing
- Live preview of your documentation

### 📝 **Smart Formatting**
- Automatically detects code concepts
- Creates logical topic hierarchies
- Generates markdown with proper structure
- Clean, readable output

### 🔄 **Flexible Workflow**
- **Web App**: Streamlit-based GUI for interactive processing
- **CLI Tool**: Command-line interface for automation
- Batch processing multiple files
- Custom section topics and AI suggestions

---

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/DevNotes-AI.git
cd DevNotes-AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Get an API key from one of the providers:
- [Google AI Studio](https://makersuite.google.com/app/apikey) (Gemini)
- [OpenAI Platform](https://platform.openai.com/api-keys)
- [Anthropic](https://console.anthropic.com/) (Claude)

---

## 💻 Usage

### Web Interface

Start the Streamlit app:

```bash
streamlit run app.py
```

Then:
1. Open your browser to `http://localhost:8501`
2. Select your AI provider and enter your API key
3. Upload your code files
4. Configure section topics (optional)
5. Click "Start Processing"
6. Review and edit generated notes
7. Download your markdown documentation

### Command Line Interface

Run the CLI version:

```bash
python main.py
```

Follow the interactive prompts to:
- Enter your main notes title
- Provide file paths (one per line)
- Get generated markdown and PDF outputs

---

## 📖 Example

**Input Code:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

**Generated Output:**

## Fibonacci Sequence

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.

### Recursive Implementation

**Concept**: The function calls itself with smaller values until reaching the base case.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Key Points**:
• Base case: `n <= 1` returns `n` (prevents infinite recursion)
• Recursive case: Returns sum of previous two Fibonacci numbers
• Time complexity: O(2^n) - not efficient for large n

### Usage

```python
print(fibonacci(10))  # Output: 55
```

🔹 **Takeaway**: Recursive solutions are elegant but can be slow for large inputs.

---

## 🎯 Supported File Types

- **Python** (`.py`)
- **JavaScript** (`.js`)
- **Jupyter Notebooks** (`.ipynb`)
- **Java** (`.java`)
- **C++** (`.cpp`)
- **C** (`.c`)
- **Plain Text** (`.txt`)

---

## 🛠️ Tech Stack

- **LangChain**: Orchestrates AI model interactions
- **Streamlit**: Beautiful, interactive web interface
- **Markdown2**: Rich text formatting
- **AI Models**: Gemini, GPT, Claude

---

## 📋 Requirements

```
langchain-google-genai
langchain-openai
langchain-anthropic
langchain
markdown2
streamlit
pdfkit
```

---

## 💡 Use Cases

- 📚 **Study Preparation**: Convert your practice code into review notes
- 📖 **Documentation**: Automatically document your codebase
- 🎓 **Teaching Materials**: Generate educational content from code examples
- 🔄 **Code Review**: Get AI-generated explanations of unfamiliar code
- 📝 **Personal Wiki**: Build a knowledge base from your projects

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📺 Demo Video

Watch the full walkthrough and see DevNotes-AI in action:

**[🎬 Watch Demo Video](https://your-demo-video-link.com)**

---

<div align="center">

**Made with ❤️ by Saish**

⭐ Star this repo if you find it useful!

</div>