#15-112 Term Project SkyGlow
#Name: Mia Tang
#Andrew ID: xinrant
#Recitation Section: B
#Mentor: Jonathan Perez


#This is a helper file to store all data related to constellations.
########################################


from tkinter import *
from PIL import Image, ImageTk

#Images from Etsy
def constellationImages(data):
    size = (150,150) 
    data.Capricorn = Image.open("Capricorn.jpg")
    data.Capricorn = data.Capricorn.resize(size, Image.ANTIALIAS)
    data.Capricorn = ImageTk.PhotoImage(data.Capricorn)

    data.Aries = Image.open("Aries.jpg")
    data.Aries = data.Aries.resize(size, Image.ANTIALIAS)
    data.Aries = ImageTk.PhotoImage(data.Aries)

    data.Gemini = Image.open("Gemini.jpg")
    data.Gemini = data.Gemini.resize(size, Image.ANTIALIAS)
    data.Gemini = ImageTk.PhotoImage(data.Gemini)

    data.Leo = Image.open("Leo.jpg")
    data.Leo = data.Leo.resize(size, Image.ANTIALIAS)
    data.Leo = ImageTk.PhotoImage(data.Leo)

    data.Libra = Image.open("Libra.jpg")
    data.Libra = data.Libra.resize(size, Image.ANTIALIAS)
    data.Libra = ImageTk.PhotoImage(data.Libra)

    data.Pisces = Image.open("Pisces.jpg")
    data.Pisces = data.Pisces.resize(size, Image.ANTIALIAS)
    data.Pisces = ImageTk.PhotoImage(data.Pisces)

    data.Sagittarius = Image.open("Sagittarius.jpg")
    data.Sagittarius = data.Sagittarius.resize(size, Image.ANTIALIAS)
    data.Sagittarius = ImageTk.PhotoImage(data.Sagittarius)

    data.Scorpio = Image.open("Scorpio.jpg")
    data.Scorpio = data.Scorpio.resize(size, Image.ANTIALIAS)
    data.Scorpio = ImageTk.PhotoImage(data.Scorpio)

    data.Virgo = Image.open("Virgo.jpg")
    data.Virgo = data.Virgo.resize(size, Image.ANTIALIAS)
    data.Virgo = ImageTk.PhotoImage(data.Virgo)

    data.Taurus = Image.open("Taurus.jpg")
    data.Taurus = data.Taurus.resize(size, Image.ANTIALIAS)
    data.Taurus = ImageTk.PhotoImage(data.Taurus)

    data.Aquarius = Image.open("Aquarius.jpg")
    data.Aquarius = data.Aquarius.resize(size, Image.ANTIALIAS)
    data.Aquarius = ImageTk.PhotoImage(data.Aquarius)

    data.Cancer = Image.open("Cancer.jpg")
    data.Cancer = data.Cancer.resize(size, Image.ANTIALIAS)
    data.Cancer = ImageTk.PhotoImage(data.Cancer)

    data.Libra = Image.open("Libra.jpg")
    data.Libra = data.Libra.resize(size, Image.ANTIALIAS)
    data.Libra = ImageTk.PhotoImage(data.Libra)

    data.Ophiuchus = Image.open("Ophiuchus.jpg")
    data.Ophiuchus = data.Ophiuchus.resize(size, Image.ANTIALIAS)
    data.Ophiuchus = ImageTk.PhotoImage(data.Ophiuchus)

