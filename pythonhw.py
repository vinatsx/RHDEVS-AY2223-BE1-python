# This program simulates the backend of a ticket purchasing system

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

def identifyBannedVisitors(applicants):
    bannedApplicants = []
    for applicant in applicants:
        if applicant in bannedVisitors:
            bannedApplicants .append(applicant)
    
    return bannedApplicants

def identifySuccessfulApplicants(applicants):
    successfulApplicants = []
    for applicant in applicants:
        if applicant not in bannedVisitors:
            successfulApplicants.append(applicant)
    
    return successfulApplicants


def processRequest(request):
    try:
        applicants = request.get("applicants")
        members = memberStatus.keys()

        #1. Identify all banned visitors with a filter call
        bannedApplicants = identifyBannedVisitors(applicants)
        successfulApplicants = identifySuccessfulApplicants(applicants)

        # 2. Determine the memberships status of all applicants
        # 3. Calculate the total price for all eligible visitors
        # 4. For each valid visitor, return a corresponding ticket in Dictionary form
        tickets = []
        totalCost = 0

        for successfulApplicant in successfulApplicants:
            if successfulApplicant in members and memberStatus.get(successfulApplicant) == True:
                totalCost += 3.5
                tickets.append({
                    "name": successfulApplicant,
                    "membershipStatus": True,
                    "price": 3.50
                })
            else:
                totalCost += 5
                tickets.append({
                    "name": successfulApplicant,
                    "membershipStatus": False,
                    "price": 5
                })
        
        output = {
            "successfulApplicants": successfulApplicants,
            "bannedApplicants": bannedApplicants,
            "totalCost": totalCost,
            "tickets": tickets

        }

        return output
    
    # 5. Return an error via thrown exception if applicants is empty
    except:
        return {"error": "No applicants"}
        

print(processRequest(request))

# {
#   successfulApplicants:
#   bannedApplicants:
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