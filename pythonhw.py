# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call (done)
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


def filterBannedApplicants(bannedVisitors, applicants):
    identifiedBannedVisitors=[]
    for user in applicants:
        if user in bannedVisitors:
            identifiedBannedVisitors.append(user)

    return identifiedBannedVisitors

def filterSuccessfulApplicants(bannedVisitors, applicants):
    identifiedSuccessfulVisitors=[]
    for user in applicants:
        if user not in bannedVisitors:
            identifiedSuccessfulVisitors.append(user)
            
    return identifiedSuccessfulVisitors

def processRequest(request):
    applicants = request.get("applicants")
    if not applicants:
        raise Exception("There are no applicants.")
    members = memberStatus.keys()
    bannedApplicants = filterBannedApplicants(bannedVisitors, applicants)
    successfulApplicants = filterSuccessfulApplicants(bannedVisitors, applicants)

    tickets = []
    totalCost = 0

    for visitor in successfulApplicants:
        if visitor in members and memberStatus.get(visitor) == True:
            totalCost += 3.5
            tickets.append({
                "name": visitor,
                "membership": True,
                "ticketPrice": 3.50
            })
        else:
            totalCost += 5
            tickets.append({
                "name": visitor,
                "membership": False,
                "ticketPrice": 5.00
            })
    
    output = {
        "identifiedBannedVisitors": bannedApplicants,
        "totalCost": totalCost,
        "tickets": tickets 
    }

    return output

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