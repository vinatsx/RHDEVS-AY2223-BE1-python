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

bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": []
}
def filterbanned(bannedVisitors, applicants):
        banned=[]
        for i in applicants: 
            if i in bannedVisitors:
                banned.append(i)
        return banned
    
def filtersuccessful(bannedVisitors, applicants):
        successful=[]
        for i in applicants: 
            if i not in bannedVisitors:
                successful.append(i)
        return successful   
    
def processRequest(request):
    applicants = request.get("applicants")
    if not applicants:
        raise Exception("There are no applicants")
    members = memberStatus.keys()
    bannedApplicants = filterbanned(bannedVisitors, applicants)
    successfulApplicants = filtersuccessful(bannedVisitors, applicants)

    totalCost=0
    tickets = []
    for i in successfulApplicants:
        if i in members and memberStatus[i] == True:
            totalCost += 3.50
            tickets.append({
                "name": i,
                "membershipStatus": True,
                "price": 3.50
                    })
        else:
            totalCost += 5
            tickets.append({
                "name": i,
                "membershipStatus": False,
                "price": 5
                })
    return tickets, totalCost

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