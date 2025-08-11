# Agentic Systems Practice

This repository contains a curated collection of **Jupyter notebooks and Python scripts** created while learning to build **agentic systems** using [LangChain](https://www.langchain.dev/) and [LangGraph](https://www.langchain.com/langgraph).  
The goal is to explore and implement **core components of LLM-based agents** such as:

- **Memory** 
- **Retrieval-Augmented Generation (RAG)**
- **Tool usage** (prebuilt & custom)
- **Agent orchestration** with the new LangChain Expression Language (**LCEL**)
- **LangGraph**-powered workflows for more control and state management

---

## 📂 Repository Contents

### 1. **Agentic Systems with LangChain**

| Script | Description |
|--------|-------------|
| `script1_aa_ai_assistant.ipynb` | A simple AI assistant built with LangChain, demonstrated **with and without memory integration**. |
| `script2_aa_rag_lcel.ipynb` | Implements **Retrieval-Augmented Generation (RAG)** using LCEL for building modular chains. |
| `script3_aa_tools_agent_tool_calling.ipynb` | Introduces **tool usage** in LangChain v0.1, including **prebuilt** and **custom tools**, and building a **tool-calling agent**. |
| `script4_aa_tools_react.ipynb` | Demonstrates the **ReAct** (Reasoning + Acting) framework with prebuilt and custom tools in LangChain v0.1. |
| `script5_aa_tools_agent_self_ask_with_search.ipynb` | Implements the **Self-Ask-With-Search** agent pattern for step-by-step reasoning with a search tool. |

---

### 2. **Agentic Systems From Scratch (Pure Python)**

| Script | Description |
|--------|-------------|
| `script6_aa_agent_react_from_scratch.ipynb` | Implements the **ReAct** agent **from scratch** to deeply understand each functionality. |

---

### 3. **Agentic Systems with LangGraph**

| Script | Description |
|--------|-------------|
| `script7_aa_agent_langgraph_introduction.ipynb` | **Introduction to LangGraph** with key concepts and terminology. |
| `script8_aa_agent_langgraph_agent_with_RAG.ipynb` | Building a **ReAct agent with RAG** using LangGraph. |
| `script9_aa_agent_langgraph_checkpoint_memory.ipynb` | Demonstrates how to define **memory checkpoints** for LangGraph agents. |

---

### 4. **`chatbot_with_langgraph/` — Complete Web-Based Chatbot Agent**

| Script | Description |
|--------|-------------|
| `aa_app.py` | **Streamlit-based** chatbot interface for interacting with the LangGraph agent. |
| `aa_bot.py` | Core chatbot logic — routes input through: `input → agent → tool → end` or `input → agent → tool → agent`. |

---

## 📝 Notes
- More scripts coming soon.
- All scripts are **annotated** and **self-contained** for ease of understanding and modification.
- Suitable for:
  - Beginners exploring **LLM-based agent design**
  - Developers experimenting with **LangChain** and **LangGraph**
  - Researchers prototyping **tool-using AI agents**
- Inspired by tutorials from the [LangGraph Agents YouTube Playlist](https://youtube.com/playlist?list=PLQxDHpeGU14AJ4sBRWLBqjMthxrLXJmgF&si=1n2zc-q1Y0H9ZULJ).

---

