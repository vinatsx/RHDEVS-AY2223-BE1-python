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

def filter_banned(applicant):
    if applicant in bannedVisitors:
        return True
    else:
        return False

def get_membership(filtered_list):
    membership_dict = {}
    for applicant in filtered_list:
        if applicant in memberStatus:
            if memberStatus.get(applicant) is True:
                membership_dict[applicant] = "member"
            else:
                membership_dict[applicant] = "visitor"
        else:
            membership_dict[applicant] = "visitor"
    return membership_dict

def calc_cost(membership_dict):
    total_cost = 0

    for status in membership_dict.values():
        if status == "visitor":
            total_cost+=5.0
        else:
            total_cost+=3.50
    return total_cost


def processRequest(request):
    # Your code here
    try:
        tickets_list = []
        applicants_list = request.get("applicants")
        if not applicants_list:
            raise Exception()
        banned_list = [x for x in filter(filter_banned,applicants_list)]
        for banned in banned_list:
            applicants_list.remove(banned)
        membership_dict = get_membership(applicants_list)
        total_cost = calc_cost(membership_dict)
        for key, value in membership_dict.items():
            if value == "member":
                tickets_list.append({"name":key,"membershipStatus":value,"price":3.50})
            else:
                tickets_list.append({"name":key,"membershipStatus":value,"price":5})
        return {"successfulApplicants":applicants_list,"bannedApplicants":banned_list,"totalCost":total_cost,"tickets":tickets_list}
    except Exception:
       return {"error": "No applicants"}


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