#Text from Wikipedia
def constellationText(data):

    data.VirgoText = \
    "\t Virgo is the sixth astrological sign in the Zodiac. \n \
    It spans the 150-180th degree of the zodiac. Under the \n \
    tropical zodiac, the Sun transits this area on average \n \
    between August 23 and September 22, and the Sun transits \n \
    the constellation of Virgo from approximately September 16\n \
    to October 30." 

    data.TaurusText =  \
    "\tTaurus is the second astrological sign in the present\n \
    zodiac.It spans from 30° to 60° of the zodiac. This sign \n \
    belongs to the Earth element or triplicity, and has a \n \
    feminine or negative polarity, as well as a Fixed modality, \n \
    quality, or quadruplicity.It is a Venus-ruled sign, just like\n \
    Libra."
    
    data.ScorpioText = \
    "\tScorpio is the eighth astrological sign in the Zodiac, \n \
     originating from the constellation of Scorpius. It spans 210°\n\
     -240° ecliptic longitude. Under the tropical zodiac, the Sun \n\
     transits this sign on average from October 23 to November 22."

    data.PiscesText = \
    "\tPisces is the twelfth astrological sign in the Zodiac. It is\n\
     a negative mutable sign. It spans 330° to 360° of celestial \n\
     longitude. Under the tropical zodiac, the sun transits this area \n\
     between February 19 and March 20."
    
    data.SagittariusText = \
    '\tSagittarius is the ninth astrological sign, which is \n\
     associated with the constellation Sagittarius and spans\n\
     240–270th degrees of the zodiac. Under the tropical zodiac, \n\
     the sun transits this sign between approximately November 23 \n\
     and December 21. '
    
    data.LibraText = \
    "\tLibra is the seventh astrological sign in the Zodiac. \n\
     It spans 180°–210° celestial longitude. Under the tropical\n\
     zodiac, the Sun transits this area on average between \n\
     (northern autumnal equinox) September 23 and October 23, \n\
     and under the sidereal zodiac, the sun currently transits \n\
     the constellation of Libra from approximately October 31 \n\
     to November 22. "
    
    data.CapricornText = \
    "\tCapricorn is the tenth astrological sign in the zodiac \n\
     out of twelve total zodiac signs, originating from the \n\
     constellation of Capricornus, the horned goat. It spans the \n\
     270–300th degree of the zodiac, corresponding to celestial \n\
     longitude."

    data.CancerText = \
    "\tCancer is one of the twelve constellations of the zodiac.\n\
     Its name is Latin for crab and it is commonly represented\n\
     as one. Its astrological symbol is."

    data.AriesText =  \
    "\tAries is the first astrological sign in the zodiac, spanning\n\
     the first 30 degrees of celestial longitude, and originates from \n\
     the constellation of the same name. Under the tropical zodiac, \n\
     the Sun transits this sign from approximately March 20 to April \n\
     21 each year."

    data.AquariusText = \
    "\tAquarius is the eleventh astrological sign in the Zodiac, \n\
     originating from the constellation Aquarius. Under the tropical \n\
     zodiac, the Sun is in the Aquarius sign between about January 21 \n\
     and about February 20, while under the sidereal Zodiac, the sun \n\
     is in Aquarius from approximately ebruary 15 to March 14, \n\
     depending on the leap year."

    data.LeoText = \
    "\tLeo is one of the constellations of the zodiac, lying \n\
     between Cancer the crab to the west and Virgo the maiden to \n\
     the east. Its name is Latin for lion, and to the ancient Greeks \n\
     represented the Nemean Lion killed by the mythical Greek hero \n\
     Heracles meaning 'Glory of Hera' as one of his welve labors."

    data.GeminiText = \
    "\tGemini is one of the constellations of the zodiac. It was\n\
     one of the 8 constellations described by the 2nd century AD \n\
     astronomer Ptolemy, and it remains one of the 88 modern \n\
     constellations today. Its name is Latin for twins and it\n\
     is associated with the twins Castor and Pollux in Greek \n\
     mythology. Its symbol is"

    data.OphiuchusText = \
    "\tOphiuchus (/ɒfiˈjuːkəs/) has sometimes been used in \n\
     sidereal astrology as a thirteenth sign in addition to the \n\
     twelve signs of the tropical Zodiac, because the eponymous\n\
     constellation Ophiuchus (Greek: φίδι-φορέας Serpent-bearer),\n\
     as defined by the 1930 International Astronomical Union's \n\
     constellation boundaries, is situated behind the sun from \n\
     November 29 to December 18."

