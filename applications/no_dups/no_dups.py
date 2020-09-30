def no_dups(s):
    # Your code here
    str_thing = ""
    words = {}
    s = str_thing.split(" ")
    for word in s:
        if word not in words:
            words[word] = 1
            s += " " + word
    if s[0] == " ":
                s = s [1:]
    return s    
            



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))