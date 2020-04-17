from Entities_Recognition.Entities_Recognition import sample_analyze_entities
from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching

def main():
    
    # Pass the recording to Google speech to text API
    #file_path = 'Data/Dual_Channel/WhatsApp Audio 2020-04-16 at 13.26.55.wav'
    #text = sample_recognize(file_path)

    text = """Hello
Hello. I am Rixy from Dialog service center. How can I help you.
Yesterday I activated 399 data package. After that I have lost all my credit balance. Earlier I had 500 credit amount.
What is your mobile number?
It is 09811111111.
Could you give me a moment. Let me check out that.
Okay
Sir, your problem is solved now. Now you have the data package.
What about my credit balance?
You will get your credit amount as a reload within a hour.
Ok. Thanks
Thank you.



"""

    # Getting entities from text 
    entity_list = sample_analyze_entities(text)
    
    # Getting correct intent from set of entities
    issues = intent_matching(entity_list)

    print(issues)

if __name__ == "__main__":
    main()

