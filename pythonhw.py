# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

from venv import create


bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


def processRequest(request):
    if len(request['applicants']) == 0: 
        raise Exception("Sorry, there are no applicants.")
    else: 
        filteredUsers = filterUsers(bannedVisitors, request['applicants'])
        responseDict = {
            'successfulApplicants': str(filteredUsers['successfulApplicants']),
            'bannedApplicants': str(filteredUsers['identifiedUsers']), 
            'totalCost': str(calculatePrice(request['applicants'])),
            'tickets': createTicket(request['applicants'])
        }
    return responseDict
        


def filterUsers(bannedUsers, applicants): 
    identifiedBannedUsers = []
    successfulApplicants = []
    for user in applicants: 
        if user in bannedUsers:
            identifiedBannedUsers.append(user)
            applicants.remove(user) 
        else: 
            successfulApplicants.append(user)
    users = {
        "identifiedUsers": identifiedBannedUsers,
        "successfulApplicants": successfulApplicants
    }    
    return users

def calculatePrice(applicants):
    price = 0 
    for member in applicants: 
        if memberStatus.__contains__(member): 
            if memberStatus[member]: 
                price += 3.5
            else: 
                price += 5
        else: 
            price += 5 
    return str(price)
    
def createTicket(applicants):
    tickets = []
    for member in applicants:
        if memberStatus.__contains__(member):
            if memberStatus[member]: 
                indivTicket = {
                    "name": member,
                    "membershipStatus": memberStatus[member],
                    "price": "3.50" 
                }
                tickets.append(indivTicket)
            else:  
                indivTicket = {
                    "name": member,
                    "membershipStatus": memberStatus[member],
                    "price": "5" 
                }
                tickets.append(indivTicket)
        else: 
            indivTicket = {
                "name": member,
                "membershipStatus": "False",
                "price": "5" 
            }
            tickets.append(indivTicket) 
    return tickets

print(processRequest(request))

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
#
# }


# OR

# {"error": "No applicants"}