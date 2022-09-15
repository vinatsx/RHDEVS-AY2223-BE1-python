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
    try:

        applicants = request["applicants"]

        def banned(applicant):
            return True if applicant in bannedVisitors else False

        banned_applicants = list(filter(banned, applicants))
        successful_applicants = [applicant for applicant in applicants if applicant not in banned_applicants]

        def total_sum(applicant_list, member_status):
            status_list = []
            price_list = []
            for applicant in applicant_list:
                if applicant in memberStatus.keys() and memberStatus[applicant] == True:
                    status_list.append(True)
                    price_list.append(3.5)
                else:
                    status_list.append(False)
                    price_list.append(5)
            return status_list, price_list

        status_list, price_list = total_sum(successful_applicants, memberStatus)

        def ticketDict(applicant, status, price):
            ticket_list = []
            for i in range(len(applicant)):
                d = {
                    "name": applicant[i],
                    "membershipStatus": status[i],
                    "price": price[i],
                }
                ticket_list.append(d)
            return ticket_list

        process = {
            "successfulApplicants": successful_applicants,
            "bannedApplicants": banned_applicants,
            "totalCost": sum(price_list),
            "tickets": ticketDict(successful_applicants, status_list, price_list)
        }
        return process
    
    except Exception as e:
        return {
            "error": "No applicants"
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