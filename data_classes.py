import path_dicts


class Row:
    state = None
    row_e = None
    county = None

    trump_percentage = None
    trump_votes = None


    biden_percentage = None
    biden_votes = None


    jorgensen_percentage = None
    jorgensen_votes = None


    west_percentage = None
    west_votes = None


    writein_percentage = None
    writein_votes = None

    other_percentage = None
    other_votes = None


    def set_row_state(self, state):
        self.state = state

    def set_row_e(self, e):
        self.row_e = e
        self.parse_row_e()

    def parse_row_e(self):
        ##set the xpaths
        #set the country

        path = path_dicts.county_xpath[self.state]
        self.county = self.row_e.xpath(path)[0].text
        #print(self.county)

        #set the trump data
        path = path_dicts.trump_percentage[self.state]
        self.trump_percentage = self.row_e.xpath(path)[0].text
        self.trump_percentage = float(self.trump_percentage.replace("%",""))


        #trump votes
        self.trump_votes = self.row_e.xpath(path_dicts.trump_votes[self.state])[0].text
        self.trump_votes = int(self.trump_votes.replace(",", ""))


        #set the biden data
        #biden precentage
        self.biden_percentage = self.row_e.xpath(path_dicts.biden_percentage[self.state])[0].text
        self.biden_percentage = float(self.biden_percentage.replace("%", ""))


        #biden votes
        self.biden_votes = self.row_e.xpath(path_dicts.biden_votes[self.state])[0].text
        self.biden_votes = int(self.biden_votes.replace(",", ""))


        # set the jorgensen data
        # jorgensen precentage
        self.jorgensen_percentage = self.row_e.xpath(path_dicts.jorgensen_percentage[self.state])[0].text
        self.jorgensen_percentage = float(self.jorgensen_percentage.replace("%", ""))

        #jorgensen votes
        self.jorgensen_votes = self.row_e.xpath(path_dicts.jorgensen_votes[self.state])[0].text
        self.jorgensen_votes = int(self.jorgensen_votes.replace(",", ""))

        # set the west data

        # west percentage
        self.west_percentage = self.row_e.xpath(path_dicts.west_percentage[self.state])[0].text
        self.west_percentage = float(self.west_percentage.replace("%", ""))

        # west votes
        self.west_votes = self.row_e.xpath(path_dicts.west_votes[self.state])[0].text
        self.west_votes = int(self.west_votes.replace(",", ""))

        # Other votes

        # other percentage

        self.other_percentage = self.row_e.xpath(path_dicts.other_percentage[self.state])[0].text
        self.other_percentage = float(self.other_percentage.replace("%", ""))

        # other votes
        self.other_votes = self.row_e.xpath(path_dicts.other_votes[self.state])[0].text
        self.other_votes = int(self.other_votes.replace(",", ""))

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
        label_width = 20
        c = self.get_county()
        print(f"{c}")

        label = "Trump Votes"
        value = str(self.trump_votes)
        print(f"{label:{label_width}} {value}")

        label = "Trump Percentage"
        value = str(self.trump_percentage)
        print(f"{label:{label_width}} {value}")

        label = "Biden Votes"
        value = str(self.biden_votes)
        print(f"{label:{label_width}} {value}")

        label = "Biden Percentage"
        value = str(self.biden_percentage)
        print(f"{label:{label_width}} {value}")

        label = "Jorgensen Votes"
        value = str(self.jorgensen_votes)
        print(f"{label:{label_width}} {value}")

        label = "Jorgensen Percentage"
        value = str(self.jorgensen_percentage)
        print(f"{label:{label_width}} {value}")

        label = "West Votes"
        value = str(self.west_votes)
        print(f"{label:{label_width}} {value}")

        label = "West Percentage"
        value = str(self.west_percentage)
        print(f"{label:{label_width}} {value}")

        label = "Write-In Votes"
        value = str(self.writein_votes)
        print(f"{label:{label_width}} {value}")

        label = "Write-In Percentage"
        value = str(self.writein_percentage)
        print(f"{label:{label_width}} {value}")

        label = "Other Votes"
        value = str(self.other_votes)
        print(f"{label:{label_width}} {value}")

        label = "Other Percentage"
        value = str(self.other_percentage)
        print(f"{label:{label_width}} {value}")

        return "\n"

    def print_values(self):
        state = "AL"
        county = self.get_county()
        trump_votes = self.trump_votes
        biden_votes = self.biden_votes
        print(f"('{state}','{county}','{trump_votes}','{biden_votes}'")


class Table:
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
