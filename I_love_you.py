import random

fortunes = [
    "I love you.",
    
]

def get_fortune():
    return random.choice(fortunes)

if __name__ == "__main__":
    print("🍪 Your fortune cookie says:")
    print(get_fortune())
    print("\nEnjoy your day! 🎉")
