'''
Topic: Final Project - Soccer Premier League Analysis
Name: Ishwar Jadhav
Description:
    The project is based on a live website & we will consist of the latest data.
    The program helps us to analyze the current Soccer Premier League.
    The data is used to provide analysis based on Points, goals scored and conceded.
    The analysis is represented by plotting multiple graphs and generating pie chart
'''

##########    Importing Required Libraries      ###########
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import csv
from prettytable import from_csv
import pandas as pd

##########    URL for the dataset      ###########
url = 'https://www.premierleague.com/tables'

##########    Extraction of Classes after inspecting the url      ###########
PositionDes = "value"
TeamNameDes = "long"
TeamPointsDes = "points"
GoalsForDes = "hideSmall"
GoalsAgainstDes = "hideSmall"
GamesPlayedDes = "tableDark"

##########    Implementing BeautifulSoup      ###########
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")


##########    Position of each team on the table      ###########
teamPosition = [int(PositionDes.getText()) for PositionDes in soup.find_all(name="span", class_=PositionDes)][:10]

##########    Name of each teams      ###########
teamName = [(TeamNameDes.getText()) for TeamNameDes in soup.find_all(name="span", class_=TeamNameDes)][:10]

##########    Amount of Points scored by each team      ###########
teamPoints = [int(TeamPointsDes.getText()) for TeamPointsDes in soup.find_all(name="td", class_=TeamPointsDes)][:10]
addPoints = sum(teamPoints)

##########    Amount of goals scored by each team      ###########
goalsFor = [int(GoalsForDes.getText()) for GoalsForDes in soup.find_all(name="td", class_=GoalsForDes)[::2]][:10]
addGoalsFor = sum(goalsFor)

##########    Amount of goals Conceded by each team      ###########
goalsAgainst = [int(GoalsAgainstDes.getText()) for GoalsAgainstDes in soup.find_all(name="td", class_=GoalsAgainstDes)[1::2]][:10]
addGoalsAgainst = sum(goalsAgainst)


##########    Implementing the csv file using pandas      ###########
##########    Headers for csv columns      ###########
headers = ['Position', 'Name', 'Points', 'GF', 'GA']
with open("Graph.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    pd.DataFrame({'Position': teamPosition, 'Name': teamName, 'Points': teamPoints, 'GF': goalsFor, 'GA': goalsAgainst}).to_csv("Graph.csv", index=False)


##########    Initializing class      ###########
class Project():

    ##########    Graph for analysis of Points Scored by each team      ###########
    def Graph1(self):
        x = []
        y = []
        ##########    reading the csv file     ###########
        with open('Graph.csv', 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')

            for row in plots:
                x.append(row[1])
                y.append((row[2]))

        plt.bar(x, y, color='#003f5c', width=0.72, label="Points")
        ##########    lABEL for x-axis      ###########
        plt.xlabel('Team Names')
        ##########    lABEL for x-axis      ###########
        plt.ylabel('Points scored')
        ##########    lABEL for title      ###########
        plt.title('Points scored by each team')
        plt.legend()
        ##########    plotting the graph      ###########
        plt.show()


    ##########    Pie chart representation of Points vs Goals scored vs Goals conceded      ###########
    def PieChart(self):
        ##########  defining labels  ##########
        activities = ['Points Achieved', 'Goals Scored', 'Goals Conceded']

        ##########  portion covered by each label  ##########
        slices = [addPoints, addGoalsFor, addGoalsAgainst]

        ##########  color for each label  ##########
        colors = ['#9dc6e0', '#ff7c43', '#ffa600']

        ##########  plotting the pie chartl  ##########
        plt.pie(slices, labels=activities, colors=colors,
                startangle=90, shadow=True, explode=(0, 0.1, 0),
                radius=1.2, autopct='%1.1f%%')

        ##########  plotting legend  ##########
        plt.legend()
        plt.title('Record of Points, Goals Scored & Goals Conceded this season')
        ##########  showing the plot  ##########
        plt.show()


    ##########    Graph for analysis of Team names and Goal scored by them     ###########
    def Graph2(self):
        tick_label = [teamName]

        ##########  plotting a bar chart  ##########
        plt.bar(teamPosition, goalsFor, tick_label=teamName,
                width=0.8, color=['#bc5090', '#ff6361'])

        ##########  naming the x-axis  ##########
        plt.xlabel('Team Names')
        ##########  naming the y-axis  ##########
        plt.ylabel('Number of Goals Scored')
        ##########  plot title  ##########
        plt.title('Goals scored by each team!')
        ##########  function to show the plot  ##########
        plt.show()


    def Graph3(self):
        ##########  plotting a bar chart  ##########
        plt.bar(teamPosition, goalsAgainst, tick_label=teamName,
                width=0.8, color=['#bad0af', '#00c698'])

        ##########  naming the x-axis  ##########
        plt.xlabel('Team Names')
        ##########  naming the y-axis  ##########
        plt.ylabel('Number of Goals Conceded')
        ##########  plot title naming the y-axis  ##########
        plt.title('Goals Conceded by each team!')

        ##########  function to show the plot   ##########
        plt.show()


    def Table(self):
        with open("Graph.csv", "r") as fp:
            x = from_csv(fp)
        print(x)
        print("Here is my Analysis: ")

        line_number = 1
        with open("Graph.csv", 'r') as f:
            mycsv = csv.reader(f)
            mycsv = list(mycsv)
            text = mycsv[line_number][1]
            print("The team on top of the table is ----> ", text)

            text2 = mycsv[line_number][2]
            print(text + " is on Top of the table with ----> " + text2 + " points!")


            df = pd.read_csv('Graph.csv')
            ##########  FINDING MAX AND MIN   ##########
            maxGF = df['GF'].max()
            minGF = df['GF'].min()
            maxGA = df['GA'].max()
            minGA = df['GA'].min()

            ##########  FINAL ANALYSIS   ##########
            print("The maximum number of goals scored by a team this season is ----> ", maxGF)
            # print(minGF)
            print("The maximum number of goals conceded by a team this season is ----> ", maxGA)
            # print(minGA)
            print("The team at the bottom of the table is ----> ", df['Name'][9])

        print("Thank you for your time!")


##########  Main Function   ##########
def main():
    obj = Project()
    obj.Graph1()
    obj.PieChart()
    obj.Graph2()
    obj.Graph3()
    obj.Table()


if __name__ == '__main__':
    main()









