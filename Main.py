from Entities_Recognition.Entities_Recognition import sample_analyze_entities
from Voice_Recognition.Enhanced_Speech_Recognition import sample_recognize
from Intent_Matching import intent_matching

def main():
    
    text = """Hello, I am Jenny from Dialog customer care service. How may I assist you?
Hello, This is Sam. Today morning I have recharged my mobile with rs 499 reload through your mobile app.
Ok
As I was in a hurry. I haven’t waited till I got the confirmation message.
May I know your problem.
I haven’t got any topup. My balance is same as previous.
Sir, can you please tell your mobile number.
It is 07666666666.
Sir. It might be due to system malfunction. We will try to fix this.
It has been 8 hours since my last recharge. But the problem still persists. May I know how much time does soon mean?
Sir, we are exactly sorry for inconvenience caused to you. But a few of our lines are under repair. The problem might have occurred due to that.
So when I can expect my problem to be solved?
We will definitely clear the issue within next hour.
Okay fine.
Thanks for contacting with us


"""

    # Getting entities from text 
    entity_list = sample_analyze_entities(text)
    
    # Getting correct intent from set of entities
    issues = intent_matching(entity_list)

    print(issues)

if __name__ == "__main__":
    main()

