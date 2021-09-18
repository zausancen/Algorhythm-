def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("anitalavalatina"))
    
if __name__=='__main__':
    run()