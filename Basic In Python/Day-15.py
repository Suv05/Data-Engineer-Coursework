# KBC game stages
stages = [
    {
        "question": "Who is the Prime Minister of India?",
        "ans": "modi",
        "options": ["obama", "rajendra", "modi", "lalita"],
        "prize": "$10"
    },
    {
        "question": "Who was the first President of India?",
        "ans": "rajendra",
        "options": ["obama", "rajendra", "modi", "lalita"],
        "prize": "$50"
    },
    {
        "question": "Who is known as the Iron Man of India?",
        "ans": "lal",
        "options": ["obama", "rajendra", "modi", "lal"],
        "prize": "$20"
    },
    {
        "question": "Who is the Chief Minister of Odisha?",
        "ans": "nabin",
        "options": ["obama", "nabin", "modi", "lalita"],
        "prize": "$30"
    },
    {
        "question": "What is the national song of India?",
        "ans": "vande-mataram",
        "options": ["vande-mataram", "rajendra", "modi", "lalita"],
        "prize": "$40"
    }
]

# intialize total price
total_prize = 0

for stage in stages:
    print("\nQuestion: ", stage["question"])
    print("Options:")

    for idx, option in enumerate(stage["options"], 1):
        print(f"{idx: }-{option}")

    answer = input("Enter your answer: ").lower()
    if answer == stage["ans"]:
        print(f"Correct! You win {stage['prize']}")
        total_prize += int(stage['prize'].replace("$",""))
    else:
        print("Incorrect answer. Game Over!")
        break

print(f"\nTotal prize money you get: {total_prize}")
