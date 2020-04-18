from Entities_Recognition.Entities_Recognition import sample_analyze_entities
from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching

def main():
    
    # Pass the recording to Google speech to text API
    #file_path = 'Data/Dual_Channel/WhatsApp Audio 2020-04-16 at 13.26.55.wav'
    #text = sample_recognize(file_path)

    text = """
Hello.
Hello madam. I am David from Dialog customer care. How can I assist you?
I have an issue with Dialog 4G broadband download speed. It is 680 kbps. So it is too slow and I am very disappointed.
Sorry sir. We do understand your concern. Can you please tell me your mobile and NIC number?
Yes sure. Mobile is 07111111111. And NIC is 8717166176271V.
Please wait a moment to check this issue.
Yes sure.
Thanks for waiting sir. It seems to be a network issue. Now our team is working on this matter. We are really sorry for the experience you are having. 
When is the estimated date that this will be fixed?
Sorry sir. It takes time to fix. We already escalate this to relevant. Please bare with us till we provide you the best service.
Okay.
Thank for calling. Have a nice day.



"""

    # Getting entities from text 
    entity_list = sample_analyze_entities(text)
    
    # Getting correct intent from set of entities
    issues = intent_matching(entity_list)

    print(issues)

if __name__ == "__main__":
    main()

