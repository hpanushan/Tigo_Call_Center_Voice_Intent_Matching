
def intent_matching_google(entity_list):
    # Counts
    counts = {
        'recharge_issue' : 0,
        'service_failure' : 0,
        'network_faiulre' : 0
    }

    ##### Layer 01
    # Keywords
    recharge_issue = ['topup', 'balance','recharge','card','credit','amount','reload',
                        'card','transfer']
    service_failure = ['service','services','subscribe', 'unsubscribe','alert','alerts'
                        'subscription' 'subscriptions','unsubscription', 'expire','package', 'data', 'voice','activation',
                        'deactivation','bill','bills','basis']                       
                         # Subscribe/Unsubscribe
    network_faiulre = ['strength','disconnect','disconnects', 'signal', 'signals','network', 'coverage', 
                        'coverage', 'connectivity', '2G', '3G', '4G ','poor','noise','noises','speed']

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

    
    # Sorting dictionary by its value
    counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    
    # Selecting the case with maximum value
    max_count =  max(counts.values())   

    # Calculating the threshold
    threshold = max_count * 0.5        
    
    # Checking the cases with max value
    issues = [k for k,v in counts.items() if v >= threshold]

    return issues


#print(intent_matching(['recharge_issue','topup','network_failure','signal strength','service','subscribe']))