#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class ChampionshipCup2019ClockwiseTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "The 2019 DeepRacer Championship Cup (New - Clockwise)"
        self._ui_description = "This is the official track for the 2019 DeepRacer Championship Cup finals. Train your model on this track if you are taking part in the Knockouts, or plan to be at re:Invent 2019 where you will get the opportunity to race on the track for prizes and glory."
        self._ui_length_in_m = 60.0  # metres
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "reInvent2019_track_cw"
        self._track_sector_dividers = [29, 52]
        self._annotations = config.championship_cup_2019_cw_annotations
        self._track_width = 1.06

        self._track_waypoints = [(-4.012111513376725, -0.40334061411444255),
                                 (-3.9856139109139566, -0.10054636252347537), (-3.904826013803971, 0.19241211685117177),
                                 (-3.7561305449013833, 0.4570036170142501), (-3.5349625036721353, 0.6650119808572142),
                                 (-3.260567037821307, 0.7950744566577278), (-2.9618534729485635, 0.8520717558520644),
                                 (-2.657807438135638, 0.855320268596968), (-2.3590620443825863, 0.7997846243041368),
                                 (-2.0786230251793985, 0.6827715572970717), (-1.8079729363923212, 0.5438980546849586),
                                 (-1.5212179706101558, 0.44387570145305144), (-1.2187199876313333, 0.41543465974505833),
                                 (-0.9162235245709542, 0.44632933410581044), (-0.6191345587973718, 0.5122724709170668),
                                 (-0.3340441309516553, 0.618047097052893), (-0.1019417182211999, 0.8121987518924086),
                                 (0.04806278788994599, 1.0759808060782783), (0.15367822492073735, 1.361222767557463),
                                 (0.2612349181766387, 1.645713770117125), (0.4016107800747033, 1.9153768059867233),
                                 (0.5882448270316001, 2.155270778860411), (0.8176122918124076, 2.3547207948821396),
                                 (1.0875011100764151, 2.493890368666014), (1.3743740632529136, 2.5947306987899155),
                                 (1.669152529477584, 2.6693997022765488), (1.9703720524306174, 2.7105587360518784),
                                 (2.274047048329818, 2.727046334471068), (2.578112514256942, 2.7214412328856796),
                                 (2.8806585385794516, 2.690854274954161), (3.1780131175513144, 2.6276727554457993),
                                 (3.4633970572943564, 2.5232513782637924), (3.720715911626327, 2.362589323248228),
                                 (3.915525586843001, 2.1314178344863275), (4.012587578534591, 1.8445663091796236),
                                 (4.032012017011153, 1.5414487955230074), (4.003354580640304, 1.2388172981398902),
                                 (3.9450050904745932, 0.9403593179839461), (3.8644138886923667, 0.6471010980265944),
                                 (3.7656615092749472, 0.3594288912671416), (3.6529095485205527, 0.07693362357791356),
                                 (3.5285880877966758, -0.20066617307488033), (3.393314988851058, -0.4731002270174415),
                                 (3.2479540421957847, -0.7402899625641496), (3.0932485177512046, -1.002181685243288),
                                 (2.9297955348486777, -1.2587055328232437), (2.757463009595382, -1.5093502166611343),
                                 (2.575892479657638, -1.7533821823937084), (2.3844605996603843, -1.9897517326218277),
                                 (2.182750077485549, -2.217410719667116), (1.9705805494780417, -2.435349202428499),
                                 (1.7465280010695334, -2.641027248178163), (1.5087790205473777, -2.830655253205934),
                                 (1.255721600293624, -2.999265706811586), (0.9852393879885551, -3.1377532842499405),
                                 (0.6928400411600943, -3.219290292535463), (0.39016112828205785, -3.2455957296234756),
                                 (0.08795452540318927, -3.2154791715485245), (0.08795452540318927, -3.2154791715485245),
                                 (-0.20207108274523655, -3.125436222825685), (-0.4679920286541108, -2.97876480845038),
                                 (-0.6966214314704064, -2.7790077092987686), (-0.8834870890383844, -2.539244270597139),
                                 (-1.0876854941849832, -2.3145036461693436), (-1.3438299582009439, -2.1529271366936356),
                                 (-1.6397704765801553, -2.0889917376381546), (-1.9430784270768289, -2.102480149541536),
                                 (-2.2433834955697183, -2.1509007575852066), (-2.5435429499154214, -2.2001446845871597),
                                 (-2.8460819408898477, -2.230179167066255), (-3.14814695572902, -2.2056702735764175),
                                 (-3.4211729452614907, -2.0761356714111954), (-3.6287039206032876, -1.8556592228752762),
                                 (-3.775674907923234, -1.589855170522371), (-3.875955073595536, -1.3029445472103744),
                                 (-3.9472570106988076, -1.0073007705551773), (-3.9932919428353433, -0.7067331585032136),
                                 (-4.012111513376725, -0.40334061411444255)]