import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Basic keyword list for demo (extend as needed)
SKILL_KEYWORDS = [
    'python', 'java', 'c++', 'excel', 'communication', 'management', 'design',
    'html', 'css', 'react', 'javascript', 'sql', 'recruitment', 'teamwork',
    'photoshop', 'illustrator', 'leadership', 'analytics', 'data', 'figma'
]

def extract_skills(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    filtered_tokens = [w for w in tokens if w not in stopwords.words('english')]

    # Extract skills present in the resume
    extracted = [skill for skill in SKILL_KEYWORDS if skill in filtered_tokens]
    return list(set(extracted))
