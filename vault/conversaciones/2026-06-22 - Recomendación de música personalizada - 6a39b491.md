---
titulo: "Recomendación de música personalizada"
fecha: 2026-06-22
mensajes: 8
origen: ChatGPT
---

# Recomendación de música personalizada

### Usuario

Quiero que te conectes a mi cuenta de Spotify, veas la música que está en mi biblioteca y me des una lista de reproducción basada en la información que puedas recopilar de mis listas de reproducción que seguramente me puedan gustar específicamente la lista de música https://open.spotify.com/playlist/2ziKlwg9C1MoIKNHByitUt?si=PnLLizO9Q4KYvIodijxf-w&pi=MJKCSqvOTNWR9
Que no estén en esa playlist pero que tengan relacion con géneros y años de esa música

### Asistente

No puedo conectarme a tu cuenta de Spotify ni ver el contenido privado de tu biblioteca. Tampoco puedo extraer de forma fiable el contenido completo de esa playlist a partir del enlace que me pasaste, porque Spotify restringe gran parte de esa información a usuarios autenticados.

La mejor forma de hacerlo es una de estas dos:

1. Me pasas una captura de pantalla de varias secciones de la playlist.
2. Me copias aquí entre 30 y 50 canciones de esa lista.
3. Me exportas la playlist a texto (por ejemplo desde Spotify o una web como Exportify) y me pegas el listado.

Dicho eso, conozco bastante bien tus gustos por conversaciones anteriores:

- Grunge estilo entity["musical_artist","Nirvana","Grunge band"]
- Heavy/Hard Rock estilo entity["musical_artist","Metallica","American heavy metal band"]
- Rock alternativo de los 90 y 2000
- Post-grunge
- Rock moderno melódico
- Algo de punk melódico y hard rock contemporáneo

Si tu playlist gira alrededor de esas influencias, estas canciones tienen muchas probabilidades de gustarte y no suelen aparecer en las listas más obvias:

- entity["song","Black Honey","Thrice song"] — entity["musical_artist","Thrice","American rock band"]
- entity["song","The Vengeful One","Disturbed song"] — entity["musical_artist","Disturbed","American heavy metal band"]
- entity["song","Pain","Three Days Grace song"]
- entity["song","The Sound of Winter","Bush song"]
- entity["song","I Am Machine","Three Days Grace song"]
- entity["song","45","Shinedown song"]
- entity["song","Not Strong Enough","Apocalyptica song featuring Brent Smith"]
- entity["song","Cut The Cord","Shinedown song"]
- entity["song","Enemy","Sevendust song"]
- entity["song","Broken","Seether song"]
- entity["song","Fine Again","Seether song"]
- entity["song","The Diary of Jane","Breaking Benjamin song"]
- entity["song","Polyamorous","Breaking Benjamin song"]
- entity["song","Still Remains","Stone Temple Pilots song"]
- entity["song","The Outsider","A Perfect Circle song"]
- entity["song","Remedy","Cold song"]
- entity["song","Bury Me Alive","We Are The Fallen song"]
- entity["song","World So Cold","Three Days Grace song"]
- entity["song","State of My Head","Shinedown song"]
- entity["song","Lowlife","Theory of a Deadman song"]

Y si quieres descubrir bandas posteriores a 2011 que encajan con tu perfil:

- entity["musical_artist","Badflower","American rock band"]
- entity["musical_artist","Dead Poet Society","American rock band"]
- entity["musical_artist","Royal Blood","British rock duo"]
- entity["musical_artist","Cleopatrick","Canadian rock duo"]
- entity["musical_artist","Nothing More","American rock band"]
- entity["musical_artist","Highly Suspect","American rock band"]
- entity["musical_artist","Rival Sons","American rock band"]
- entity["musical_artist","Mammoth WVH","Rock project by Wolfgang Van Halen"]

Si me pegas el listado de canciones de esa playlist, puedo hacer algo mucho más preciso: analizar década por década, géneros dominantes, artistas repetidos y darte 50 canciones que encajen exactamente con el ADN musical de esa lista y que no estén dentro de ella.

### Usuario

