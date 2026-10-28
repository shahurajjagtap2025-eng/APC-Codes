# 17. develop a tool to analyze social media posts and extract all hashtags 
import re

def extract_hashtags(text):
    return re.findall(r'#[A-Za-z0-9_]+', text)

text = input("Enter a social media post: ")

hashtags = extract_hashtags(text)

print(hashtags)

