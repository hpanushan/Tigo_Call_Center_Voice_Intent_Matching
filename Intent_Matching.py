
def intent_matching(entity_list):
    # Keywords
    recharge_issue = ['issue','topup', 'balance','recharge','card','credit','amount','reload',
                        'card']
    service_failure = ['failure', 'service','subscribe', 'unsubscribe','alert', 'subscription', 'unsubscription', 
                        'expire','package', 'data', 'voice','activation','deactivation']                       
                         # Subscribe/Unsubscribe
    network_faiulre = ['failure','strength','disconnect','disconnects', 'signal', 'network', 'coverage', 
                        'coverage', 'connectivity', '2G', '3G', '4G ']

    # Counts
    counts = {
        'recharge_issue' : 0,
        'service_failure' : 0,
        'network_faiulre' : 0
    }
    

    for entity in entity_list:
        entity = entity.lower().split()

        for i in entity:
            if i in recharge_issue:
                counts['recharge_issue'] += 1
        
            elif i in service_failure:
                counts['service_failure'] += 1

            elif i in network_faiulre:
                counts['network_faiulre'] += 1

            else: pass
    
    # Selecting the case with maximum value
    max_count =  max(counts.values())   

    # Calculating the threshold
    threshold = max_count * 0.5        
    
    # Checking the cases with max value
    issues = [k for k,v in counts.items() if v >= threshold]

    return issues


#print(intent_matching(['recharge_issue','topup','network_failure','signal strength','service','subscribe']))