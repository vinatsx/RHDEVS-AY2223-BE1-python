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
    "Brendan": False,
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}


def is_banned(x, bannedVisitors):
    if x in bannedVisitors:
        return True
    else:
        return False

def total_cost(y):
    total = 0
    for i in y:
        if memberStatus[i] == True:
            total += 3.50
        else:
            total += 5.00
    return total

def processRequest(request):
    result ={}
    result["successfulApplicants"] = list(filter(lambda x: is_banned(x, bannedVisitors)==False, request["applicants"]))
    result["bannedApplicants"] = list(filter(lambda x: is_banned(x, bannedVisitors)==True, request["applicants"]))
    result["totalCost"] = total_cost(request["applicants"])
    result["tickets"] = []
    for i in request["applicants"]:
        x = input(f"Is {i} a member?")
        print(x)
        if x.lower() == "yes":
            memberStatus[i] = True
        if x.lower() == "no":
            memberStatus[i] = False
     
        result["tickets"].append({
            "name": i, 
            "membershipStatus": memberStatus[i], 
            "price": total_cost([i])
        })
    if request["applicants"] == []:
        raise Exception({"error": "No applicants"})
    return result


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
