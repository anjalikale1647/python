import re

def moderate_text(text, forbidden_words):
    
    for word in forbidden_words:
        
        pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text


feedback = "This product is terrible and bad. Absolutely horrible service!"
blocked_words = ["terrible", "bad", "horrible"]

moderated_feedback = moderate_text(feedback, blocked_words)

print("Original:", feedback)
print("Moderated:", moderated_feedback)