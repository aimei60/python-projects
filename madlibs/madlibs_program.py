def read_file(storyfile):
    with open(storyfile, 'r') as file:
        storyfile = file.read()
        return storyfile
    
def madlibs():
    new_words = set()
    target_start = "<"
    target_end = ">"
    
    original_text = read_file("storyfile.txt")
    words = original_text.split()
    
    for word in words:
        if target_start in word and target_end in word:
            new_words.add(word)
      
    answers = {}

    for word in new_words:
        answer = input("Enter a " + word + ": ")
        answers[word] = answer
            
    for word in new_words:
        original_text = original_text.replace(word, answers[word])
            
    print(original_text)

madlibs()