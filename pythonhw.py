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

bannedVisitors = ["Amy", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

def filterSuccessfulVisitors(applicant):
    return applicant not in bannedVisitors

def filterBannedVisitors(applicant):
    return applicant in bannedVisitors

def calculatePrice(applicant):
    if applicant not in memberStatus or not memberStatus[applicant]:
        return 5
    else:
        return 3.5

def generateTicket(applicant, price):
    if applicant not in memberStatus:
        ms = False
    else:
        ms = memberStatus[applicant]
    return {
        "name": applicant,
        "membershipStatus": ms,
        "price": price
    }

def processRequest(request):
    # Your code here
    try:
        successfulApplicants = list(filter(filterSuccessfulVisitors, request["applicants"]))
        bannedApplicants = list(filter(filterBannedVisitors, request["applicants"]))
        totalCost = 0
        tickets = []
        for applicant in successfulApplicants:
            price = calculatePrice(applicant)
            totalCost += price
            tickets.append(generateTicket(applicant, price))
    except:
        return {"error": "No applicants"}

    return {
        "successfulApplicants": successfulApplicants,
        "bannedApplicants": bannedApplicants,
        "totalCost": totalCost,
        "tickets": tickets
    }


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