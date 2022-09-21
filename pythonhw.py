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
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


bannedVisitors = ["Charles", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

def filterBannedApplicants(applicants):
    bannedApplicants = []
    for x in applicants:
        if x in bannedVisitors:
            bannedApplicants.append(x)

    return bannedApplicants

def filterSuccessfulApplicants(applicants):
    successfulApplicants = []
    for x in applicants:
        if x not in bannedVisitors:
            successfulApplicants.append(x)

    return successfulApplicants 

def processRequest(request):
    applicants = request.get("applicants")
    if not applicants:
        raise Exception("No applicants found.")
    members = memberStatus.keys()
    bannedApplicants = filterBannedApplicants(applicants)
    SuccessfulApplicants = filterSuccessfulApplicants(applicants)

    tickets = []
    totalCost = 0

    for successfulPeople in SuccessfulApplicants:
        if successfulPeople in members and memberStatus.get(successfulPeople) == True:
            totalCost += 3.5
            tickets.append({
                "name": successfulPeople,
                "membershipStatus": True,
                "price": 3.50
            })
        else:
            totalCost += 5
            tickets.append({
                "name": successfulPeople,
                "membershipStatus": False,
                "price": 5
            })

    output = {
        "successfulApplicants": SuccessfulApplicants,
        "bannedApplicants": bannedApplicants,
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