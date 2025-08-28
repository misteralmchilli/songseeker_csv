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
|0007:|1| |2|1|2|0|0| 0| 0|
|0012:|8|2| |3|5|0|1| 2|21|
|0015:|3|1|3| |6|0|0| 5|21|
|0019:|2|2|5|6| |0|0| 3| 6|
|0025:|0|0|0|0|0| |0| 2 |4|
|0026:|0|0|1|0|0|0| | 0| 0|
|0039:|11|0|2|5|3|2|0| |16|
|0040:|26|0|21|21|6|4|0|16| |

You can remove these cards if you want to play with mixted decks and without doublicates:

|Dublicates for hitster-de-aaaa*| List containing Card#/Card# Artist Title |
|---|---|
|2+7|#280/#244 Wencke Myhre Er hat ein knallrotes Gummiboot|
|2+12|#1/#55 Rudi Carrell Wann wird's mal wieder richtig Sommer; #64/#260 Thelma Houston Don't Leave Me This Way; #92/#258 Kaoma Lambada; #94/#4 Creedence Clearwater Revival Have You Ever Seen The Rain; #117/#107 Las Ketchup The Ketchup Song; #147/#76 Ritchie Valens La Bamba; #187/#191 Buddy Ab in den Süden; #285/#266 Shakira Waka Waka|
|2+15|#32/#114 Siw Malmkvist Liebeskummer Lohnt Sich Nicht; #111/#261 Gitte Hænning Ich will 'nen Cowboy als Mann; #201/#241 Culture Beat Mr. Vain|
|2+19|#100/#88 The Supremes You Can't Hurry Love; #139/#226 Die Ärzte Westerland|
|2+39|#28/#286 Journey Don't Stop Believin'; #34/#11 Lynyrd Skynyrd Sweet Home Alabama; #74/#261 Chuck Berry Johnny B. Goode; #75/#275 Billy Idol White Wedding; #90/#76 Bill Haley & His Comets Rock Around The Clock; #114/#245 Elvis Presley Jailhouse Rock; #119/#207 The Monkees I'm a Believer; #123/#240 Steppenwolf Born To Be Wild; #190/#147 The Beach Boys Surfin' U.S.A.; #205/#3 Prince Purple Rain; #302/#74 Roy Orbison Oh' Pretty Woman|
|2+40|#7/#69 Daft Punk One More Time; #18/#84 Whitney Houston I Wanna Dance with Somebody; #34/#160 Lynyrd Skynyrd Sweet Home Alabama; #44/#262 No Doubt Don't Speak; #50/#188 Outkast Hey Ya!; #61/#120 Neil Diamond Sweet Caroline; #68/#39 Eddy Grant Gimme Hope Jo'Anna; #86/#234 O Dragostea din tei; #99/#15 Oasis Wonderwall; #118/#29 MIKA Relax, Take It Easy; #136/#186 Reel 2 Real I Like To Move It; #143/#87 Aqua Barbie Girl; #155/#176 The Trammps Disco Inferno; #161/#189 Carly Simon You're So Vain; #207/#278 Connie Francis Schöner fremder Mann; #210/#51 Bill Haley & His Comets See You Later, Alligator; #223/#105 Little Eva The Locomotion; #224/#18 Nirvana Smells Like Teen Spirit; #231/#168 Snow Informer; #233/#286 Kool & The Gang Celebration; #268/#85 Tones And I Dance Monkey; #272/#79 Rick James Super Freak; #277/#127 MadHouse Like a Prayer; #290/#203 Billie Eilish bad guy; #302/#303 Roy Orbison Oh, Pretty Woman; #305/#23 Aretha Franklin Respect|
|7+7|#14/#234 Almklausi, Specktakel Mama Laudaaa|
|7+12|#82/#254 Julian Sommer Dicht im Flieger; #219/#42 Edward Reekers So schmeckt der Sommer|
|7+15|#290/#85 Helene Fischer Herzbeben|
|7+19|#75/#170 Clowns & Helden Ich liebe dich; #279/#192 Sabrina Setlur Du liebst mich nicht|
|12+15|#85/#301 Jonas Brothers Sucker; #237/#252 Rick Astley Never Gonna Give You Up; #277/#271 David Guetta When Love Takes Over|
|12+19|#77/#35 Glass Animals Heat Waves; #126/#47 SNAP! Rhythm Is A Dancer; #130/#177 Mariah Carey Without You; #231/#92 A Touch Of Class Around the World; #277/#188 David Guetta When Love Takes Over|
|12+26|#64/#46 Kenny Loggins Footloose|
|12+39|#223/#45 T. Rex Get It On; #241/#25 Third Eye Blind Semi|
|12+40|#65/#184 Justin Timberlake CAN'T STOP THE FEELING!; #79/#17 Miami Sound Machine Conga!; #89/#209 Lou Bega Mambo No. 5; #121/#121 J Balvin Mi Gente; #140/#2 SNAP! The Power; #142/#103 Bob Sinclar Love Generation; #153/#56 Justin Timberlake SexyBack; #165/#185 Corona The Rhythm of the Night; #177/#292 Alvaro Soler Solo Para Ti; #186/#97 Spice Girls Wannabe; #189/#306 Boney M. Daddy Cool; #198/#198 Ed Sheeran Shape of You; #201/#48 Safri Duo Played; #221/#49 Crystal Waters Gypsy Woman; #223/#307 T. Rex Get It On; #227/#228 Don McLean American Pie; #230/#45 The Beatles Let It Be; #246/#167 Alexandra Stan Mr. Saxobeat; #255/#298 George McCrae Rock Your Baby; #265/#130 Salt Let's Talk About Sex; #282/#247 Miley Cyrus Flowers|
|15+19|#25/#128 Shaggy Mr Boombastic; #36/#106 Billy Joel Uptown Girl; #97/#158 Youssou N'Dour 7 Seconds; #271/#188 David Guetta When Love Takes Over; #286/#144 Ricchi E Poveri Sarà perché ti amo; #294/#204 Robbie Williams Candy|
|15+39|#15/#185 Meat Loaf I'd Do Anything For Love; #61/#128 Eagles Hotel California; #144/#114 Ray Charles Hit the Road Jack; #265/#75 Europe The Final Countdown; #289/#54 Joan Jett & the Blackhearts I Love Rock 'N Roll|
|15+40|#2/#216 The B Love Shack; #3/#91 Wham! Wake Me Up Before You GoGo; #21/#206 Panic! At The Disco High Hopes; #28/#258 aha Take on Me; #58/#196 Taylor Swift Shake It Off; #73/#80 The Weather Girls It's Raining Men; #86/#86 Katy Perry I Kissed A Girl; #90/#147 Lesley Gore It's My Party; #138/#268 OneRepublic I Ain't Worried; #139/#172 Rozalla Everybody's Free; #148/#115 Harry Styles As It Was; #149/#148 Peggy Gou Nanana; #156/#19 BTS Dynamite; #160/#35 KC & The Sunshine Band That's the Way; #178/#219 Britney Spears ...Baby One More Time; #202/#265 The Bangles Walk Like an Egyptian; #230/#269 The 5th Dimension Aquarius/Let The Sunshine In; #245/#128 The Ronettes Be My Baby; #265/#140 Europe The Final Countdown; #279/#1 Gloria Gaynor I Will Survive; #280/#30 Village People YMCA|
|19+39|#105/#18 Red Hot Chili Peppers Give It Away; #201/#288 No Doubt Just A Girl; #225/#23 Cream Sunshine Of Your Love|
|19+40|#31/#229 Avicii Waiting For Love; #97/#166 James Brown Get Up I Feel Like Being Like A Sex Machine, Pts. 1 & 2; #110/#43 Michael Sembello Maniac; #127/#175 Queen We Will Rock You; #136/#291 Olivia Rodrigo good 4 u; #178/#215 Black Eyed Peas Let's Get It Started|
|25+39|#63/#73 Survivor Eye of the Tiger; #144/#297 Queen Bohemian Rhapsody|
|25+40|#60/#93 Michael Jackson Bad; #104/#178 Alcatraz Crying At the Discoteque; #121/#134 Roxette How Do You Do!; #127/#74 The Supremes Where Did Our Love Go|
|39+40|#10/#155 Blondie Call Me; #11/#160 Lynyrd Skynyrd Sweet Home Alabama; #30/#108 The Knack My Sharona; #45/#307 T. Rex Get It On; #62/#302 The Guess Who American Woman; #74/#303 Roy Orbison Oh' Pretty Woman; #75/#140 Europe The Final Countdown; #119/#94 Bachman You Ain't Seen Nothing Yet; #149/#138 Linkin Park The Emptiness Machine; #172/#42 Spin Doctors Two Princes; #188/#152 The White Stripes Seven Nation Army; #225/#142 The Killers Mr. Brightside; #255/#119 Alice Cooper School's Out; #277/#46 Foo Fighters The Pretender; #280/#34 TOTO Hold the Line; #281/#159 Thin Lizzy The Boys Are Back In Town|

# Hitster songs year distribution
Histograms showing song year distribution per German Hitster edition:
![Histogram distribution of decades covered by song cards per Hitster edition](/hitster-de-hist.png)
![Histogram distribution of decades covered by song cards for Hitster Rock edition](/hitster-de-aaaa0039_hist.png)
![Histogram distribution of decades covered by song cards for Hitster Celebrations edition](/hitster-de-aaaa0040_hist.png)
