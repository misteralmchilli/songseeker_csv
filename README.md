# songseeker_csv
Creating some missing songseeker csvs for the project https://github.com/andygruber/songseeker

Includes Python scripts to gather/crawl metadata for Hitster cards (including automatic Spotify, isrc and youtube searches).

See create_csv.py for usage. This is for experimentation only! This repo is not claiming any usage/owner rights to any of the original data/music/texts.
Do not misuse the Spotify API. Always interact with Youtube while preserving all usage rights. 
Support Jumbo Games and buy the card versions of Hitster.

Status (Automatic crawled results unless "Chk" is set; italics already exist by others in final repo):
|File|Edition|Chk URL|Chk Year|
|---|---|---|---|
|_hitster-de-aaaa0002_|_Original_|_X_|_X_|
|_hitster-de-aaaa0007_|_Schlager Party_|_X_|_X_|
|_hitster-de-aaaa0012_|_Summer Party_|_X_|_X_|
|_hitster-de-aaaa0015_|_Guilty Pleasures_|_X_|_X_|
|hitster-de-aaaa0019.csv|Bingo| X | X |
|hitster-de-aaaa0025.csv|Bayern 1 Expansion| X | X |
|_hitster-de-aaaa0026_|_Movies&TV Soundtracks_|_X_|_X_|
|hitster-de-aaaa0039.csv|Rock| X | X |

Unreleased versions are not added until physical copy available.
Results will after cleanup be submitted as pull requests to the repo here:
https://github.com/andygruber/songseeker-hitster-playlists

# Hitster Dublicates

These are the number of dublicates between the various hitster-de versions:
| vs. |0002|0007|0012|0015|0019|0025|0026|0039|
|---|---|---|---|---|---|---|---|---|
|0002:| |1|8|3|2|0|0|11|
|0007:|1| |2|1|2|0|0|0|
|0012:|8|2| |3|5|0|1|2|
|0015:|3|1|3| |6|0|0|5|
|0019:|2|2|5|6| |0|0|3|
|0025:|0|0|0|0|0| |0|2|
|0026:|0|0|1|0|0|0| |0|
|0039:|11|0|2|5|3|2|0| |

You can remove these cards if you want to play with mixted decks and without doublicates:

|Dublicates for hitster-de-aaaa*| List containing Card#/Card# Artist Title |
|---|---|
|2+7|#280/#244 Wencke Myhre Er hat ein knallrotes Gummiboot|
|2+12|#1/#55 Rudi Carrell Wann wird's mal wieder richtig Sommer; #64/#260 Thelma Houston Don't Leave Me This Way; #92/#258 Kaoma Lambada; #94/#4 Creedence Clearwater Revival Have You Ever Seen The Rain; #117/#107 Las Ketchup The Ketchup Song; #147/#76 Ritchie Valens La Bamba; #187/#191 Buddy Ab in den Süden; #285/#266 Shakira Waka Waka|
|2+15|#32/#114 Siw Malmkvist Liebeskummer Lohnt Sich Nicht; #111/#261 Gitte Hænning Ich will 'nen Cowboy als Mann; #201/#241 Culture Beat Mr. Vain|
|2+19|#100/#88 The Supremes You Can't Hurry Love; #139/#226 Die Ärzte Westerland|
|2+39|#28/#286 Journey Don't Stop Believin'; #34/#11 Lynyrd Skynyrd Sweet Home Alabama; #74/#261 Chuck Berry Johnny B. Goode; #75/#275 Billy Idol White Wedding; #90/#76 Bill Haley & His Comets Rock Around The Clock; #114/#245 Elvis Presley Jailhouse Rock; #119/#207 The Monkees I'm a Believer; #123/#240 Steppenwolf Born To Be Wild; #190/#147 The Beach Boys Surfin' U.S.A.; #205/#3 Prince Purple Rain; #302/#74 Roy Orbison Oh' Pretty Woman|
|7+7|#14/#234 Almklausi, Specktakel Mama Laudaaa|
|7+12|#82/#254 Julian Sommer Dicht im Flieger; #219/#42 Edward Reekers So schmeckt der Sommer|
|7+15|#290/#85 Helene Fischer Herzbeben|
|7+19|#75/#170 Clowns & Helden Ich liebe dich; #279/#192 Sabrina Setlur Du liebst mich nicht|
|12+15|#85/#301 Jonas Brothers Sucker; #237/#252 Rick Astley Never Gonna Give You Up; #277/#271 David Guetta When Love Takes Over|
|12+19|#77/#35 Glass Animals Heat Waves; #126/#47 SNAP! Rhythm Is A Dancer; #130/#177 Mariah Carey Without You; #231/#92 A Touch Of Class Around the World; #277/#188 David Guetta When Love Takes Over|
|12+26|#64/#46 Kenny Loggins Footloose|
|12+39|#223/#45 T. Rex Get It On; #241/#25 Third Eye Blind Semi|
|15+19|#25/#128 Shaggy Mr Boombastic; #36/#106 Billy Joel Uptown Girl; #97/#158 Youssou N'Dour 7 Seconds; #271/#188 David Guetta When Love Takes Over; #286/#144 Ricchi E Poveri Sarà perché ti amo; #294/#204 Robbie Williams Candy|
|15+39|#15/#185 Meat Loaf I'd Do Anything For Love; #61/#128 Eagles Hotel California; #144/#114 Ray Charles Hit the Road Jack; #265/#75 Europe The Final Countdown; #289/#54 Joan Jett & the Blackhearts I Love Rock 'N Roll|
|19+39|#105/#18 Red Hot Chili Peppers Give It Away; #201/#288 No Doubt Just A Girl; #225/#23 Cream Sunshine Of Your Love|
|25+39|#63/#73 Survivor Eye of the Tiger; #144/#297 Queen Bohemian Rhapsody|

# Hitster songs year distribution
Histograms showing song year distribution per German Hitster edition:
![Histogram distribution of decades covered by song cards per Hitster edition](/hitster-de-hist.png)
![Histogram distribution of decades covered by song cards for Hitster Rock edition](/hitster-de-aaaa0039_hist.png)
