Data:
=====
Data retrieved from:
http://www.retrosheet.org/retroID.htm

For each player id, go to its pitcher matchup page and retrieve that information. Example:
if id is: aabb01
check if the link "http://www.retrosheet.org/boxesetc/A/MU0_aabb01.htm" exists
if it does, then the player has pitcher matchups
note that the capital letter A is due to the player id starting with small letter a
if id starts with another letter, A is replaced with that letter capitalized

Content of this folder:
=======================
playerinfo.txt includes ids of all players, not just the ones in the pitcher matchups

pitcherinfo/<player_id>_pitcher_matchup.txt is the pitcher matchups for player <player_id>