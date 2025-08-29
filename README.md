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
|hitster-de-aaaa0040.csv|Celebrations| X | X |

Unreleased versions are not added until physical copy available.
Results will after cleanup be submitted as pull requests to the repo here:
https://github.com/andygruber/songseeker-hitster-playlists

# Hitster Dublicates

These are the number of dublicates between the various hitster-de versions:
| vs. |0002|0007|0012|0015|0019|0025|0026|0039|0040|
|---|---|---|---|---|---|---|---|---|---|
|0002:| |1|8|3|2|0|0|11|26|
|0007:|1| |2|2|2|0|0|0|0|
|0012:|8|2| |3|5|0|1|2|23|
|0015:|3|2|3| |6|0|0|5|21|
|0019:|2|2|5|6| |0|0|3|6|
|0025:|0|0|0|0|0| |0|2|4|
|0026:|0|0|1|0|0|0| |0|0|
|0039:|11|0|2|5|3|2|0| |16|
|0040:|26|0|23|21|6|4|0|16| |

You can remove these cards if you want to play with mixted decks and without doublicates:

|Dublicates for hitster-de-aaaa*| List containing Card#/Card# Artist Title |
|---|---|
|7+2|#244/#280 Wencke Myhre Er hat ein knallrotes Gummiboot|
|7+7|#234/#14 Almklausi, Specktakel Mama Laudaaa|
|12+2|#4/#94 Creedence Clearwater Revival Have You Ever Seen The Rain; #55/#1 Rudi Carrell Wann wird's mal wieder richtig Sommer; #76/#147 Ritchie Valens La Bamba; #107/#117 Las Ketchup The Ketchup Song; #191/#187 Buddy Ab in den Süden; #258/#92 Kaoma Lambada; #260/#64 Thelma Houston Don't Leave Me This Way; #266/#285 Shakira Waka Waka|
|12+7|#42/#219 Edward Reekers So schmeckt der Sommer; #254/#82 Julian Sommer Dicht im Flieger|
|15+2|#114/#32 Siw Malmkvist Liebeskummer Lohnt Sich Nicht; #241/#201 Culture Beat Mr. Vain; #261/#111 Gitte Hænning Ich will 'nen Cowboy als Mann|
|15+7|#85/#290 Helene Fischer Herzbeben; #117/#282 Nik P., DJ Ötzi Ein Stern, der Deinen Namen trägt|
|15+12|#252/#237 Rick Astley Never Gonna Give You Up; #271/#277 David Guetta When Love Takes Over; #301/#85 Jonas Brothers Sucker|
|19+2|#88/#100 The Supremes You Can't Hurry Love; #226/#139 Die Ärzte Westerland|
|19+7|#170/#75 Clowns Ich liebe dich; #192/#279 Sabrina Setlur Du liebst mich nicht|
|19+12|#35/#77 Glass Animals Heat Waves; #47/#126 SNAP! Rhythm Is A Dancer; #92/#231 A Touch Of Class Around the World; #177/#130 Mariah Carey Without You; #188/#277 David Guetta When Love Takes Over|
|19+15|#106/#36 Billy Joel Uptown Girl; #128/#25 Shaggy Mr Boombastic; #144/#286 Ricchi E Poveri Sarà perché ti amo; #158/#97 Youssou N'Dour 7 Seconds; #188/#271 David Guetta When Love Takes Over; #204/#294 Robbie Williams Candy|
|26+12|#46/#64 Kenny Loggins Footloose|
|39+2|#3/#205 Prince Purple Rain; #11/#34 Lynyrd Skynyrd Sweet Home Alabama; #74/#302 Roy Orbison Oh' Pretty Woman; #76/#90 Bill Haley Rock Around The Clock; #147/#190 The Beach Boys Surfin' U.S.A.; #207/#119 The Monkees I'm a Believer; #240/#123 Steppenwolf Born To Be Wild; #245/#114 Elvis Presley Jailhouse Rock; #261/#74 Chuck Berry Johnny B. Goode; #275/#75 Billy Idol White Wedding; #286/#28 Journey Don't Stop Believin'|
|39+12|#25/#241 Third Eye Blind Semi; #45/#223 T. Rex Get It On|
|39+15|#54/#289 Joan Jett I Love Rock 'N Roll; #75/#265 Europe The Final Countdown; #114/#144 Ray Charles Hit the Road Jack; #128/#61 Eagles Hotel California; #185/#15 Meat Loaf I'd Do Anything For Love|
|39+19|#18/#105 Red Hot Chili Peppers Give It Away; #23/#225 Cream Sunshine Of Your Love; #288/#201 No Doubt Just A Girl|
|39+25|#73/#63 Survivor Eye of the Tiger; #297/#144 Queen Bohemian Rhapsody|
|40+2|#15/#99 Oasis Wonderwall; #18/#224 Nirvana Smells Like Teen Spirit; #23/#305 Aretha Franklin Respect; #29/#118 MIKA Relax, Take It Easy; #39/#68 Eddy Grant Gimme Hope Jo'Anna; #51/#210 Bill Haley See You Later, Alligator; #69/#7 Daft Punk One More Time; #79/#272 Rick James Super Freak; #84/#18 Whitney Houston I Wanna Dance with Somebody; #85/#268 Tones And I Dance Monkey; #87/#143 Aqua Barbie Girl; #105/#223 Little Eva The Locomotion; #120/#61 Neil Diamond Sweet Caroline; #127/#277 MadHouse Like a Prayer; #160/#34 Lynyrd Skynyrd Sweet Home Alabama; #168/#231 Snow Informer; #176/#155 The Trammps Disco Inferno; #186/#136 Reel 2 Real I Like To Move It; #188/#50 Outkast Hey Ya!; #189/#161 Carly Simon You're So Vain; #203/#290 Billie Eilish bad guy; #234/#86 O Dragostea din tei; #262/#44 No Doubt Don't Speak; #278/#207 Connie Francis Schöner fremder Mann; #286/#233 Kool Celebration; #303/#302 Roy Orbison Oh, Pretty Woman|
|40+12|#2/#140 SNAP! The Power; #17/#79 Miami Sound Machine Conga!; #45/#230 The Beatles Let It Be; #48/#201 Safri Duo Played; #49/#221 Crystal Waters Gypsy Woman; #53/#72 Daft Punk Get Lucky; #56/#153 Justin Timberlake SexyBack; #97/#186 Spice Girls Wannabe; #103/#142 Bob Sinclar Love Generation; #113/#88 Calvin Harris One Kiss; #121/#121 J Balvin Mi Gente; #130/#265 Salt Let's Talk About Sex; #167/#246 Alexandra Stan Mr. Saxobeat; #184/#65 Justin Timberlake CAN'T STOP THE FEELING!; #185/#165 Corona The Rhythm of the Night; #198/#198 Ed Sheeran Shape of You; #209/#89 Lou Bega Mambo No. 5; #228/#227 Don McLean American Pie; #247/#282 Miley Cyrus Flowers; #292/#177 Alvaro Soler Solo Para Ti; #298/#255 George McCrae Rock Your Baby; #306/#189 Boney M. Daddy Cool; #307/#223 T. Rex Get It On|
|40+15|#1/#279 Gloria Gaynor I Will Survive; #19/#156 BTS Dynamite; #30/#280 Village People YMCA; #35/#160 KC That's the Way; #80/#73 The Weather Girls It's Raining Men; #86/#86 Katy Perry I Kissed A Girl; #91/#3 Wham! Wake Me Up Before You GoGo; #115/#148 Harry Styles As It Was; #128/#245 The Ronettes Be My Baby; #140/#265 Europe The Final Countdown; #147/#90 Lesley Gore It's My Party; #148/#149 Peggy Gou Nanana; #172/#139 Rozalla Everybody's Free; #196/#58 Taylor Swift Shake It Off; #206/#21 Panic! At The Disco High Hopes; #216/#2 The B Love Shack; #219/#178 Britney Spears ...Baby One More Time; #258/#28 aha Take on Me; #265/#202 The Bangles Walk Like an Egyptian; #268/#138 OneRepublic I Ain't Worried; #269/#230 The 5th Dimension Aquarius/Let The Sunshine In|
|40+19|#43/#110 Michael Sembello Maniac; #166/#97 James Brown Get Up I Feel Like Being Like A Sex Machine, Pts. 1; #175/#127 Queen We Will Rock You; #215/#178 Black Eyed Peas Let's Get It Started; #229/#31 Avicii Waiting For Love; #291/#136 Olivia Rodrigo good 4 u|
|40+25|#74/#127 The Supremes Where Did Our Love Go; #93/#60 Michael Jackson Bad; #134/#121 Roxette How Do You Do!; #178/#104 Alcatraz Crying At the Discoteque|
|40+39|#34/#280 TOTO Hold the Line; #42/#172 Spin Doctors Two Princes; #46/#277 Foo Fighters The Pretender; #94/#119 Bachman You Ain't Seen Nothing Yet; #108/#30 The Knack My Sharona; #119/#255 Alice Cooper School's Out; #138/#149 Linkin Park The Emptiness Machine; #140/#75 Europe The Final Countdown; #142/#225 The Killers Mr. Brightside; #152/#188 The White Stripes Seven Nation Army; #155/#10 Blondie Call Me; #159/#281 Thin Lizzy The Boys Are Back In Town; #160/#11 Lynyrd Skynyrd Sweet Home Alabama; #302/#62 The Guess Who American Woman; #303/#74 Roy Orbison Oh' Pretty Woman; #307/#45 T. Rex Get It On|

The meaning of the "R" before a number: New editions (Rock, Celebrations) have a leading "R" before some card numbers in their right lower corner. This is Hitster's own indicator for dublications (when a newer version contains a card that was already in an edition before that; i.e. the card on the "newer" version has the "R"). However, this is somewhat flawed as they missed many dublicates. It does speed up the sorting/removing task but for example in Celebrations, these ids should also have an "R": 19,48,49,74,93,94,134,292. Also, the "R" does not stick to one language; the German Celebrations Edition has Card# 214 (Taio Cruz; Dynamite) marked with "R", but this song is only released in other languages (CZ, PL). Given that 91 [sic!] cards in Celebrations are dublicates, the 80 correct R's are still a great help.

# Hitster songs year distribution
Histograms showing song year distribution per German Hitster edition:
![Histogram distribution of decades covered by song cards per Hitster edition](/hitster-de-hist.png)
![Histogram distribution of decades covered by song cards for Hitster Rock edition](/hitster-de-aaaa0039_hist.png)
![Histogram distribution of decades covered by song cards for Hitster Celebrations edition](/hitster-de-aaaa0040_hist.png)
