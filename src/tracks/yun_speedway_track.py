from src.tracks.track import Track
import src.configuration.personal_track_annotations as config


class YunSpeedwayTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Yun Speedway"
        self._ui_description = "Yun is the Chinese word for cloud. The Yun Speedway is a broad loop with constant cornering, void of any major straightaway."
        self._ui_length_in_m = 51  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "Albert"
        self._track_sector_dividers = [80, 160, 254]
        self._annotations = config.yun_speedway_annotations
        self._track_width = 1.066

        self._track_waypoints = [
            (-5.10302591323852, 6.096558332443237), (-4.952847003936768, 6.095563888549805),
            (-4.802656412124634, 6.0964930057525635), (-4.652460098266602, 6.099183559417725),
            (-4.502285003662113, 6.102705955505371), (-4.352135419845581, 6.106913089752197),
            (-4.202000856399536, 6.111515998840332), (-4.051855325698856, 6.115838050842285),
            (-3.9016965627670324, 6.119767427444458), (-3.751504421234127, 6.121960878372192),
            (-3.601273536682129, 6.121934413909912), (-3.4511164426803624, 6.117975950241089),
            (-3.301120519638065, 6.108806610107422), (-3.1518580913543737, 6.091949224472046),
            (-3.0038409233093226, 6.0654563903808585), (-2.8589090108871495, 6.026055574417115),
            (-2.7184704542160034, 5.9721410274505615), (-2.5855674743652344, 5.9020256996154785),
            (-2.461823582649231, 5.8166184425354), (-2.3487889766693115, 5.717378377914429),
            (-2.2461519241332977, 5.60766243934631), (-2.1535930037498474, 5.489165544509888),
            (-2.0687090158462524, 5.365126371383667), (-1.99076247215271, 5.2365562915802),
            (-1.9203495383262634, 5.1038055419921875), (-1.8587504625320435, 4.966822147369385),
            (-1.8110950589180004, 4.824383974075321), (-1.775075078010559, 4.678564548492432),
            (-1.7475225329399104, 4.530903577804563), (-1.7252659797668461, 4.382353067398075),
            (-1.7056599855422974, 4.2334303855896), (-1.686669945716858, 4.084429025650024),
            (-1.6668135523796082, 3.935539484024048), (-1.6450554728507996, 3.7869149446487427),
            (-1.6207115054130554, 3.6386945247650146), (-1.5934014916419983, 3.4909889698028564),
            (-1.5628705620765686, 3.3439090251922607), (-1.5288845300674438, 3.197601556777954),
            (-1.4917849898338318, 3.0520390272140503), (-1.4522612988948822, 2.9071184396743774),
            (-1.4102857410907745, 2.7628830671310425), (-1.3657850325107574, 2.6194114685058594),
            (-1.318587988615036, 2.4767860174179077), (-1.2676928639411926, 2.3354644775390625),
            (-1.2128665149211884, 2.1955695748329163), (-1.1530632674694061, 2.057778537273407),
            (-1.08787801861763, 1.9223674535751343), (-1.016120731830597, 1.7904059290885925),
            (-0.9372143298387527, 1.6624509692192078), (-0.8499562591314316, 1.5401909947395325),
            (-0.7538282573223114, 1.4245449900627136), (-0.648093119263649, 1.3178480863571167),
            (-0.5327586084604263, 1.221327155828476), (-0.4082227572798729, 1.1371697187423706),
            (-0.27564311027526855, 1.0663318634033203), (-0.1363035924732685, 1.0096842050552368),
            (0.007691953331232071, 0.9668328613042831), (0.15522770956158638, 0.9374588280916214),
            (0.3044206500053406, 0.9199007153511047), (0.4546559005975723, 0.9135304242372513),
            (0.6048972904682159, 0.9161626398563385), (0.7547982037067413, 0.9270666986703873),
            (0.9039529263973236, 0.9456496387720108), (1.0519982874393463, 0.9713789820671082),
            (1.1987109780311584, 1.0044596642255783), (1.3430854678153992, 1.0458043813705444),
            (1.4849849939346313, 1.0955103039741516), (1.6238089799880981, 1.153030276298523),
            (1.7592480182647705, 1.2180812656879425), (1.891234576702118, 1.2899702489376068),
            (2.019683539867401, 1.3678398728370667), (2.144827425479889, 1.4510299563407898),
            (2.2671289443969727, 1.5382285118103027), (2.386975407600403, 1.6288185715675354),
            (2.505310535430908, 1.7213334441184998), (2.6226320266723633, 1.81513249874115),
            (2.740172028541565, 1.9086654782295227), (2.8585100173950195, 2.001177966594696),
            (2.9789499044418335, 2.09096497297287), (3.1020665168762207, 2.1770519614219666),
            (3.2289494276046753, 2.2575360536575317), (3.359932541847229, 2.3311654925346375),
            (3.495507001876831, 2.3959739208221436), (3.6353999376296997, 2.4509690403938293),
            (3.77924907207489, 2.4949100017547607), (3.926172137260437, 2.526605486869812),
            (4.075098037719727, 2.544613003730774), (4.225324630737305, 2.553213953971863),
            (4.375569105148315, 2.560241937637329), (4.52576756477356, 2.566317558288574),
            (4.675350189208984, 2.5783075094223022), (4.8241260051727295, 2.5985214710235596),
            (4.971889972686768, 2.6267424821853638), (5.117899179458618, 2.6621850728988647),
            (5.262059450149536, 2.704761028289795), (5.403903961181641, 2.7541940212249756),
            (5.543262481689453, 2.8103535175323486), (5.680281639099121, 2.8719635009765625),
            (5.8150835037231445, 2.938239097595215), (5.948647499084473, 3.006983995437622),
            (6.0816731452941895, 3.0767370462417603), (6.216053009033203, 3.143920063972473),
            (6.353123426437378, 3.205357551574707), (6.494640588760376, 3.2562135457992554),
            (6.640975475311281, 3.2901740074157715), (6.790716648101807, 3.3034695386886597),
            (6.940881013870239, 3.2931236028671265), (7.087826967239382, 3.2620614767074576),
            (7.230064392089844, 3.2125210762023926), (7.3663530349731445, 3.1496520042419434),
            (7.49724507331848, 3.0755839347839364), (7.626259088516235, 2.9983465671539307),
            (7.753892183303835, 2.9190729856491076), (7.88043689727783, 2.8382065296173105),
            (8.007450103759766, 2.7580854892730713), (8.135154962539675, 2.6790513992309557),
            (8.263554096221924, 2.6011040210723877), (8.392229557037354, 2.5235899686813354),
            (8.520806312561035, 2.4459235668182373), (8.64928674697876, 2.368103504180908),
            (8.777350902557373, 2.2896125316619873), (8.904645442962646, 2.209862470626831),
            (9.031101703643799, 2.1287620663642883), (9.155682563781738, 2.0448439717292786),
            (9.278026580810547, 1.957601547241211), (9.396923065185547, 1.8657690286636353),
            (9.510931491851807, 1.7678430080413818), (9.618555068969727, 1.6629464626312256),
            (9.717334747314453, 1.549633502960205), (9.805655479431152, 1.4279944896697998),
            (9.881505012512207, 1.2981719970703125), (9.944759845733643, 1.1618003249168396),
            (9.99533462524414, 1.0202447474002838), (10.034976959228516, 0.8752070069313049),
            (10.065041542053223, 0.7280104458332062), (10.086772918701172, 0.5792213082313538),
            (10.10236644744873, 0.42983144521713257), (10.111979007720947, 0.27987760305404663),
            (10.117844104766846, 0.12972550466656685), (10.120851516723633, -0.02048181975260377),
            (10.120961666107178, -0.1707407459616661), (10.116987705230713, -0.32092465460300446),
            (10.108364582061768, -0.4709726423025131), (10.094699382781982, -0.6207800209522247),
            (10.07105016708374, -0.7690291106700897), (10.035926818847656, -0.9153132140636444),
            (9.988341808319092, -1.0579063296318054), (9.927549839019775, -1.1955289244651794),
            (9.85310173034668, -1.3260940313339233), (9.76466417312622, -1.447841465473175),
            (9.663427352905273, -1.5588630437850952), (9.550266742706299, -1.6580820083618164),
            (9.427704334259033, -1.7449080348014832), (9.296950340270996, -1.8193439841270447),
            (9.160552024841309, -1.8822464346885681), (9.019423007965088, -1.9341930747032166),
            (8.875330448150635, -1.9766254425048828), (8.728794574737549, -2.0101824402809143),
            (8.580870628356934, -2.036282956600189), (8.431797981262207, -2.0553815364837646),
            (8.282183170318604, -2.068683445453644), (8.132128238677979, -2.0764734745025635),
            (7.981942892074585, -2.0798590183258057), (7.8316919803619385, -2.079019546508789),
            (7.6815760135650635, -2.074038028717041), (7.531676530838013, -2.0649459958076477),
            (7.381824493408203, -2.0542485117912292), (7.231797695159912, -2.0452415347099304),
            (7.081636667251587, -2.0392410159111023), (6.931521415710449, -2.0420260429382324),
            (6.78164267539978, -2.0545049905776978), (6.633339166641235, -2.0784460306167603),
            (6.487406015396118, -2.114712953567505), (6.345907926559448, -2.1652730107307434),
            (6.210482597351074, -2.2303320169448853), (6.082667112350464, -2.3094435334205627),
            (5.963128566741943, -2.400428533554077), (5.850839376449585, -2.5001940727233887),
            (5.743854522705078, -2.6056629419326787), (5.63930869102478, -2.7135170698165894),
            (5.533867835998535, -2.8205130100250244), (5.424386024475098, -2.9233709573745728),
            (5.308670997619629, -3.0191615819931026), (5.185243129730225, -3.104874014854431),
            (5.0535500049591064, -3.177114963531494), (4.91707444190979, -3.2399849891662598),
            (4.777679681777954, -3.2960269451141357), (4.637065410614014, -3.3489339351654053),
            (4.495479583740234, -3.3991249799728394), (4.352414131164551, -3.444873571395874),
            (4.207801103591919, -3.485555410385132), (4.061668634414673, -3.5204038619995117),
            (3.9141465425491333, -3.54866361618042), (3.7654420137405396, -3.569946050643921),
            (3.6158945560455322, -3.5841740369796753), (3.4658855199813843, -3.591951012611389),
            (3.315700054168701, -3.5944758653640747), (3.1654945611953735, -3.5931135416030884),
            (3.01533305644989, -3.5893728733062744), (2.865199089050293, -3.5847009420394897),
            (2.7150609493255615, -3.5801475048065186), (2.564899444580078, -3.576403021812439),
            (2.414713501930237, -3.5741536617279053), (2.26450252532959, -3.573475956916809),
            (2.11429500579834, -3.5745739936828613), (2.11429500579834, -3.5745739936828613),
            (1.9641119837760925, -3.5771279335021973), (1.8139490485191345, -3.5807104110717773),
            (1.663789987564087, -3.584560990333557), (1.5136269927024841, -3.5882314443588257),
            (1.3634470105171204, -3.591033935546875), (1.2132434844970703, -3.5926220417022705),
            (1.0630374550819397, -3.5922939777374268), (0.9128403663635254, -3.589722990989685),
            (0.762735903263092, -3.5841771364212036), (0.6127667725086212, -3.5753254890441895),
            (0.463118240237236, -3.5623809099197388), (0.31388119608163834, -3.544994592666626),
            (0.16539417207241058, -3.522328495979309), (0.017816610634326935, -3.49402391910553),
            (-0.1283090861979872, -3.459241509437561), (-0.27273640036582947, -3.4176450967788696),
            (-0.4146588072180748, -3.368478536605835), (-0.5537574887275696, -3.3115040063858032),
            (-0.689168855547905, -3.246425986289978), (-0.8204654157161713, -3.173076033592224),
            (-0.9459429979324341, -3.090715527534485), (-1.0656676590442657, -2.999862551689148),
            (-1.1828364431858063, -2.9057165384292603), (-1.298326700925827, -2.809625029563904),
            (-1.416029453277588, -2.716394543647766), (-1.5374460220336914, -2.627887010574341),
            (-1.662642002105713, -2.5448285341262817), (-1.791678547859192, -2.4677690267562866),
            (-1.9251024723052979, -2.398792028427124), (-2.063152015209198, -2.3393019437789917),
            (-2.2056424617767334, -2.2916914224624634), (-2.3519099950790405, -2.2573130130767822),
            (-2.5009080171585083, -2.237378478050232), (-2.6510204076766968, -2.231777548789978),
            (-2.8010849952697754, -2.2393100261688232), (-2.950152039527893, -2.258348047733307),
            (-3.0977200269699097, -2.2863839268684387), (-3.243754506111145, -2.3217055201530457),
            (-3.3883389234542847, -2.3624584674835205), (-3.5317825078964233, -2.4070550203323364),
            (-3.674259066581726, -2.454639971256256), (-3.8161054849624634, -2.5040628910064697),
            (-3.9574440717697144, -2.5549100637435913), (-4.098620057106018, -2.6062129735946655),
            (-4.239762783050537, -2.657604455947876), (-4.3810319900512695, -2.7086429595947266),
            (-4.522681951522827, -2.75862193107605), (-4.664744853973389, -2.807438015937805),
            (-4.807544946670532, -2.854028582572937), (-4.9511754512786865, -2.8980824947357178),
            (-5.09595799446106, -2.938098430633545), (-5.242111444473267, -2.973046064376831),
            (-5.389806032180786, -3.0004465579986572), (-5.539110898971558, -3.018249988555908),
            (-5.689303398132324, -3.0217649936676025), (-5.838968276977539, -3.007417917251587),
            (-5.984735488891602, -2.969802498817444), (-6.12095046043396, -2.9066970348358154),
            (-6.243765592575073, -2.8197920322418213), (-6.350414037704468, -2.7135905027389526),
            (-6.442312479019165, -2.5947870016098022), (-6.52103590965271, -2.466552495956421),
            (-6.589886903762817, -2.3330190181732178), (-6.649887800216675, -2.1951465010643005),
            (-6.703099966049194, -2.054728925228119), (-6.750134706497192, -1.9120410084724426),
            (-6.795755863189697, -1.7688505053520203), (-6.841124534606934, -1.6255879998207092),
            (-6.886270999908447, -1.482264518737793), (-6.933759689331055, -1.339780032634735),
            (-6.985193967819214, -1.1986969709396362), (-7.040574550628662, -1.0590161681175232),
            (-7.100353956222534, -0.9210575819015503), (-7.166287183761597, -0.7860670685768127),
            (-7.238550424575806, -0.6541695445775986), (-7.31916356086731, -0.5273392051458359),
            (-7.410410165786743, -0.4078117273747921), (-7.51344108581543, -0.2984480895102024),
            (-7.629287481307983, -0.20258625596761703), (-7.755122900009155, -0.1206992119550705),
            (-7.886040687561035, -0.0468875914812088), (-8.015954971313477, 0.028446242213249207),
            (-8.13854193687439, 0.11542299389839172), (-8.248621225357056, 0.21773499995470047),
            (-8.345537185668945, 0.332563157659024), (-8.429625511169434, 0.45729828625917435),
            (-8.504193782806396, 0.5877808034420013), (-8.570229053497314, 0.7227745950222015),
            (-8.62991189956665, 0.8607748448848724), (-8.685093879699707, 1.0005055665969849),
            (-8.735774993896484, 1.1419672667980194), (-8.782512187957764, 1.2848089933395386),
            (-8.82592487335205, 1.4286454916000366), (-8.866011142730713, 1.5734755396842957),
            (-8.901474475860596, 1.7194624543190002), (-8.930729389190674, 1.866803526878357),
            (-8.953345775604248, 2.0154260396957397), (-8.967340469360352, 2.164985418319702),
            (-8.972111701965332, 2.315285563468933), (-8.965416431427002, 2.465335965156555),
            (-8.946499824523926, 2.614527463912964), (-8.914025783538818, 2.7612110376358032),
            (-8.868101119995117, 2.904336929321289), (-8.809147357940674, 3.0426135063171387),
            (-8.739034652709961, 3.1754549741744995), (-8.659126281738281, 3.3027645349502563),
            (-8.571917533874512, 3.42506206035614), (-8.478835105895996, 3.5430129766464233),
            (-8.381616830825806, 3.657523989677429), (-8.28150486946106, 3.7695236206054688),
            (-8.17940354347229, 3.8796950578689575), (-8.076259136199951, 3.9888938665390015),
            (-7.972629070281982, 4.097625017166138), (-7.868892669677734, 4.206258058547974),
            (-7.765360116958618, 4.3150975704193115), (-7.662764549255371, 4.424810409545898),
            (-7.5626771450042725, 4.536827087402344), (-7.465562582015991, 4.651458501815796),
            (-7.372910499572754, 4.7696614265441895), (-7.284466505050659, 4.891112804412842),
            (-7.1993279457092285, 5.014862537384033), (-7.11641263961792, 5.140115976333618),
            (-7.034520387649536, 5.266035079956055), (-6.951319932937622, 5.391108989715576),
            (-6.8643975257873535, 5.513610124588013), (-6.770937919616699, 5.631237506866455),
            (-6.667803525924683, 5.7405736446380615), (-6.5531439781188965, 5.837620496749878),
            (-6.427104949951172, 5.919373989105225), (-6.291306972503662, 5.984001636505127),
            (-6.148935556411747, 6.03202199935913), (-6.002481937408445, 6.065788507461548),
            (-5.8536660671234095, 6.087240934371948), (-5.703924417495731, 6.09880256652832),
            (-5.553712844848633, 6.101540565490723), (-5.403424978256226, 6.101013422012329),
            (-5.253200054168701, 6.099177598953247), (-5.10302591323852, 6.096558332443237)
        ]