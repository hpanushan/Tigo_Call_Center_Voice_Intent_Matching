from Entities_Recognition.Entities_Recognition import sample_analyze_entities
from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching

def main():
    
    text = """hello hello how can I help you I have his shoe when I try to pop up my balance 
    I have you but it didn't work out like request cannot be completed could you please help them used for this
    how you speak maybe you don't have online shopping facility could you please check with another bank
    yeah issue thank you"""

    # Getting entities from text 
    entity_list = sample_analyze_entities(text)
    
    # Getting correct intent from set of entities
    issues = intent_matching(entity_list)

    print(issues)

if __name__ == "__main__":
    main()

