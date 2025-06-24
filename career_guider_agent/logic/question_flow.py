questions = [
    "📌 Konsa subject aapko Matric me sabse zyada pasand tha?",
    "📊 Kis subject me aapke sabse zyada marks aye?",
    "💡 Aapko kis type ka kaam pasand hai? (e.g. tech, helping people, business, art)",
    "🎯 Aap future me kya banna chahtay hain ya kis field me kaam ka irada hai?"
]

def get_next_question(step):
    return questions[step] if step < len(questions) else None
