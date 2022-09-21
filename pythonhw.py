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


def processRequest(request):
    applicant_list = request.get("applicants")
    if not applicant_list:
        raise Exception("No applicants lah don't anyhow")
    
    banned_applicants = identifyBanned(applicant_list)
    successful_applicants = identifySuccessful(applicant_list)
    members = memberStatus.keys()
    
    total_cost = 0
    tickets = []

    for name in applicant_list:
        if name in members and memberStatus.get(name) == True:
            total_cost += 3.5
            tickets.append({
                "Name": name,
                "Membership Status": True,
                "Ticket Price": "$3.50"
            })
        else:
            total_cost += 5
            tickets.append({
                "Name": name,
                "Membership Status": False,
                "Ticket Price": "$5.00"
            })
    display = {
        "Banned Applicants": banned_applicants,
        "Total Price": total_cost,
        "Tickets": tickets
    }

    return display


        
def identifyBanned(applicants):
    banned = []
    for name in applicants:
        if name in bannedVisitors:
            banned.append(name)
    return banned

def identifySuccessful(applicants):
    successful = []
    for name in applicants:
        if name not in bannedVisitors:
            successful.append(name)
    return successful


        

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