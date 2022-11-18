import json
class Checking:
    """Constructor function with price and discount"""

    def __init__(self, db_all, person, checking_strategy=None):

        """take price and discount strategy"""

        self.db_all = db_all
        self.person = person
        if checking_strategy:
          self.checking_strategy = eval(checking_strategy)
        else:
            self.checking_strategy=checking_strategy

    """A separate function for price after discount"""

    async def matching(self):

        if self.checking_strategy:
            ls_matched = self.checking_strategy(self)
        else:
            x = {
                "matches": []

            }

            ls_matched = x


        return ls_matched




"""function dedicated to strategy of detecting fraud"""



def strategyOne(data):



    x = {
        "matches": []

    }
    ls_matched=[]
    for a in data.db_all:
        if a.identification==data.person.identification:
            y={"first_name":a.first_name,"last_name":a.last_name,"birthdate":a.birthdate,"identification":a.identification,"probability":"1"}
            x["matches"] += [y]

    if len(x["matches"])>1:
        newlist = sorted(x["matches"], key=lambda d: d['first_name'])
        x["matches"]=newlist

    ls_matched = x
    return ls_matched





