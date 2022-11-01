## Paths to data files
filename = {}
path = {}

## Paths to element locations in the underlying data tables.
county_xpath = {}
trump_percentage = {}
trump_votes = {}
biden_percentage = {}
biden_votes = {}
jorgensen_percentage = {}
jorgensen_votes = {}
west_percentage = {}
west_votes = {}
other_percentage = {}
other_votes = {}

# Arkansas
filename["ar"] = "ar.html"
path["ar"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=10]/tbody"
county_xpath["ar"] = "./td[position()=1]/a"

trump_percentage["ar"] = "./td[position()=2]/b"
trump_votes["ar"] = "./td[position()=3]/i"
biden_percentage["ar"] = "./td[position()=4]/b"
biden_votes["ar"] = "./td[position()=5]/i"
jorgensen_percentage["ar"]="./td[position()=6]/b"
jorgensen_votes["ar"] = "./td[position()=7]/i"
west_percentage["ar"]="./td[position()=8]/b"
west_votes["ar"] = "./td[position()=9]/i"
other_percentage["ar"]="./td[position()=10]/b"
other_votes["ar"] = "./td[position()=11]/i"


# Alabama
county_xpath["al"] = "./td[position()=1]/a"
trump_percentage["al"] = "./td[position()=2]/b"
biden_percentage["al"] = "/html/body/div[3]/div[3]/div[5]/div[1]/table[8]/tbody/tr[1]/td[4]/b"


# Arizona
filename["az"] = "az.html"
path["az"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=10]/tbody"


# Califorina
filename["ca"] = "ca.html"
path["ca"] = "/html/body/div[position()=3]/div[position()=3]/div[position()=5]/div[position()=1]/table[position()=15]/tbody"

county_xpath["ca"] = "./td[position()=1]"
trump_percentage["ca"] = "./td[position()=4]/b"
trump_votes["ca"] = "./td[position()=5]/i"
biden_percentage["ca"] = "./td[position()=2]/b"
biden_votes["ca"] = "./td[position()=3]/i"










