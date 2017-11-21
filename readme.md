# Log Analysis

> Log Analysis python script finds the following stats for an internet webpage hits.

* `What are the most popular three articles of all time? Which articles have been accessed the most?`
##### Examples

```sh
	* "Princess Shellfish Marries Prince Handsome" — 1201 views
	* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
	* "Political Scandal Ends In Political Scandal" — 553 views
```
* `Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views?`
##### Examples

```sh
	* Ursula La Multa — 2304 views
	* Rudolf von Treppenwitz — 1985 views
	* Markoff Chaney — 1723 views
	* Anonymous Contributor — 1023 views
```
* `On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser`
##### Examples

```sh
	July 29, 2016 — 2.5% errors
```
**Run it**
```sh
python log_analysis.py
```

```sh
	"Candidate is jerk, alleges rival" - 338647 views 
	"Bears love berries, alleges bear" - 253801 views 
	"Bad things gone, say good people" - 170098 views
```
```sh
	Ursula La Multa - 507594views
	Rudolf von Treppenwitz - 423457views
	Anonymous Contributor - 170098views
	Markoff Chaney - 84557views
```
```sh
	July      17, 2016 -- 2.2626862468 %
```

