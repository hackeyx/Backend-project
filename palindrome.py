text: str = input()


def iseven():
    for i in text:
        if len(text) / 2 == len(text) // 2:
            return "even"
        else:
            return "odd"


iseven()

if iseven() == "even":
    for i in text:
        this = len(text) // 2
        hmm = this
        hmmm = this
        print(text[:hmm])
        print(text[hmmm:])
        hmmmm = text[hmmm:]
        ok = hmmmm[::-1]
        print("opposite of the left side- " + ok)
        if ok == text[:hmm]:
            print("word is palindrome")
        else:
            print("word is not palindrome")
        break
else:
    for i in text:
        string1 = ""
        this = len(text) // 2
        okay = list(text)
        okay.pop(this)
        for e in okay:
            string1 += str(e)
        print(string1)
        hmm = this
        hmmm = this
        print(string1[:hmm])
        print(string1[hmmm:])
        hmmmm = string1[hmmm:]
        ok = hmmmm[::-1]
        print("opposite of the left side- " + ok)
        if ok == text[:hmm]:
            print("word is palindrome")
        else:
            print("word is not palindrome")
        break