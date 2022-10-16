# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call                DONE
# 2. Determine the memberships status of all applicants             
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

import re


bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

# request = {
#     "applicants": []
# }


def processRequest(request):
    try:
        if len(request["applicants"] == 0):
            raise Exception("No Applicants")

        def is_banned(x):
            if x in bannedVisitors:
                return True
            else:
                return False
            
        bannedApplicants = list(filter(is_banned, request["applicants"]))

        #status = []
        applicants = request["applicants"]
        def stat(x):
            if x in memberStatus.keys() and memberStatus[x] == True:
                return True
            else:
                return False
        
        def not_is_banned(x):
            if x in bannedVisitors:
                return False
            else:
                return True

        visitors = list(filter(not_is_banned, request["applicants"]))
        #visitors = list(filter(is_member, visitors1))

    
        def calculate_total():
            totalPrice = 0
            for i in range(len(visitors)): 
                if visitors[i] not in memberStatus.keys() or memberStatus[visitors[i]] == False:
                    totalPrice = totalPrice + 5

                else:
                    totalPrice = totalPrice + 3.5
            return totalPrice

        def price_pax(x):
                if x not in memberStatus.keys() or memberStatus[x] == False:
                    return 5
                else:
                    return 3.5
        
        def give_ticket():
            ticket = []
            for i in range(len(visitors)):
                ticket.append({
                    "name": visitors[i],
                    "membershipStatus": stat(visitors[i]),
                    "price": price_pax(visitors[i])
                })
            return ticket
        return give_ticket()

    except:
        return {"error": "No applicants"}
        


    

print(processRequest(request))
#processRequest(request)




# {
#   successfulApplicants:
#   bannedApplicatns:
#   totalCost:
#   tickets: [
#       {
#            "name": ,
#            "membershipStatus": ,
#            "price":
#       }, ....
#   ]

# }


# OR

# {"error": "No applicants"}