def build_prompt(answers):
    return f"""
A student just completed Matric and gave the following answers:

- Favorite Subject: {answers.get('favorite_subject')}
- Highest Marks In: {answers.get('highest_marks')}
- Enjoys: {answers.get('interest')}
- Future Goal: {answers.get('future_goal')}

Suggest the best post-Matric field (FSc, ICS, ICom, DAE etc.).
Reply in short, kind Urdu-English mix.
"""
