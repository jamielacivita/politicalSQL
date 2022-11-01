## Paths to data files
filename = {}
path = {}

filename["ar"] = "ar.html"
path["ar"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=10]/tbody"

filename["az"] = "az.html"
path["az"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=10]/tbody"

filename["ca"] = "ca.html"
path["ca"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=15]/tbody"


## Paths to element locations

#County
county_xpath = {}
county_xpath["al"] = "./td[position()=1]/a"
county_xpath["ar"] = "./td[position()=1]/a"
county_xpath["ca"] = "./td[position()=1]"

## Trump
trump_percentage = {}
trump_percentage["al"] = "./td[position()=2]/b"
trump_percentage["ar"] = "./td[position()=2]/b"
trump_percentage["ca"] = "./td[position()=4]/b"

trump_votes = {}
trump_votes["ca"] = "./td[position()=5]/i"
trump_votes["ar"] = "./td[position()=3]/i"

## Biden
biden_percentage = {}
biden_percentage["al"] = "/html/body/div[3]/div[3]/div[5]/div[1]/table[8]/tbody/tr[1]/td[4]/b"
biden_percentage["ca"] = "./td[position()=2]/b"
biden_percentage["ar"] = "./td[position()=4]/b"

biden_votes = {}
biden_votes["ca"] = "./td[position()=3]/i"
biden_votes["ar"] = "./td[position()=5]/i"


