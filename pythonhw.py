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
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho", "Bruce"]
}

def processRequest(request):

    banned = []
    tickets = []
    successful = []

    #5
    if len(request["applicants"]) == 0:
        return ValueError("No applicants")

    # 1
    for i in range(len(bannedVisitors)):
        if bannedVisitors[i] in request["applicants"]:
            banned.append(bannedVisitors[i])
            request["applicants"].remove(bannedVisitors[i])
    
    # 2, 3, 4
    for j in request["applicants"]:
        if j in banned:
            continue
        is_member = memberStatus.get(j, False)
        ticket = {"name": j,
        "membershipStatus": is_member,
        "price": 3.50 if is_member else 5.00}
        if not is_member:
            successful.append(j)
        tickets.append(ticket)

    return {
        "successfulApplicants": successful,
        "bannedApplicatns": banned,
        "totalCost": sum(t['price'] for t in tickets),
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