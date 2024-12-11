## generate a simple dataset for clustering.
import random
#Abd
pos_lexicon = ["joy", "love", "happy", "bright", "cheerful", "beautiful", "fantastic", "wonderful",
    "brilliant", "excellent", "amazing", "delightful", "splendid", "optimistic", "fabulous",
    "fantastic", "inspiring", "radiant", "uplifting", "peace", "harmony", "laughter",
    "success", "kindness", "gratitude", "hope", "achievement", "adventure", "compassion",
    "friendship", "celebration", "generous", "vibrant", "trustworthy", "lively", "passionate",
    "nurturing", "playful", "creative", "supportive", "thrilling", "phenomenal", "resilient",
    "curious", "motivating", "extraordinary", "empathetic", "joyous", "charming", "exciting",
    "lovely", "satisfying", "dazzling", "witty", "refreshing", "serene", "elegant", "captivating",
    "graceful", "humorous", "dazzling", "adventurous", "flourishing", "memorable", "purposeful",
    "brightening", "engaging", "considerate", "uplifting", "blessed", "enthusiastic", "enchanting",
    "nurturing", "supportive", "promising", "fulfilling", "radiant", "zealous", "harmonious",
    "invigorating", "optimistic", "thoughtful", "wise", "generous", "marvelous", "supportive",
    "joyous", "fulfilling", "harmonious", "inspiring", "respectful", "captivating", "encouraging",
    "motivating", "sparkling", "joyful", "delightful", "wonderful", "spirited", "thriving"]

neg_lexicon = ["pain", "hate", "sadness", "dark", "gloomy", "terrible", "awful", "dreadful", "miserable",
    "disastrous", "negative", "fearful", "angry", "frustrating", "hurt", "lonely", "bitter",
    "resentful", "jealous", "chaotic", "suffering", "toxic", "empty", "pessimistic", "confusion",
    "hostility", "rage", "disappointment", "shame", "anguish", "regret", "weakness", "despair",
    "threat", "loss", "grief", "stressful", "turmoil", "burden", "betrayal", "desperate",
    "abrasive", "hostile", "dismal", "resentful", "dangerous", "haunting", "aggressive",
    "toxic", "vile", "daunting", "chaotic", "draining", "hopeless", "destructive", "enraged",
    "frustrated", "gloomy", "sorrowful", "fractured", "lost", "troubled", "alarming", "unsettling",
    "anxious", "pessimistic", "cynical", "defensive", "harsh", "oppressive", "shattered",
    "bleak", "sour", "untrustworthy", "withdrawn", "selfish", "bitter", "despairing", "hostile",
    "fractured", "regretful", "vicious", "stressful", "turbulent", "chaotic", "cynical",
    "overwhelmed", "resentful", "hopeless", "indifferent", "negative", "jarring", "disheartening",
    "anxious", "toxic", "fragile", "stagnant", "disturbing", "tumultuous", "abrasive"
]

def create_docs(npos, nneg) :
    length = 100
    pos_docs = []
    neg_docs = []
    for i in range(npos) :
        d = [random.choice(pos_lexicon) for j in range(length)]
        pos_docs.append(d)
    for j in range(nneg) :
        d = [random.choice(neg_lexicon) for j in range(length)]
        neg_docs.append(d)

    return (pos_docs, neg_docs)