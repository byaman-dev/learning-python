'''
PROJECT: AI-Genius Master v2.0
FEATURES: 20 Categorized Questions, Bi-Topic Selection, Score Analytics.
CONCEPTS: Nested Dicts (Ch 5), List Processing (Ch 4), String Cleaning (Ch 3).
'''

import os

# --- CHAPTER 5: THE CORE DATABASE (Nested Dictionary) ---
# Separating content into two distinct modules for better data management
quiz_data = {
    "Cybersecurity": {
        1: {"q": "What is the main goal of a Firewall?", "o": ["A) Filter traffic", "B) Speed up internet"], "a": "A"},
        2: {"q": "What is 'Phishing'?", "o": ["A) A network protocol", "B) Social engineering"], "a": "B"},
        3: {"q": "What does VPN stand for?", "o": ["A) Virtual Private Network", "B) Visual Port Node"], "a": "A"},
        4: {"q": "Which is a 'strong' password trait?", "o": ["A) Your birthday", "B) Random symbols"], "a": "B"},
        5: {"q": "What is Ransomware?", "o": ["A) Data kidnapping", "B) Free software"], "a": "A"},
        6: {"q": "What is 2FA?", "o": ["A) Second-Factor Auth", "B) Two-File Access"], "a": "A"},
        7: {"q": "What is a 'Botnet'?", "o": ["A) A robot network", "B) A group of infected PCs"], "a": "B"},
        8: {"q": "What does HTTPS provide?", "o": ["A) Faster loading", "B) Encryption"], "a": "B"},
        9: {"q": "What is a Zero-Day?", "o": ["A) A new vulnerability", "B) A holiday for hackers"], "a": "A"},
        10: {"q": "What is a 'SQL Injection'?", "o": ["A) Database attack", "B) Hardware failure"], "a": "A"}
    },
    "Artificial Intelligence": {
        1: {"q": "What is 'Machine Learning'?", "o": ["A) Robots building robots", "B) Learning from data"], "a": "B"},
        2: {"q": "Which is an AI LLM?", "o": ["A) GPT-4", "B) MP3"], "a": "A"},
        3: {"q": "What is 'NLP'?", "o": ["A) Natural Language Processing", "B) New Logic Part"], "a": "A"},
        4: {"q": "Who is Alan Turing?", "o": ["A) A movie star", "B) The father of AI"], "a": "B"},
        5: {"q": "What is a 'Neural Network'?", "o": ["A) Computer brain model", "B) An ISP"], "a": "A"},
        6: {"q": "What is 'Computer Vision'?", "o": ["A) Eye surgery", "B) Image recognition"], "a": "B"},
        7: {"q": "What is AGI?", "o": ["A) General Intelligence", "B) Gaming Interface"], "a": "A"},
        8: {"q": "What is 'Deep Learning'?", "o": ["A) Multi-layer ML", "B) Underwater AI"], "a": "A"},
        9: {"q": "What is AI 'Bias'?", "o": ["A) High speed", "B) Unfair results"], "a": "B"},
        10: {"q": "Which AI plays Go?", "o": ["A) AlphaGo", "B) Siri"], "a": "A"}
    }
}

# --- CHAPTER 1-4: APPLICATION LOGIC ---
def run_app():
    score = 0
    categories = list(quiz_data.keys()) # Ch 4: List from dict keys

    print("="*45)
    print("      🚀 AI-GENIUS INTELLIGENCE v2.0      ")
    print("="*45)
    
    # Topic Selection (Ch 2/3)
    print(f"\nChoose your path:\n1. {categories[0]}\n2. {categories[1]}")
    choice = input("\nEnter choice (1/2): ").strip()

    if choice == "1":
        active_topic = categories[0]
    elif choice == "2":
        active_topic = categories[1]
    else:
        print("Invalid entry. Exiting.")
        return

    # Quiz Loop
    print(f"\n--- {active_topic.upper()} MODULE LOADED ---")
    current_questions = quiz_data[active_topic]

    for q_id, info in current_questions.items():
        print(f"\nQ{q_id}: {info['q']}")
        for opt in info['o']:
            print(f"  {opt}")
        
        # Ch 3: Sanitizing Input
        user_ans = input("Your Answer (A/B): ").strip().upper()
        
        if user_ans == info['a']:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❗ Incorrect. Correct answer: {info['a']}")

    # Final Analytics (Ch 2)
    accuracy = (score / 10) * 100
    print("\n" + "#"*40)
    print(f"TOPIC: {active_topic} | SCORE: {score}/10")
    print(f"SUCCESS RATE: {accuracy}%")
    print("#"*40)

if __name__ == "__main__":
    run_app()
