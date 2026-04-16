# 🤖 AI-Genius: CLI-Based Educational Engine

AI-Genius is a robust, terminal-driven assessment tool designed to test and track knowledge of Artificial Intelligence fundamentals. This project demonstrates the practical application of nested data structures and real-time user input processing.

## 🎯 Project Purpose
The goal of this project is to move beyond simple "Hello World" scripts and implement a **Data-Driven Logic Flow**. By separating the quiz content (the data) from the engine (the code), the application becomes highly scalable and easy to maintain.

## 🏗️ Technical Architecture

### 1. Nested Dictionary Structure (The "Knowledge Base")
The application uses a **Key-Value-Object** mapping strategy. Each unique question ID maps to a sub-dictionary containing:
* `question`: The core prompt (String).
* `options`: A list of potential answers (List).
* `answer`: The validation key (Character).

### 2. Normalization Pipeline
To ensure a frictionless user experience, the engine performs **Input Normalization**:
* `strip()`: Removes accidental whitespace.
* `upper()`: Standardizes the input to match the dictionary keys, preventing case-sensitive failures.

### 3. State Management
Using Chapter 2 variables, the engine maintains the application "state" (the score) as it iterates through the data list, calculating a final accuracy percentage using floating-point arithmetic.

## 🛠️ Industry Applications
This "Quiz Engine" logic is the foundation for:
* **Skill Assessment Bots:** Used in platforms like LinkedIn or HackerRank for initial candidate filtering.
* **Compliance Training:** Automated internal corporate training for legal or security protocols.
* **Interactive Chatbots:** The logic for branching conversations starts with this type of mapped dictionary logic.

## 🚀 Deployment
1. Ensure Python 3.x is installed.
2. Clone this repository.
3. Execute via terminal:
   ```bash
   python ai_quiz.py
