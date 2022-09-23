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
    # Your code here
  try:
    tickets={}
    member={}
    human={}
    big_dict={}
    totalCost=0
    successfulApplicants=list(filter(lambda a:a not in bannedVisitors,request['applicants']))
    bannedApplicants=list(filter(lambda a:a in bannedVisitors,request['applicants']))
  
    for name in successfulApplicants:
      if name in memberStatus:
        if memberStatus[name]:
          member[name]=True
          tickets[name]=3.50
          totalCost+=3.50
        else:
          member[name]=False
          tickets[name]=5
          totalCost+=5
      else:
        member[name]=False
        tickets[name]=5
        totalCost+=5
    big_dict["successfulApplicants"]=successfulApplicants
    big_dict["bannedApplicants"]=bannedApplicants
    big_dict["totalCost"]=totalCost
    big_dict["tickets"]=[]
    
    for name in successfulApplicants:
      human['name']=name
      human['membershipStatus']=member[name]
      human['price']=tickets[name]
      big_dict["tickets"].append(human.copy())
    
  
      
    return big_dict
  except:
    small_dict={}
    small_dict['error']="No applicants"
    return small_dict



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