﻿Track URI,Track Name,Album Name,Artist Name(s),Release Date,Duration (ms),Popularity,Explicit,Added By,Added At,Genres,Record Label,Danceability,Energy,Key,Loudness,Mode,Speechiness,Acousticness,Instrumentalness,Liveness,Valence,Tempo,Time Signature
spotify:track:0JXXm3RqxU8EKzX4P8M0n3,"More And More - Single Version","Love Is Not Sex","Captain Hollywood Project",1993-03-05,253573,69,false,fenixhuman27,2017-04-11T16:56:27Z,"eurodance,happy hardcore","High Fashion Music",0.661,0.847,7,-11.855,1,0.0349,0.225,0.835,0.0863,0.71,125.862,4
spotify:track:5igLjt2pQ4Q2aiFIrBjuUR,"Only With You - Radio Mix","Love Is Not Sex","Captain Hollywood Project",1993-03-05,234093,58,false,fenixhuman27,2017-04-11T16:57:36Z,"eurodance,happy hardcore","High Fashion Music",0.642,0.984,8,-7.893,0,0.0425,0.0712,0.467,0.116,0.893,128.852,4
spotify:track:3N3t4yMGy1PCF7ZbizvZbK,"Mr. Vain - Radio Edit","Mr. Vain","Culture Beat",1993,257466,4,false,fenixhuman27,2017-04-11T17:00:21Z,"eurodance,europop","Abfahrt Media",0.703,0.997,9,-7.666,0,0.0399,0.0726,0.0235,0.123,0.391,132.872,4
spotify:track:2VvJgBu3yybNLZUxToyDzF,"Mr. Vain","Serenity","Culture Beat",1993,336840,0,false,fenixhuman27,2017-04-11T17:00:38Z,"eurodance,europop","Abfahrt Media",0.676,0.996,9,-7.946,0,0.0397,0.0478,0.262,0.333,0.4,132.871,4
spotify:track:2foOeJLKSvepjHEkb4NR8N,"Think About the Way","Ice 'n' Green","Ice Mc",1994-01-01,260973,18,false,fenixhuman27,2017-04-11T17:01:24Z,"eurodance","DWA Records",0.764,0.713,2,-8.9,0,0.0311,0.128,0.00058,0.145,0.67,132.993,4
spotify:track:2pjj239FG6qY3tj6hhjxeC,"It's a Rainy Day","Ice 'n' Green","Ice Mc",1994-01-01,255400,13,false,fenixhuman27,2017-04-11T17:01:38Z,"eurodance","DWA Records",0.621,0.729,2,-11.71,0,0.0306,0.00508,0.000834,0.335,0.467,134.966,4
spotify:track:5otExhdK6wDJB05JrXcLir,"Look Who's Talking - Long Version","Look Who's Talking","Dr. Alban",1994-02-18,324333,0,false,fenixhuman27,2023-02-27T21:56:29Z,"eurodance","BMG Rights Management GmbH",0.68,0.929,2,-9.851,1,0.0315,0.0000882,0.817,0.132,0.978,133.016,4
spotify:track:44o1MQVbm8S827avRs4RHc,"Feel the heat of the night - Radio Edit","Feel the heat of the night","Masterboy",2006-01-23,221840,64,false,fenixhuman27,2017-04-11T17:02:48Z,"eurodance","Klubbstyle Rec.",0.625,0.917,9,-6.893,0,0.0396,0.0136,0.00338,0.324,0.9,137.968,4
spotify:track:5Y3W09WHcXPx7eZ7s9gdMs,"Be My Lover","Greatest Hits","La Bouche",2007,240866,61,false,fenixhuman27,2017-04-11T17:03:38Z,"eurodance,europop","MCI",0.658,0.963,1,-3.283,0,0.0326,0.00283,0.00000238,0.951,0.793,134.798,4
spotify:track:2wz5weI4PREzpexKfrKgwv,"Sweet Dreams","Greatest Hits","La Bouche",2007,204586,69,false,fenixhuman27,2017-04-11T17:03:47Z,"eurodance,europop","MCI",0.656,0.956,11,-5.647,0,0.0536,0.0784,0.0247,0.0923,0.831,133.713,4
spotify:track:3tITGbn5bV6CwxQB0ybqoY,"U Got 2 Let The Music - Brescia Edit","Best Of Cappella","Cappella",2010-05-07,220093,0,false,fenixhuman27,2017-04-11T17:07:07Z,"eurodance,happy hardcore","ZYX Music",0.67,0.974,9,-4.411,0,0.0367,0.0893,0.208,0.0989,0.69,135.043,4
spotify:track:7pSJmBTlbA4S5zSLsj6Pzz,"No Limit","Unlimited Hits & Remixes","2 Unlimited",2014-05-05,223694,4,false,fenixhuman27,2017-04-11T17:38:55Z,"eurodance,hip house","Byte Records",0.652,0.999,3,-6.659,1,0.0522,0.0109,0.000646,0.0533,0.637,141.056,4
spotify:track:5ISKWtyWgg1y8yYrmxpvmS,"Get Ready - Steve Aoki Vocal Radio Edit","Get Ready (Steve Aoki Radio Mixes)","2 Unlimited",2013-11-04,175115,0,false,fenixhuman27,2017-04-11T17:39:02Z,"eurodance,hip house","Byte Records",0.712,0.86,4,-5.669,1,0.355,0.0507,0.0000449,0.0566,0.359,127.975,4
spotify:track:4cqiLvFRDuV8ClE61eMmZx,"Never Alone","Dreams","2 Brothers On The 4th Floor",1994-01-01,351026,61,false,fenixhuman27,2023-02-27T21:57:52Z,"happy hardcore,eurodance,gabber","CNR Entertainment BV",0.705,0.866,8,-5.036,0,0.0563,0.171,0.000162,0.645,0.816,127.986,4
spotify:track:5q10Ov2JEbODDK2tk4NYWW,"Tribal Dance","Unlimited Hits & Remixes","2 Unlimited",2014-05-05,218899,0,false,fenixhuman27,2017-04-11T17:39:32Z,"eurodance,hip house","Byte Records",0.653,0.982,5,-7.388,0,0.051,0.06,0.00481,0.097,0.76,130.074,4
spotify:track:0AUCQKbxc3k6mP74y0LvKZ,"The Real Thing","Unlimited Hits & Remixes","2 Unlimited",2014-05-05,219119,0,false,fenixhuman27,2017-04-11T17:39:46Z,"eurodance,hip house","Byte Records",0.592,0.981,2,-7.403,1,0.132,0.0291,0.000893,0.129,0.44,143.933,4
spotify:track:1q9NmfgguvcvcLjQrnoXzM,"No One","Unlimited Hits & Remixes","2 Unlimited",2014-05-05,206065,0,false,fenixhuman27,2017-04-11T17:39:55Z,"eurodance,hip house","Byte Records",0.795,0.816,1,-8.617,1,0.0396,0.0355,0.00136,0.0771,0.972,132.947,4
spotify:track:0ofMkI3jzmGCElAOgOLeo3,"The Rhythm of the Night","The Rhythm of the Night","Corona",1994,264280,25,false,fenixhuman27,2017-04-11T18:37:33Z,"eurodance","DWA Records",0.69,0.805,5,-11.522,0,0.0336,0.000232,0.739,0.095,0.799,127.808,4
spotify:track:4lDKORchTM8Rd0PFQFXTLX,"Baby Baby","The Rhythm of the Night","Corona",1994,228013,12,false,fenixhuman27,2017-04-11T18:37:44Z,"eurodance","DWA Records",0.639,0.869,7,-8.479,1,0.0311,0.00336,0.002,0.0576,0.562,133.033,4
spotify:track:2QbuqnxPaHCsYnlbAZDxvV,"Try Me Out","The Rhythm of the Night","Corona",1994,206880,4,false,fenixhuman27,2017-04-11T18:37:54Z,"eurodance","DWA Records",0.753,0.77,7,-8.655,0,0.035,0.0489,0.000397,0.251,0.558,130.977,4
spotify:track:69jRUfC6ZjhiY88OySXqoj,"Let the Dream Come True","Best Of","DJ BoBo",2014-05-02,241066,0,false,fenixhuman27,2017-04-11T18:39:22Z,"eurodance,europop","Yes Music AG",0.701,0.868,11,-7.585,0,0.0287,0.0337,0.114,0.291,0.716,141.981,4
spotify:track:3cOnQmSQuEUie603kZp82h,"Somebody Dance with Me","Best Of","DJ BoBo",2014-05-02,212893,0,false,fenixhuman27,2017-04-11T18:39:31Z,"eurodance,europop","Yes Music AG",0.682,0.988,6,-7.11,0,0.0388,0.101,0.00105,0.14,0.649,124.051,4
spotify:track:06j55Ok0s91zfw63w45L7f,"Everybody","Megamix","DJ BoBo",2014-09-12,228693,1,false,fenixhuman27,2017-04-11T18:39:38Z,"eurodance,europop","Yes Music AG",0.744,0.744,10,-10.706,0,0.0462,0.118,0.00279,0.336,0.7,100.029,4
spotify:track:0iBS7wbu5EbjxLa2tercQt,"Love Is All Around","There Is a Party","DJ BoBo",2005-03-01,269706,1,false,fenixhuman27,2017-04-11T18:40:30Z,"eurodance,europop","Yes Music AG",0.597,0.892,9,-5.79,0,0.0284,0.00346,0.0317,0.069,0.637,134.008,4
spotify:track:7vnPP2P7DJ9ebqWOWrtdHr,"There Is a Party","Best Of","DJ BoBo",2014-05-02,252693,0,false,fenixhuman27,2017-04-11T18:40:46Z,"eurodance,europop","Yes Music AG",0.672,0.875,10,-6.943,0,0.0412,0.242,0.000897,0.267,0.896,99.993,4
spotify:track:6rQ9qJPvInEqSzlh89LsPJ,"Coco Jamboo - Radio Version","We See The Same Sun","Mr. President",1996,218733,2,false,fenixhuman27,2017-04-11T18:42:30Z,"eurodance","First Class Dancefloor Music",0.832,0.838,1,-5.414,0,0.0421,0.0791,0,0.152,0.965,100.019,4
spotify:track:4G2HfoKgnzkfHmt3EqyJ6E,"The Summer Is Magic - Gambrinus Club Mix","Best Summer Hits - EP","Playahitty",2010-04-28,297000,26,false,fenixhuman27,2017-04-12T14:45:00Z,"eurodance","Conte Max Music",0.685,0.958,6,-6.512,0,0.0295,0.0606,0.163,0.125,0.889,133.821,4
spotify:track:0BQblMoALRAlYA7YykYGVl,"What Is Love - Single Mix","What Is Love (Single)","Haddaway",2009-12-22,271093,0,false,fenixhuman27,2017-04-13T17:04:01Z,"eurodance","Razor & Tie Label",0.687,0.768,7,-7.898,0,0.0314,0.024,0.00681,0.313,0.755,123.876,4
spotify:track:623rRTKwGmgjH6sjE9uWLh,"Scatman (ski-ba-bop-ba-dop-bop)","Scatman's World","Scatman John",1995-06-01,215973,75,false,fenixhuman27,2017-04-13T17:04:10Z,"eurodance","Iceberg Records",0.65,0.82,5,-10.9,0,0.0356,0.0662,0.00272,0.215,0.757,135.982,4
spotify:track:5hDPWrf12qJQ2pFGTbputX,"Ecuador - Original Radio Edit","The Best Of","Sash!",2016-09-30,212133,51,false,fenixhuman27,2017-04-13T17:04:22Z,"eurodance","High Fashion Music",0.591,0.888,4,-6.836,1,0.0354,0.00223,0.699,0.396,0.588,132.885,4
spotify:track:74jTexO94dFGyXGyeu8krd,"Beautiful Life","The Bridge","Ace of Base",1995-11-07,221186,72,false,fenixhuman27,2017-04-13T17:22:49Z,"eurodance,europop","Playground Music",0.749,0.988,0,-5.266,0,0.0387,0.202,0.00631,0.17,0.749,135.015,4
spotify:track:42MOQv8uspw7Jt6XSujAm7,"Life - Radio Edit","The Album","Haddaway",1993-09-13,257360,2,false,fenixhuman27,2017-04-13T17:24:30Z,"eurodance","Coconut Music",0.595,0.847,10,-8.495,1,0.0333,0.00601,0.445,0.215,0.596,128.479,4
spotify:track:12BbMJsJi65mxneq6c9Lm7,"All That She Wants","Happy Nation","Ace of Base",1992-11-16,211213,2,false,fenixhuman27,2017-04-13T17:24:39Z,"eurodance,europop","Playground Music",0.707,0.628,11,-9.684,1,0.0877,0.00526,0.0000821,0.104,0.87,187.548,4
spotify:track:0hrBpAOgrt8RXigk83LLNE,"The Sign","The Sign","Ace of Base",1993-12-24,191240,81,false,fenixhuman27,2017-04-13T17:27:02Z,"eurodance,europop","Playground Music",0.808,0.786,4,-6.897,0,0.0447,0.00928,0.0701,0.0574,0.899,96.987,4
spotify:track:12DVGoYMPBebItALnmaNdT,"Pump Up the Jam","Winners Greatest Hits Vol.2","Technotronic",2010-11-16,214575,1,false,fenixhuman27,2017-04-13T17:30:20Z,"eurodance,hip house,dance","Musart - Balboa",0.848,0.875,10,-8.866,0,0.0822,0.0164,0.00000169,0.046,0.673,124.821,4
spotify:track:3QRM0qZB7oMYavveH0iEqx,"Here Comes the Hotstepper - Heartical Mix","Here Comes The Hotstepper","iNi Kamoze;Salaam Remi",1994,250466,75,false,fenixhuman27,2017-04-13T21:04:58Z,"reggae,roots reggae","Columbia",0.889,0.453,4,-8.598,0,0.221,0.0141,0.000205,0.202,0.437,100.358,4
spotify:track:161UMtixaGd2orYqx03psi,"Big Time - Original","Whigfield 1","Whigfield",1995-05-04,201493,0,false,fenixhuman27,2017-04-13T23:35:45Z,"eurodance","X-Energy",0.787,0.744,11,-8.634,0,0.0343,0.0188,0.00531,0.293,0.974,95.803,4
spotify:track:2ahnofp2LbBWDXcJbMaSTu,"What Is Love - 7"" Mix","What Is Love (Remixes)","Haddaway",1993-03-22,270373,7,false,fenixhuman27,2017-04-17T17:15:36Z,"eurodance","Coconut Music",0.683,0.772,7,-7.907,0,0.0311,0.0222,0.0149,0.203,0.737,123.871,4
spotify:track:4t0UsYzmmmZRMTWn77jiGF,"Show Me Love","Show Me Love","Robin S",1993,252106,82,false,fenixhuman27,2017-04-17T17:27:08Z,"","Atlantic Records",0.811,0.833,5,-4.259,1,0.153,0.014,0.0000206,0.0769,0.567,120.258,4
spotify:track:1EQgbMBc304Ss86dXBulJA,"If You Had My Love","On The 6","Jennifer Lopez",1999-06-28,266000,0,false,fenixhuman27,2017-04-17T17:35:21Z,"","Work",0.68,0.625,11,-7,0,0.0353,0.0645,0.0000581,0.109,0.814,94.02,4
spotify:track:2AKEtttzKmCjcG2SMaZ62e,"Somebody Dance With Me (Album_Version)","Tuning Hitz 2","DJ BoBo",2007-12-06,211720,0,false,fenixhuman27,2017-04-21T18:12:03Z,"eurodance,europop","Tuning Hitz",0.685,0.978,6,-8.682,0,0.0396,0.105,0.000508,0.137,0.665,124.019,4
spotify:track:1gMZCGs6bxhyPeHAEiNc3i,"Everybody's Free (Single Version)","Everybody's Free","Rozalla",1992,212426,58,false,fenixhuman27,2017-04-21T18:16:34Z,"eurodance","Demon",0.579,0.972,9,-5.885,0,0.095,0.0119,0.000265,0.403,0.159,130.086,4
spotify:track:6PwbVXIomkvk4YcafiOc6i,"Bailando","Tarpeia","Paradisio",1997,229333,72,false,fenixhuman27,2017-04-26T17:51:15Z,"eurodance,europop","P.Samoy Recordings",0.647,0.94,6,-8.759,1,0.0394,0.0836,0.00962,0.119,0.835,132.824,4
spotify:track:0RVW7ifzZWqxfNWequ5CfJ,"Rhythm Is A Dancer - 12'' Version","Attack - The Remixes (Part 2)","SNAP!",2005,316133,0,false,fenixhuman27,2017-04-26T18:12:15Z,"eurodance","Luma Music",0.768,0.874,9,-7.303,0,0.034,0.119,0.0648,0.0842,0.838,124.251,4
spotify:track:5ojjL1ypuOtqqOpb4QiM1M,"I've Been Thinking About You","Fetenkult - Best Of The 90's","Londonbeat",2005-02-14,233200,0,false,fenixhuman27,2017-05-08T13:43:35Z,"eurodance","Ariola",0.644,0.887,11,-6.449,0,0.0372,0.0171,0.000602,0.0706,0.886,113.535,4
spotify:track:0KjvKAAnipAGwO9xiGSpdC,"I Need You More","Flash Maniac, Vol. 1","Pascal D Mann",2016-12-01,248424,0,false,fenixhuman27,2017-05-16T17:49:07Z,"eurodance","Da Crime Recordings",0.779,0.816,10,-7.492,0,0.0614,0.002,0.000529,0.0437,0.962,103.019,4
spotify:track:5jWQOxpciWcXm1eOWn8QNy,"Love & Devotion","Flash Maniac, Vol. 1","Real McCoy;Mc Sar",2016-12-01,271647,0,false,fenixhuman27,2017-05-16T18:01:49Z,"eurodance,europop,hip house","Da Crime Recordings",0.816,0.765,10,-10.19,0,0.116,0.0467,0.00113,0.284,0.6,101.968,4
spotify:track:1B75hgRqe7A4fwee3g3Wmu,"U Can't Touch This","Please Hammer Don't Hurt 'Em","MC Hammer",1990-02-20,257359,78,false,fenixhuman27,2017-05-19T18:27:33Z,"","EMI/EMI Records (USA)",0.867,0.517,11,-13.22,0,0.088,0.00449,0.000343,0.0864,0.862,133.149,4
spotify:track:6dHTkQYY3zdR9i9Nj0IGVW,"I Like To Move It (feat. The Mad Stuntman) - Erick ""More"" Album Mix","Move It!","Reel 2 Real;The Mad Stuntman;Erick Morillo",1994-10-10,230760,3,false,fenixhuman27,2023-02-27T22:55:54Z,"eurodance,soca","Strictly Rhythm Records",0.862,0.781,5,-8.546,0,0.0786,0.0392,0.00029,0.125,0.764,122.934,4
spotify:track:1gyaphIqlNbfhlQTUJ8iNr,"Saturday Night - Radio Edit","Best of [X-Mas Edition]","Whigfield",2013-12-17,223909,1,false,fenixhuman27,2017-05-31T17:10:34Z,"eurodance","X-Energy",0.735,0.868,11,-9.07,1,0.0387,0.0339,0.0264,0.234,0.965,129.963,4
spotify:track:7kTvXtMERxvwCGcWv68ssH,"Sweat (A La La La La Long)","Bad To The Bone","Inner Circle",1992-03-05,226546,1,false,fenixhuman27,2017-06-02T01:07:46Z,"reggae,roots reggae","WM Sweden",0.787,0.79,0,-6.649,1,0.21,0.0166,0,0.18,0.948,173.032,4
spotify:track:6HdM7gzXVgcpepv276raog,"It's My Life","One Love (2nd Edition)","Dr. Alban",1992-05-04,239933,8,false,fenixhuman27,2017-06-03T16:09:18Z,"eurodance","Ariola-Logic",0.655,0.933,7,-7.703,1,0.0536,0.00332,0.0365,0.0983,0.472,128.701,4
spotify:track:2aPbkXxYRTQ1cQrscHswuM,"Blue (Da Ba Dee) - Radio Edit","Europop","Eiffel 65",1999-11-30,210266,0,false,fenixhuman27,2017-06-03T16:10:30Z,"dance italiano,eurodance,europop","Universal Records",0.813,0.958,7,-9.186,0,0.0617,0.26,0.0000433,0.393,0.737,127.991,4
spotify:track:1IsvXZXAV9EBC4hBKW6yDN,"Missing - Todd Terry Remix / Radio Edit","Like The Deserts Miss The Rain","Everything But The Girl",2002-01-01,235026,64,false,fenixhuman27,2017-06-03T16:24:04Z,"","Virgin Records",0.739,0.853,9,-6.539,0,0.0296,0.0217,0.00357,0.057,0.652,123.509,4
spotify:track:1CgbwsrNDlFrRuk2ebQ7zr,"9Pm (Till I Come)","Movin' Melodies","ATB",1999-04-26,193880,75,false,fenixhuman27,2017-07-21T10:23:57Z,"trance","Kontor Records",0.672,0.941,9,-6.427,0,0.0494,0.0276,0.926,0.149,0.754,130.218,4
spotify:track:0v8xoqvW9klW45aM4zXfU5,"Come Back - Radio Edit","Flash Maniac, Vol. 1","Londonbeat",2016-12-01,233927,0,false,fenixhuman27,2017-07-27T13:34:58Z,"eurodance","Da Crime Recordings",0.698,0.748,7,-12.008,0,0.0433,0.266,0,0.133,0.818,120.47,4
spotify:track:0iQ2QFQmpwdjno9c0n5jrf,"Bob Marley","100 Trance, Dubstep, And Drum & Bass Workout Hits","Sun Is Shining (Extended Club mix)",2011-09-30,236280,32,false,fenixhuman27,2017-07-31T11:16:24Z,"","Hypnotic Records",0.685,0.896,0,-7.465,1,0.0971,0.00308,0.0637,0.103,0.885,130.061,4
spotify:track:5tnoDGu7ewh2NXOsK2BjLb,"Sun Is Shining","Sun Is Shining","Funkstar De Luxe",1999-09-13,234000,0,false,fenixhuman27,2017-07-31T11:17:57Z,"","Lifted House",0.706,0.961,4,-3.609,0,0.057,0.000946,0.0653,0.117,0.928,130.027,4
spotify:track:08uDST16GIe2K47v6O7VY9,"Change - Single Mix","100 hits från 90-talet","Lisa Stansfield",2014-08-22,336720,4,false,fenixhuman27,2017-07-31T11:18:17Z,"","RCA Records Label",0.658,0.889,0,-5.365,1,0.0527,0.267,0.0000629,0.324,0.707,105.85,4
spotify:track:70MxbDQ1qF5NimyVa4nIHy,"Shy Guy","Pure... R&B Party","Diana King",2013-08-02,243880,18,false,fenixhuman27,2017-07-31T11:30:02Z,"","Sony Music Entertainment",0.713,0.816,11,-5.754,0,0.0754,0.0172,0.000344,0.0475,0.779,94.045,4
spotify:track:4ACxa9buEUnOdYEoPcnMpi,"Your Woman","Women In Technology","White Town",1997-02-24,259893,2,false,fenixhuman27,2017-07-31T11:30:22Z,"","Echo",0.815,0.605,5,-9.118,0,0.0368,0.033,0.684,0.114,0.795,102.642,4
spotify:track:1IJqMwiZxMWrqyPtGq7muS,"Fat Boy","Nº1 Pop & Latino Vol. 2","Max a Million",2015-05-01,283200,0,false,fenixhuman27,2017-10-03T00:31:49Z,"","Dfm Music",0.818,0.924,5,-7.777,0,0.0467,0.00784,0.00164,0.121,0.942,126.964,4
spotify:track:7ozYx2bYrHZTA3MYNQXY4V,"Shine - Beatmasters 7"" Mix","Rise and Shine","Aswad",1994,219133,42,false,fenixhuman27,2018-02-17T00:06:52Z,"reggae,roots reggae,lovers rock,dub,reggae pop,ragga,rocksteady","Bubblin' Records",0.691,0.863,5,-6.842,0,0.0427,0.0697,0,0.0833,0.701,104.89,4
spotify:track:0gggjVyUJd90tYzAnmBjFV,"Another Night","Another Night","Real McCoy",1995-03-14,236933,71,false,fenixhuman27,2018-03-28T12:34:00Z,"eurodance,europop","Arista",0.813,0.882,7,-7.575,1,0.0402,0.0908,0.00457,0.147,0.874,125.983,4
spotify:track:7eheoW4hxrH51ww2QePVwF,"Gonna Make You Sweat (Everybody Dance Now) (feat. Freedom Williams)","Super Hits","C & C Music Factory;Freedom Williams",2000-02-28,244093,71,false,fenixhuman27,2018-03-28T12:34:10Z,"hip house","Columbia/Legacy",0.557,0.798,6,-7.405,1,0.0935,0.000851,0.665,0.183,0.793,112.117,4
spotify:track:2rVQyOpG4G2ECnQFOCsnmz,"Come Into My Life (Molella And Phil Jay Edit Mix)","Come Into My Life (The Album)","Gala;Molella;Phil Jay",1997-11-17,204460,54,false,fenixhuman27,2018-03-28T12:35:57Z,"eurodance,dance italiano","Do It Yourself",0.658,0.831,5,-6.527,0,0.0299,0.000431,0.0342,0.177,0.695,129.067,4
spotify:track:6kWJvPfC4DgUpRsXKNa9z9,"All That She Wants","The Sign","Ace of Base",1993-12-24,211213,84,false,fenixhuman27,2018-03-28T12:36:05Z,"eurodance,europop","Playground Music",0.798,0.625,11,-9.689,1,0.0548,0.00547,0.0000798,0.103,0.858,93.764,4
spotify:track:4Ypojjb7T5AW2IgkCAxmAO,"Moving on Up","One Night In Heaven: The Very Best Of M People","M People",2009-03-26,216040,44,false,fenixhuman27,2018-03-28T12:39:41Z,"","Legacy Recordings",0.895,0.862,0,-6.078,0,0.0365,0.0408,0.0399,0.102,0.964,125.078,4
spotify:track:5ICwDM1fzgqv7HNFUIjPyx,"Living in Danger","The Sign","Ace of Base",1993-12-24,223226,53,false,fenixhuman27,2018-03-28T12:45:36Z,"eurodance,europop","Playground Music",0.669,0.931,11,-7.161,0,0.0488,0.000573,0.56,0.106,0.829,102.079,4
spotify:track:08bZOAr9YLpCLL0Jmtsgbi,"Wheel of Fortune","The Sign","Ace of Base",1993-12-24,234106,57,false,fenixhuman27,2018-03-28T12:52:02Z,"eurodance,europop","Playground Music",0.785,0.79,10,-6.836,0,0.0555,0.0366,0.0223,0.0845,0.815,91.753,4
spotify:track:5OszlrLzTv7lf33uTGdrF2,"The Music's Got Me - Charismatic Mix","The Music's Got Me","Bass Bumpers",1992-01-01,388306,0,false,fenixhuman27,2018-04-14T13:29:01Z,"eurodance,hip house,house de Chicago,acid house","Brilliant Beats",0.869,0.932,10,-13.664,0,0.0446,0.00284,0.0413,0.121,0.582,128.971,4
spotify:track:3ChI7hyZWuHThzx72HRwuL,"The Music's Got Me - Dread Mix","The Music's Got Me","Bass Bumpers",1992-01-01,254560,0,false,fenixhuman27,2018-04-14T13:29:01Z,"eurodance,hip house,house de Chicago,acid house","Brilliant Beats",0.854,0.939,10,-11.186,0,0.0416,0.00518,0.00881,0.0801,0.913,129.002,4
spotify:track:1EtScazq8nGz0NewbbT4SG,"The Music's Got Me - Radio Version 1","The Music's Got Me","Bass Bumpers",1992-01-01,243266,0,false,fenixhuman27,2018-04-14T13:29:01Z,"eurodance,hip house,house de Chicago,acid house","Brilliant Beats",0.797,0.544,10,-11.194,0,0.0408,0.0286,0.00452,0.335,0.665,128.937,4
spotify:track:4uM7mVjab6WUJ4YIPz84M2,"The Music's Got Me - Radio Version 2","The Music's Got Me","Bass Bumpers",1992-01-01,252826,0,false,fenixhuman27,2018-04-14T13:29:01Z,"eurodance,hip house,house de Chicago,acid house","Brilliant Beats",0.848,0.504,10,-14.472,0,0.0563,0.0107,0.0114,0.0634,0.812,128.946,4
spotify:track:5ok6puNeaz2448yxEOLyB1,"The Reason Is You - Radio Mix","The Best","Nina",2017-01-03,235859,34,false,fenixhuman27,2018-04-14T13:42:02Z,"eurodance","Independent",0.735,0.881,2,-11.833,0,0.0366,0.248,0.513,0.179,0.953,127.347,4
spotify:track:4IiKITgHYaHrF1zUlcTyVH,"2 Times - Original","2 Times (Full Package)","Ann Lee",1998-12-15,230933,71,false,fenixhuman27,2018-04-17T14:13:46Z,"eurodance","X-Energy",0.849,0.875,0,-6.236,1,0.03,0.0947,0.0213,0.364,0.898,130.013,4
spotify:track:5FgtdSf7I5lClThz2ptWvl,"Blue (Da Ba Dee)","Europop","Eiffel 65",1999,283747,5,false,fenixhuman27,2018-04-17T14:21:48Z,"dance italian
Aqui tienes

