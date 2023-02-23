# create a function to detect spam
def detect_spam(message):
    spam_words = ["lottery", "prize", "winner",
                  "buy", "free", "cash", "urgent", "money", "offer", "Win", "Limited offer"]

    count = 0
    for word in spam_words:
        if word in message.lower():
            count += 1

    if count >= 2:
        return "This message is likely to be spam."
    else:
        return "This message is not spam."


# Usage
message = input("Enter your message: ")
print(detect_spam(message))
