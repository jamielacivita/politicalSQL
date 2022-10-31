class row():
    state = None
    row_e = None
    county = None

    trump_percentage = None
    trump_votes = None

    biden_percentage = None
    biden_votes = None

    Jorgensen_percentage = None
    Jorgensen_votes = None

    WriteIn_percentage = None
    WriteIn_votes = None

    def set_row_state(self,state):
        self.state = state

    def set_row_e(self,e):
        self.row_e = e
        self.parse_row_e()

    def parse_row_e(self):
        #set the xpaths
        county_xpath = {}
        county_xpath["al"]="./td[position()=1]/a"
        county_xpath["ca"]="./td[position()=1]"


        trump_percentage = {}
        trump_percentage["al"] = "./td[position()=2]/b"
        trump_percentage["ca"] = "./td[position()=4]/b"

        trump_votes = {}
        trump_votes["ca"]="./td[position()=5]/i"

        biden_percentage = {}
        biden_percentage["ca"]="./td[position()=2]/b"

        biden_votes = {}
        biden_votes["ca"]="./td[position()=3]/b"


        #set the country
        print(self.row_e.attrib)
        print(self.row_e.keys())
        print(self.row_e.xpath(county_xpath[self.state]))
        self.county = self.row_e.xpath(county_xpath[self.state])[0].text
        #print(self.county)

        #set the trump data
        #trump precentage
        self.trump_percentage = self.row_e.xpath(trump_percentage[self.state])[0].text
        self.trump_percentage = float(self.trump_percentage.replace("%",""))

        #print(self.trump_percentage)

        #trump votes
        self.trump_votes = self.row_e.xpath(trump_votes[self.state])[0].text
        self.trump_votes = int(self.trump_votes.replace(",", ""))

        #print(self.trump_votes)

        #set the biden data
        #biden precentage
        self.biden_percentage = self.row_e.xpath(biden_percentage[self.state])[0].text
        self.biden_percentage = float(self.biden_percentage.replace("%", ""))

        #print(self.biden_percentage)

        #biden votes
        self.biden_votes = self.row_e.xpath(biden_votes[self.state])[0].text
        self.biden_votes = int(self.biden_votes.replace(",", ""))
        #print(self.biden_votes)



    def get_county(self):
        return self.county

    def get_trump_votes(self):
        return self.trump_votes

    def get_trump_percentage(self):
        return self.trump_percentage

    def get_biden_votes(self):
        return self.biden_votes

    def get_biden_percentage(self):
        return self.biden_percentage


    def __str__(self):
        c = self.get_county()
        print(c)
        print("\t" + "Trump votes : " + str(self.trump_votes))
        print("\t" + "Biden votes : " + str(self.biden_votes))
        print("\t" + "Jorgensen votes : " + str(self.jorgensen_votes))
        print("\t" + "Write-In votes : " + str(self.writeIn_votes))

        return "\n"

    def print_values(self):
        state = "AL"
        county = self.get_county()
        trump_votes = self.trump_votes
        biden_votes = self.biden_votes
        jorgensen_votes = self.jorgensen_votes
        writein_votes = self.writeIn_votes
        print(f"('{state}','{county}','{trump_votes}','{biden_votes}','{jorgensen_votes}','{writein_votes}'),")

class table():
    row_object_lst = []

    def  add_row(self, row):
        self.row_object_lst.append(row)
        print(len(self.row_object_lst))

    def __str__(self):
        for row_object in self.row_object_lst:
            print(row_object)
        return "the end of the table __str__."

    def write_sql_values(self):
        for row_object in self.row_object_lst:
            row_object.print_values()

    def write_sql(self):
        print("USE test;")
        print("DROP TABLE IF EXISTS al;")
        print("CREATE TABLE al (")
        print("state varchar(2) NOT NULL,")
        print("county varchar(40) NOT NULL,")
        print("trump_votes int NOT NULL,")
        print("biden_votes int NOT NULL,")
        print("jorgensen_votes int NOT NULL,")
        print("writein_votes int NOT NULL,")
        print("PRIMARY KEY (state, county)")
        print(");")

        print("INSERT INTO al VALUES")
        self.write_sql_values()
        print(";")

        return True