### Asistente

Ahora sí puedo sacar conclusiones bastante sólidas.

Tu playlist tiene un ADN muy claro:

- Eurodance clásico 1992-1999 (aprox. 80% de la lista).
- BPM entre 124 y 136.
- Voces femeninas melódicas + rap masculino.
- Sonido alemán, italiano, holandés y escandinavo.
- Mucho sello DWA Records, X-Energy, Byte Records, Coconut y Ariola.
- Algunos cruces con reggae-pop noventero, house vocal y trance melódico.
- Te gustan tanto los grandes éxitos como los "deep cuts" (temas menos conocidos de los mismos artistas).

Por eso NO te voy a recomendar "What Is Love", "Blue" o "Rhythm Is A Dancer" porque ya los tienes o están demasiado cerca de lo obvio.

Estas son las canciones que tienen más probabilidades de gustarte y que no aparecen en el fragmento que enviaste:

1. Maxx – Get-A-Way
2. Maxx – No More (I Can't Stand It)
3. Maxx – You Can Get It
4. Magic Affair – Omen III
5. Magic Affair – Give Me All Your Love
6. Magic Affair – In The Middle Of The Night
7. Twenty 4 Seven – Slave To The Music
8. Twenty 4 Seven – Take Me Away
9. Twenty 4 Seven – Leave Them Alone
10. Fun Factory – Close To You
11. Fun Factory – Celebration
12. Fun Factory – I Wanna B With U
13. Fun Factory – Pain
14. Real McCoy – Run Away
15. Real McCoy – Come And Get Your Love
16. Real McCoy – Automatic Lover
17. E-Rotic – Max Don't Have Sex With Your Ex
18. E-Rotic – Fred Come To Bed
19. E-Rotic – Help Me Dr. Dick
20. E-Rotic – Willy Use A Billy... Boy

Segunda capa, para alguien que realmente conoce el género:

21. Activate – Save Me
22. Activate – Let The Rhythm Take Control
23. Intermission – Piece Of My Heart
24. Intermission – It's My Life
25. Netzwerk – Memories
26. Netzwerk – Passion
27. Masterboy – Generation Of Love
28. Masterboy – Anybody (Movin' On)
29. Masterboy – Is This The Love
30. Masterboy – Land Of Dreaming

Más trance/eurodance, porque veo que tienes ATB y Sash!:

31. Chicane – Offshore
32. Chicane feat. Máire Brennan – Saltwater
33. Alice Deejay – Better Off Alone
34. Fragma – Toca's Miracle
35. Darude – Sandstorm
36. Rank 1 – Airwave
37. Binary Finary – 1998
38. Faithless – Insomnia
39. DJ Quicksilver – Bellissima
40. DJ Quicksilver – Free

Y estas son las que creo que más te sorprenderían porque encajan perfecto con tu gusto y mucha gente no las conoce:

41. Centory – Point Of No Return
42. Sonic Dream Collective – Don't Go Breaking My Heart
43. Me & My – Dub-I-Dub
44. Solid Base – Mirror Mirror
45. Solid Base – You Never Know
46. Rednex – Wish You Were Here
47. Le Click – Tonight Is The Night
48. Le Click – Call Me
49. Captain Jack – Captain Jack
50. Captain Jack – Drill Instructor

Mis 10 apuestas más seguras para ti, viendo toda la lista que compartiste:

1. Get-A-Way — Maxx
2. Slave To The Music — Twenty 4 Seven
3. Close To You — Fun Factory
4. Generation Of Love — Masterboy
5. Better Off Alone — Alice Deejay
6. Toca's Miracle — Fragma
7. Omen III — Magic Affair
8. Run Away — Real McCoy
9. Mirror Mirror — Solid Base
10. Point Of No Return — Centory

Si quieres, también puedo construirte una playlist de 100 canciones manteniendo estrictamente el sonido eurodance 1992-1999, evitando cualquier tema que ya esté en tu biblioteca y priorizando rarezas europeas que casi nunca aparecen en playlists comerciales de Spotify. Esa sería probablemente la versión más ajustada a tu perfil musical.

### Usuario

Construye una playlist evitando cualquier tema que ya esté en mi biblioteca

### Asistente

Basándome en el fragmento de biblioteca que compartiste, veo que tu núcleo está formado por artistas como entity["musical_artist","Captain Hollywood Project","Eurodance alemán"], entity["musical_artist","Culture Beat","Eurodance alemán"], entity["musical_artist","2 Unlimited","Eurodance neerlandés"], entity["musical_artist","Masterboy","Eurodance alemán"], entity["musical_artist","Ace of Base","Europop sueco"], entity["musical_artist","DJ BoBo","Eurodance suizo"] y entity["musical_artist","Real McCoy","Eurodance alemán"].

Como no tengo tu biblioteca completa, no puedo garantizar al 100% que ninguna de estas canciones esté guardada en otra lista tuya, pero sí puedo excluir todo lo que aparece en el listado que me enviaste.

Playlist sugerida: "Eurodance Hidden Gems 1992-1999"

1. "Get-A-Way" – entity["musical_artist","Maxx","Eurodance alemán"]
2. "No More (I Can't Stand It)" – entity["musical_artist","Maxx","Eurodance alemán"]
3. "Omen III" – entity["musical_artist","Magic Affair","Eurodance alemán"]
4. "Give Me All Your Love" – entity["musical_artist","Magic Affair","Eurodance alemán"]
5. "Slave To The Music" – entity["musical_artist","Twenty 4 Seven","Eurodance neerlandés"]
6. "Take Me Away" – entity["musical_artist","Twenty 4 Seven","Eurodance neerlandés"]
7. "Close To You" – entity["musical_artist","Fun Factory","Eurodance alemán"]
8. "I Wanna B With U" – entity["musical_artist","Fun Factory","Eurodance alemán"]
9. "Celebration" – entity["musical_artist","Fun Factory","Eurodance alemán"]
10. "Run Away" – entity["musical_artist","Real McCoy","Eurodance alemán"]
11. "Come And Get Your Love" – entity["musical_artist","Real McCoy","Eurodance alemán"]
12. "Automatic Lover" – entity["musical_artist","Real McCoy","Eurodance alemán"]
13. "Generation Of Love" – entity["musical_artist","Masterboy","Eurodance alemán"]
14. "Land Of Dreaming" – entity["musical_artist","Masterboy","Eurodance alemán"]
15. "Anybody (Movin' On)" – entity["musical_artist","Masterboy","Eurodance alemán"]
16. "Feel The Fire" – entity["musical_artist","Masterboy","Eurodance alemán"]
17. "Max Don't Have Sex With Your Ex" – entity["musical_artist","E-Rotic","Eurodance alemán"]
18. "Fred Come To Bed" – entity["musical_artist","E-Rotic","Eurodance alemán"]
19. "Help Me Dr. Dick" – entity["musical_artist","E-Rotic","Eurodance alemán"]
20. "Willy Use A Billy... Boy" – entity["musical_artist","E-Rotic","Eurodance alemán"]
21. "Point Of No Return" – entity["musical_artist","Centory","Eurodance alemán"]
22. "Take It To The Limit" – entity["musical_artist","Centory","Eurodance alemán"]
23. "Mirror Mirror" – entity["musical_artist","Solid Base","Eurodance sueco"]
24. "You Never Know" – entity["musical_artist","Solid Base","Eurodance sueco"]
25. "This Is How We Do It" – entity["musical_artist","Solid Base","Eurodance sueco"]
26. "Dub-I-Dub" – entity["musical_artist","Me & My","Dance pop danés"]
27. "Baby Boy" – entity["musical_artist","Me & My","Dance pop danés"]
28. "Touch Me There" – entity["musical_artist","Total Touch","Dance neerlandés"]
29. "Tell Me Why" – entity["musical_artist","Prezioso","Eurodance italiano"]
30. "Stayin' Alive" – entity["musical_artist","N-Trance","Dance británico"]

Si tuviera que elegir solamente 10 temas que creo que tienen más probabilidades de convertirse en favoritos para vos, serían:

- Get-A-Way
- Omen III
- Slave To The Music
- Close To You
- Run Away
- Generation Of Love
- Land Of Dreaming
- Point Of No Return
- Mirror Mirror
- Dub-I-Dub

Además detecté algo interesante: tu biblioteca no es solamente eurodance. También aparecen pistas de reggae-pop noventero, house vocal y trance melódico. Eso me sugiere que probablemente disfrutarías una segunda playlist más especializada en la transición Eurodance → Trance (1998-2003), con artistas como entity["musical_artist","Alice Deejay","Dance neerlandés"], entity["musical_artist","Fragma","Trance alemán"], entity["musical_artist","Rank 1","Trance neerlandés"], entity["musical_artist","Chicane","Trance británico"] y entity["musical_artist","DJ Quicksilver","Trance alemán"]. Esa etapa suele gustarle mucho a quienes crecieron escuchando el eurodance clásico.

### Usuario

Mmmmm no me gustan esas canciones, prefiero rarezas más de américa en inglés que no estén en mi playlist

### Asistente

Eso cambia bastante el análisis.

Mirando tu lista con atención, hay una pista importante: aunque el grueso es eurodance europeo, también aparecen temas como:

- entity["song","Here Comes the Hotstepper","1994 single"]
- entity["song","If You Had My Love","1999 single"]
- entity["song","Show Me Love","1993 single"]
- entity["song","I've Been Thinking About You","1990 single"]
- entity["song","Moving On Up","1993 single"]
- entity["song","Gonna Make You Sweat","1990 single"]
- entity["song","U Can't Touch This","1990 single"]

Eso me dice que no te atrae únicamente el eurodance. También te gusta ese sonido angloparlante de radio FM de los 90: dance-pop, new jack swing, freestyle tardío, house vocal, R&B pop y crossover reggae.

Si buscas "joyas ocultas" americanas o angloparlantes que encajan con el ambiente de tu playlist pero que rara vez aparecen en recopilaciones comerciales, probaría con estas:

1. "Dreamboy/Dreamgirl" – entity["musical_artist","Cynthia","Freestyle singer"] & entity["musical_artist","Johnny O","Freestyle singer"]
2. "If Wishes Came True" – entity["musical_artist","Sweet Sensation","Freestyle group"]
3. "Because I Love You (The Postman Song)" – entity["musical_artist","Stevie B","Freestyle singer"]
4. "Together Forever" – entity["musical_artist","Lisette Melendez","Freestyle singer"]
5. "Can You Feel The Beat" – entity["musical_artist","Lisa Lisa & Cult Jam","American group"]
6. "Take Me In Your Arms" – entity["musical_artist","Lil Suzy","Freestyle singer"]
7. "Fascinated" – entity["musical_artist","Company B","Freestyle trio"]
8. "Spring Love" – entity["musical_artist","Stevie B","Freestyle singer"]
9. "Point Of No Return" – entity["musical_artist","Exposé","American girl group"]
10. "Come Go With Me" – entity["musical_artist","Exposé","American girl group"]

Más orientado a dance-pop/radio estadounidense de mediados de los 90:

11. "Tell Me" – entity["musical_artist","Groove Theory","R&B duo"]
12. "Every Little Thing I Do" – entity["musical_artist","Soul For Real","R&B group"]
13. "Back & Forth" – entity["musical_artist","Aaliyah","R&B singer"]
14. "100% Pure Love" – entity["musical_artist","Crystal Waters","House singer"]
15. "Gypsy Woman" – entity["musical_artist","Crystal Waters","House singer"]
16. "Finally" – entity["musical_artist","CeCe Peniston","House singer"]
17. "Strike It Up" – entity["musical_artist","Black Box","House group"]
18. "Runaway" – entity["musical_artist","Janet Jackson","Singer"]
19. "Groove Is In The Heart" – entity["musical_artist","Deee-Lite","Dance group"]
20. "Set Adrift On Memory Bliss" – entity["musical_artist","P.M. Dawn","Hip hop group"]

Y estas son mis apuestas más fuertes porque suelen gustar a gente que escucha exactamente la mezcla que veo en tu playlist:

- "100% Pure Love" – Crystal Waters
- "Finally" – CeCe Peniston
- "Set Adrift On Memory Bliss" – P.M. Dawn
- "Dreamboy/Dreamgirl" – Cynthia & Johnny O
- "Tell Me" – Groove Theory
- "Point Of No Return" – Exposé
- "Fascinated" – Company B
- "Spring Love" – Stevie B
- "Come Go With Me" – Exposé
- "Take Me In Your Arms" – Lil Suzy

De hecho, sospecho que tu gusto real no es "eurodance". Creo que tu gusto es más específico: música bailable angloparlante de 1988-1999 que sonaba en FM, discotecas y compilados de verano, con melodías muy memorables y sensación positiva. Si es así, puedo afinar mucho más y buscar rarezas casi olvidadas de EE.UU., Canadá y Australia que tuvieron un hit menor pero nunca llegaron a convertirse en clásicos mundiales. Ahí es donde suelen aparecer las mejores sorpresas.
