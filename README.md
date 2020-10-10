
# Election_Analysis
We are helping Colarado Board of Elections employee Tom, in an election audit of the tabulated results for the US Congrational Precint in Colorado. Historically the audits have been done in excell, however Colarado Board of Elections wants to automate the process. If it is done successfully the process could be used not only in other districts but also for other elections. <br>

The tasks we are asked to complete are:

    *Total number of votes cast
    *A complete list of candidates who received votes
    *Total number of votes each candidate received
    *Percentage of votes each candidate won
    *The winner of the election based on popular
    


# Process and Tools
Counts of votes casted by; mail ballots, puch cards, and  DRI counting machines determmine the final election results. Our job is to count the votes and certifiy the results of the race.</br>

We have recieved Election Results as "Election_Results.csv" file. The file has 3 colums as; Ballot ID, County and Candidate and 369,712 rows as votes. </br>. 
![](https://github.com/4renginy/Election_Analysis/blob/master/excel.PNG)

Historically the audits have been done in excell however Colarado Board of Elections wants to automate the process.If it is done successfully the process could be used not only in other districts but also for other elections. <br>

With the help of this file we have reached the following results;</br>

    ____________________________
	Total Vote Counts: 369,711
	____________________________
	
	**Largest county turnout was in Denver with 82.8%**
	
	
	Votes % and counts by County:
		*Jefferson : 10.5% (38,855)
		*Denver    : 82.8% (306,055
		*Arapahoe  : 6.7%  (24,801)

	Vote Counts for each Candidate:
		*Charles Casper Stockham: 23.0% (85,213)
		*Diana DeGette          : 73.8% (272,892)
		*Raymon Anthony Doane   : 3.1%  (11,606)
		
	Winner Info:
		*Winner: Diana DeGette
		*Winning Vote Count: 272,892
		*Winning Percentage: 73.8%
		
##Results and Applications

Total of 369,711 votes has been casted, Diana DeGette won the election by recieving 73.8% of the total votes. The biggest turnout was in Denver county.</br>

By pointing  different "file_to_load" and "file_to_save" files this process could be used for other elections. Some examples of we could modify the code for 

-party association of the candidate
	we could have used to calculate total votes for each party
-propositions or measures on the ballot
	we could have counted the "yes" or "no" votes for each proposition and calculate the total vote for each.
Those are only a few examples of how useful this process would be for the Election Board.
-
