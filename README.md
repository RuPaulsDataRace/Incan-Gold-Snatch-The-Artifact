# Incan-Gold-Snatch-The-Artifact
This repository contains a MonteCarlo simulation of the press-your-luck board game, Incan Gold. Rules for Incan Gold can be found here: http://www.gvlibraries.org/sites/default/files/rules092906.pdf, and the BGG link is here: https://boardgamegeek.com/boardgame/15512/diamant

Insights from 10 million rounds of Incan Gold:
========
![alt text](https://raw.githubusercontent.com/rupaulsdatarace/incan-gold-snatch-the-artifact/master/incangoldmontecarlo.png)

This is a histogram of the number of rounds that ended at a certain card count. As there are always 15 treasure cards, at least 1 artifact card, and 5 different types of hazard cards in the deck, the maximum cards drawn per round is 21+(number of treasures). For this chart, I assumed 1 treasure in the deck. 

Interesting notes from this chart: 
-----------
+ 40% of rounds end between cards 5 and 8 (inclusive)
+ 70.6% of rounds end between cards 4 and 10 (inclusive)
+ 3.2% of rounds end on the 2nd card
+ 3.4% of rounds end after the 12th round
+ Less than 1% of rounds make it to the 16th round
