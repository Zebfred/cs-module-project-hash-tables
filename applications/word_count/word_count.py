import re

def word_count(s):
    # Your code here
    s = s.lower()
    s = s.split(' ')
    words = {}
    for word in s:
        new_word = re.sub(r'[^a-zA-Z0-9]+', '', word)
        if new_word not in words:
            words[new_word] = 1
        else:
            words[new_word] += 1
    return words 


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))