#Hand clicked points transformed by my own transform function
def constellationPoints(data):

     data.VirgoPoints = \
     [(-412.53484701295235, 0), (-368.2501032336555, -113.40132921796835), 
     (-293.97031760614493, -90.15238414230818), (-233.75479840851438, -48.16320401504456),
     (-157.6691047337337, -68.0621290620776), (-132.13671619427703, -156.47647821124136), 
     (-136.10971389827114, 20.955805461274302), (-91.58741442953479, 49.7267082975803), 
     (-256.213507211141, 120.19833078111608), (-319.67966089385754, 73.36834747210982), 
     (-332.00831636824057, 27.937033885620174), (0, 0)]

     data.TaurusPoints = \
     [(440.72894164100455, 0.0), (24.064677850539518, 79.44111832011023), 
     (93.52006665714565, -1.7312228172696291), (159.83747229693148, 20.22331450894387), 
     (218.42904085571723, 27.43636475284969), (239.56901856017475, 49.393171047368895), 
     (214.6239810070132, 70.26767946005639), (174.18415889404267, 84.74596621889972), 
     (290.46878456254626, -161.9317300431174), (314.79439376824445, -175.83369885230613),
     (333.7312032478411, 51.73474633887903), (0, 0)]

     data.ScorpioPoints = \
     [(485.9650193172344, 0.0), (93.81951002164051, -37.77432380995449), 
     (48.3141770841598, -29.098802255083424), (29.440390627500072, 74.31193309085833), 
     (75.99518181758616, 122.08903448103773), (123.13643497236349, 144.24083465612952),
     (165.326714488379, 111.60679852266172), (194.3473218148369, 66.144678572053),
     (340.21790340442425, -20.779273401586334), (364.54887277463183, -25.022377160159422),
     (482.4915182772386, -47.72771511946856), (444.89210417605165, 29.849885122144123), (0, 0)]

     data.PiscesPoints = \
     [(378.89312477267254, 0), (19.150519039777876, -44.46636504715789),
     (52.658648826026486, 30.414909235722195), (93.63590332045752, 102.26102683506528), 
     (115.08258437299813, 224.8866353833232), (141.7022281209584, 177.38511365262832), 
     (170.28548627983304, 160.4146288916344), (221.2444473630788, 103.29034084078651), 
     (247.18843884061693, 88.06177208947472), (302.26993448011035, 30.868863104912062), 
     (325.88609274470963, 6.946549905277735), (357.7948269220683, 29.459494697078355), 
     (370.3577363252302, -31.87706297718265), (324.30253273590773, -29.89761296618025),
     (0, 0)]

     data.SagittariusPoints = \
     [(426.2510997053263, 0.0), (23.87325219110243, 8.370652890905411), 
     (116.77623831213782, -23.39466105047891), (109.61379344780649, -51.7089575023672),
     (216.2528145117374, -14.653334629090574), (243.2181408368682, -38.03861153955728),
     (250.77471958171307, -73.92590898131179), (198.98834292424496, -178.54030183760497), 
     (320.6889087077983, -67.8426402183864), (353.9791454011693, -86.32939604247123), 
     (349.57563770043237, -137.8037500445328), (380.79901755611064, -9.904959782904347), 
     (261.2098832753081, 53.0508895241155), (211.85869095101265, 23.68322335585486), 
     (99.64079864981352, 88.55343722536873), (96.97570288634137, 157.3204152349594), 
     (220.8369669077097, 167.23945122788203), (362.4483317622031, 193.43527807201036), 
     (335.47362129706005, 127.00964299547005), (372.91868598084403, 124.389121897056), (0, 0)]

     data.LibraPoints = \
     [(-386.20331433067736, 0), (-206.10387598032395, -168.45531248935794), 
     (-62.650938254980254, -132.6606947658976), (-264.74915208121035, -61.097352416288416), 
     (-332.4518336216703, 11.822788232445106), (-132.7979281816487, 144.0510682732401), 
     (-141.3892578696146, 190.21587146996862), (0, 0)]

     data.CapricornPoints = \
     [(-484.62047005878736, 0), (-23.38531015544028, 63.74266443233968),
     (-56.188299261681706, 150.11953579091463), (-164.1160555812924, 304.601248028366), 
     (-213.61664724447576, 318.5544349401358), (-248.3118387165989, 297.6679874510892), 
     (-368.0405823104498, 194.34796055679365), (-375.11828581642, 146.1617995447191), 
     (-459.2707360731186, 75.0958786276307), (-443.5553454312909, 8.868795821766872), 
     (-345.3197096269986, 6.268823105287974), (-275.95821526849073, 21.565329253905173), (0, 0)]

     data.CancerPoints = \
     [(451.9214533522391, 0.0), (124.86019325136876, 58.09416615488036),\
     (231.2901926311751, 123.55908219404151), (295.53365747366166, 252.7209079206555), (0, 0)]

     data.AriesPoints = \
     [(423.46782640479313, 0.0), (53.16814784053487, -2.479527214415351), 
     (52.672242397651836, -137.33038586126165), (323.3657705771106, -94.46998686922485), 
     (395.909652507434, -52.92019511909336), (0, 0)]

     data.AquariusPoints = \
     [(483.125242561388, 0.0), (289.3287033791009, -217.24387540496565), 
     (251.88499643451624, -192.38489694147967), (213.7623765060828, -206.12046572446826), 
     (88.99348701395347, -133.06073526437953), (50.129858401929035, -56.355987229419945),
     (33.44060416786678, 80.45946801270843), (65.04731533667874, 106.74664757026648),
     (142.70005772103684, 108.17898837765469), (176.33315855810463, 30.192999071346417),
     (174.30055931987457, -94.19296693903895), (273.25833628580324, -158.6627922681146), 
     (351.0207810730393, -143.62942336051276), (248.2958649894134, 18.95160756133871), 
     (309.03994833395325, 129.9973474104279), (0, 0)]

     data.LeoPoints = \
     [(-548.0036496228835, 0), (-30.580088310602047, -53.8317582744218), 
     (-144.04283631016133, -49.8062376387142), (-204.76141003297863, 3.2810000466918243), 
     (-350.16555114560504, -46.14202846532305), (-413.5373918694734, -59.89011208700086), 
     (-465.54799438939114, 26.74069782214822), (-220.8269964685044, 162.80183546477338), 
     (-143.09758713096977, 81.41916578603904), (0, 0)]

     data.GeminiPoints = \
     [(444.94606414710535, 0.0), (20.168736669694592, -87.34541808903612), 
     (61.76478952045313, -41.19600436321614), (104.9250769067708, -51.10507055183697), 
     (228.0905668747452, -124.28472674772789), (157.36064579919827, -183.09185441646295), 
     (113.26766109641937, -201.7682753798195), (333.6876353420507, -211.6189075196982), 
     (332.77291773289477, -20.93287423016885), (377.81882692285336, 50.53646230830761), 
     (416.61678782422814, 10.929414578195347), (127.08057123369848, 63.96505620193641), 
     (189.25439909534666, 116.78943626484053), (277.2965308424623, 179.7543712479209), 
     (212.37405522651983, 199.22414679612282), (0, 0)]

     data.OphiuchusPoints = \
     [(-440.2238067165382, 0), (-258.42082655300936, -348.44321833500993),
     (-294.71600131689536, -232.22506016315236), (-336.183545146833, -172.0715664266101), 
     (-210.70418860769738, -179.81308323693213), (-113.32190408348912, -174.45671685232557), 
     (-105.37594580810587, -105.34187223059561), (-177.43474752671878, 9.894966908967817), 
     (-153.35154294249537, 61.55732512996316), (-93.28664050747986, 24.73060255691756), 
     (-55.3491193076011, 28.0084807134007), (-34.55742231086496, 3.9729791376916315), 
     (-37.50137940774794, -35.47740890364091), (-233.24726748845887, -10.42651471812721), 
     (-275.2463591275558, 20.18518731705428), (-311.3370924263807, -66.70243533400627), 
     (-301.5988639739598, -95.51505247664832), (-345.32889335057604, -115.95238426727799), 
     (-333.96194789316667, -138.9043460781621), (-397.6182053977593, -36.411024927420776), 
     (-390.742157456197, -9.826819753947351), (0, 0)]
