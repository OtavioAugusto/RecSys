# RecSys
Improved Cold-Start Recommendation via Two-Level Bandit Algorithms implements in Python the code based in paper published at BRACIS 2017 in follow link: 

https://github.com/OtavioAugusto/RecSys/blob/master/Improved%20Cold-Start%20Recommendation%20via%20Two-Level%20Bandit%20Algorithms.pdf

The user cold-start problem is recognized as an exploration/exploitation dilemma, for which the system needs to balance (i) maximizing the user satisfaction (exploitation) and (ii) learn about users’ tastes (exploration). We propose a new bandit algorithm that suggests items to users as a two-step process. First, we select the most relevant cluster to the target user, then, given the selected cluster, we choose an item from it that matches the user’s tastes. The experimental evaluation shows that our strategy yields significant improvements regarding recommendation quality over the state-of-the-art bandit algorithms.
