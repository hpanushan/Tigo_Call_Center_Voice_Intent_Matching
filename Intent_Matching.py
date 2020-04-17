
def intent_matching(entity_list):
    # Keywords
    recharge_issue = ['recharge issue','topup', 'balance','recharge','recharge card','credit','credit amount']
    service_failure = ['service failure', 'service','subscribe', 'unsubscribe','alert', 'subscription', 'unsubscription', 'expire']                             # Subscribe/Unsubscribe
    network_faiulre = ['network failure','signal strength','disconnect','disconnects', 'signal', 'network', 'coverage', 
                        'network coverage']

    # Counts
    counts = {
        'recharge_issue' : 0,
        'service_failure' : 0,
        'network_faiulre' : 0
    }
    

    for entity in entity_list:
        if entity.lower() in recharge_issue:
            counts['recharge_issue'] += 1
        
        elif entity.lower() in service_failure:
            counts['service_failure'] += 1

        elif entity.lower() in network_faiulre:
            counts['network_faiulre'] += 1

        else: pass
    
    # Selecting the case with maximum value
    max_count =  max(counts.values())           
    
    # Checking the cases with max value
    issues = [k for k,v in counts.items() if v == max_count]

    return issues


#print(intent_matching(['recharge_issue','topup','network_failure','signal strength','service','subscribe']))