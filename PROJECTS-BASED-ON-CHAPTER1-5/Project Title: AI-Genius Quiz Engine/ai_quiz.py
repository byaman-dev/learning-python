'''
PROJECT: AI-Genius CLI Quiz Engine
TOPIC: Artificial Intelligence Fundamentals
CONCEPTS: Nested Dictionaries (Ch 5), Lists (Ch 4), String Formatting (Ch 3), 
          and Typecasting (Ch 2).
'''

import os

# --- CHAPTER 5: NESTED DICTIONARY (The Knowledge Base) ---
# We store the question, options, and the correct answer together
quiz_data = {
    1: {
        "question": "What does 'NLP' stand for in AI?",
        "options": ["A) Natural Language Processing", "B) Network Laser Protocol", "C) New Logic Programming"],
        "answer": "A"
    },
    2: {
        "question": "Which company developed the AI model 'Gemini'?",
        "options": ["A) Meta", "B) Google", "C) OpenAI"],
        "answer": "B"
    },
    3: {
        "question": "What is the term for an AI's ability to learn without explicit programming?",
        "options": ["A) Data Mining", "B) Machine Learning", "C) Cloud Computing"],
        "answer": "B"
    },
    4: {
        "question": "The 'Turing Test' is used to determine what?",
        "options": ["A) Battery Life", "B) Processing Speed", "C) Machine Intelligence"],
        "answer": "C"
    }
}

# --- CHAPTER 2: TRACKING VARIABLES ---
score = 0
total_questions = len(quiz_data)

# --- CHAPTER 1 & 3: INTERFACE ---
print("="*40)
print("      WELCOME TO AI-GENIUS QUIZ      ")
print("="*40)
print(f"Total Questions: {total_questions}\n")

# --- CHAPTER 4: LIST ITERATION ---
# Converting dictionary keys to a list to loop through questions
for q_id in quiz_data:
    q_item = quiz_data[q_id]
    
    print(f"Question {q_id}: {q_item['question']}")
    
    # Printing options from the nested list
    for option in q_item['options']:
        print(f"  {option}")
        
    # --- CHAPTER 3: INPUT HANDLING ---
    user_ans = input("\nYour Answer (A/B/C): ").strip().upper()
    
    # Logic to check answer
    if user_ans == q_item['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q_item['answer']}.")
    print("-" * 20)

# --- FINAL SCORE CALCULATION (Ch 2 & 3) ---
percentage = (score / total_questions) * 100

print("\n" + "#"*30)
print(f"QUIZ OVER, {os.getlogin().capitalize()}!") # Ch 1: OS module to get PC name
print(f"Final Score: {score}/{total_questions}")
print(f"Accuracy: {percentage}%")
print("#"*30)

# --- CHAPTER 5: SETS (Unique Topics Covered) ---
topics = {"Natural Language Processing", "General AI", "Machine Learning", "History of AI"}
print(f"\nTopics Mastered: {topics}")
