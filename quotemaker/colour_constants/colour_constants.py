"""Provide RGB colour constants and a colours dictionary with
elements formatted: colours[colourname] = CONSTANT
Graciously taken from: 
https://www.webucator.com/article/python-colour-constants-module/"""
from collections import namedtuple, OrderedDict

Colour = namedtuple("RGB", "red, green, blue")
colours = {}  # dict of colours


class RGB(Colour):
    def hex_format(self):
        """Returns colour in hex format"""
        return "#{:02X}{:02X}{:02X}".format(self.red, self.green, self.blue)


# Colour Contants
ALICEBLUE = RGB(240, 248, 255)
ANTIQUEWHITE = RGB(250, 235, 215)
ANTIQUEWHITE1 = RGB(255, 239, 219)
ANTIQUEWHITE2 = RGB(238, 223, 204)
ANTIQUEWHITE3 = RGB(205, 192, 176)
ANTIQUEWHITE4 = RGB(139, 131, 120)
AQUA = RGB(0, 255, 255)
AQUAMARINE1 = RGB(127, 255, 212)
AQUAMARINE2 = RGB(118, 238, 198)
AQUAMARINE3 = RGB(102, 205, 170)
AQUAMARINE4 = RGB(69, 139, 116)
AZURE1 = RGB(240, 255, 255)
AZURE2 = RGB(224, 238, 238)
AZURE3 = RGB(193, 205, 205)
AZURE4 = RGB(131, 139, 139)
BANANA = RGB(227, 207, 87)
BEIGE = RGB(245, 245, 220)
BISQUE1 = RGB(255, 228, 196)
BISQUE2 = RGB(238, 213, 183)
BISQUE3 = RGB(205, 183, 158)
BISQUE4 = RGB(139, 125, 107)
BLACK = RGB(0, 0, 0)
BLANCHEDALMOND = RGB(255, 235, 205)
BLUE = RGB(0, 0, 255)
BLUE2 = RGB(0, 0, 238)
BLUE3 = RGB(0, 0, 205)
BLUE4 = RGB(0, 0, 139)
BLUEVIOLET = RGB(138, 43, 226)
BRICK = RGB(156, 102, 31)
BROWN = RGB(165, 42, 42)
BROWN1 = RGB(255, 64, 64)
BROWN2 = RGB(238, 59, 59)
BROWN3 = RGB(205, 51, 51)
BROWN4 = RGB(139, 35, 35)
BURLYWOOD = RGB(222, 184, 135)
BURLYWOOD1 = RGB(255, 211, 155)
BURLYWOOD2 = RGB(238, 197, 145)
BURLYWOOD3 = RGB(205, 170, 125)
BURLYWOOD4 = RGB(139, 115, 85)
BURNTSIENNA = RGB(138, 54, 15)
BURNTUMBER = RGB(138, 51, 36)
CADETBLUE = RGB(95, 158, 160)
CADETBLUE1 = RGB(152, 245, 255)
CADETBLUE2 = RGB(142, 229, 238)
CADETBLUE3 = RGB(122, 197, 205)
CADETBLUE4 = RGB(83, 134, 139)
CADMIUMORANGE = RGB(255, 97, 3)
CADMIUMYELLOW = RGB(255, 153, 18)
CARROT = RGB(237, 145, 33)
CHARTREUSE1 = RGB(127, 255, 0)
CHARTREUSE2 = RGB(118, 238, 0)
CHARTREUSE3 = RGB(102, 205, 0)
CHARTREUSE4 = RGB(69, 139, 0)
CHOCOLATE = RGB(210, 105, 30)
CHOCOLATE1 = RGB(255, 127, 36)
CHOCOLATE2 = RGB(238, 118, 33)
CHOCOLATE3 = RGB(205, 102, 29)
CHOCOLATE4 = RGB(139, 69, 19)
COBALT = RGB(61, 89, 171)
COBALTGREEN = RGB(61, 145, 64)
COLDGREY = RGB(128, 138, 135)
CORAL = RGB(255, 127, 80)
CORAL1 = RGB(255, 114, 86)
CORAL2 = RGB(238, 106, 80)
CORAL3 = RGB(205, 91, 69)
CORAL4 = RGB(139, 62, 47)
CORNFLOWERBLUE = RGB(100, 149, 237)
CORNSILK1 = RGB(255, 248, 220)
CORNSILK2 = RGB(238, 232, 205)
CORNSILK3 = RGB(205, 200, 177)
CORNSILK4 = RGB(139, 136, 120)
CRIMSON = RGB(220, 20, 60)
CYAN2 = RGB(0, 238, 238)
CYAN3 = RGB(0, 205, 205)
CYAN4 = RGB(0, 139, 139)
DARKGOLDENROD = RGB(184, 134, 11)
DARKGOLDENROD1 = RGB(255, 185, 15)
DARKGOLDENROD2 = RGB(238, 173, 14)
DARKGOLDENROD3 = RGB(205, 149, 12)
DARKGOLDENROD4 = RGB(139, 101, 8)
DARKGRAY = RGB(169, 169, 169)
DARKGREEN = RGB(0, 100, 0)
DARKKHAKI = RGB(189, 183, 107)
DARKOLIVEGREEN = RGB(85, 107, 47)
DARKOLIVEGREEN1 = RGB(202, 255, 112)
DARKOLIVEGREEN2 = RGB(188, 238, 104)
DARKOLIVEGREEN3 = RGB(162, 205, 90)
DARKOLIVEGREEN4 = RGB(110, 139, 61)
DARKORANGE = RGB(255, 140, 0)
DARKORANGE1 = RGB(255, 127, 0)
DARKORANGE2 = RGB(238, 118, 0)
DARKORANGE3 = RGB(205, 102, 0)
DARKORANGE4 = RGB(139, 69, 0)
DARKORCHID = RGB(153, 50, 204)
DARKORCHID1 = RGB(191, 62, 255)
DARKORCHID2 = RGB(178, 58, 238)
DARKORCHID3 = RGB(154, 50, 205)
DARKORCHID4 = RGB(104, 34, 139)
DARKSALMON = RGB(233, 150, 122)
DARKSEAGREEN = RGB(143, 188, 143)
DARKSEAGREEN1 = RGB(193, 255, 193)
DARKSEAGREEN2 = RGB(180, 238, 180)
DARKSEAGREEN3 = RGB(155, 205, 155)
DARKSEAGREEN4 = RGB(105, 139, 105)
DARKSLATEBLUE = RGB(72, 61, 139)
DARKSLATEGRAY = RGB(47, 79, 79)
DARKSLATEGRAY1 = RGB(151, 255, 255)
DARKSLATEGRAY2 = RGB(141, 238, 238)
DARKSLATEGRAY3 = RGB(121, 205, 205)
DARKSLATEGRAY4 = RGB(82, 139, 139)
DARKTURQUOISE = RGB(0, 206, 209)
DARKVIOLET = RGB(148, 0, 211)
DEEPPINK1 = RGB(255, 20, 147)
DEEPPINK2 = RGB(238, 18, 137)
DEEPPINK3 = RGB(205, 16, 118)
DEEPPINK4 = RGB(139, 10, 80)
DEEPSKYBLUE1 = RGB(0, 191, 255)
DEEPSKYBLUE2 = RGB(0, 178, 238)
DEEPSKYBLUE3 = RGB(0, 154, 205)
DEEPSKYBLUE4 = RGB(0, 104, 139)
DIMGRAY = RGB(105, 105, 105)
DIMGRAY = RGB(105, 105, 105)
DODGERBLUE1 = RGB(30, 144, 255)
DODGERBLUE2 = RGB(28, 134, 238)
DODGERBLUE3 = RGB(24, 116, 205)
DODGERBLUE4 = RGB(16, 78, 139)
EGGSHELL = RGB(252, 230, 201)
EMERALDGREEN = RGB(0, 201, 87)
FIREBRICK = RGB(178, 34, 34)
FIREBRICK1 = RGB(255, 48, 48)
FIREBRICK2 = RGB(238, 44, 44)
FIREBRICK3 = RGB(205, 38, 38)
FIREBRICK4 = RGB(139, 26, 26)
FLESH = RGB(255, 125, 64)
FLORALWHITE = RGB(255, 250, 240)
FORESTGREEN = RGB(34, 139, 34)
GAINSBORO = RGB(220, 220, 220)
GHOSTWHITE = RGB(248, 248, 255)
GOLD1 = RGB(255, 215, 0)
GOLD2 = RGB(238, 201, 0)
GOLD3 = RGB(205, 173, 0)
GOLD4 = RGB(139, 117, 0)
GOLDENROD = RGB(218, 165, 32)
GOLDENROD1 = RGB(255, 193, 37)
GOLDENROD2 = RGB(238, 180, 34)
GOLDENROD3 = RGB(205, 155, 29)
GOLDENROD4 = RGB(139, 105, 20)
GRAY = RGB(128, 128, 128)
GRAY1 = RGB(3, 3, 3)
GRAY10 = RGB(26, 26, 26)
GRAY11 = RGB(28, 28, 28)
GRAY12 = RGB(31, 31, 31)
GRAY13 = RGB(33, 33, 33)
GRAY14 = RGB(36, 36, 36)
GRAY15 = RGB(38, 38, 38)
GRAY16 = RGB(41, 41, 41)
GRAY17 = RGB(43, 43, 43)
GRAY18 = RGB(46, 46, 46)
GRAY19 = RGB(48, 48, 48)
GRAY2 = RGB(5, 5, 5)
GRAY20 = RGB(51, 51, 51)
GRAY21 = RGB(54, 54, 54)
GRAY22 = RGB(56, 56, 56)
GRAY23 = RGB(59, 59, 59)
GRAY24 = RGB(61, 61, 61)
GRAY25 = RGB(64, 64, 64)
GRAY26 = RGB(66, 66, 66)
GRAY27 = RGB(69, 69, 69)
GRAY28 = RGB(71, 71, 71)
GRAY29 = RGB(74, 74, 74)
GRAY3 = RGB(8, 8, 8)
GRAY30 = RGB(77, 77, 77)
GRAY31 = RGB(79, 79, 79)
GRAY32 = RGB(82, 82, 82)
GRAY33 = RGB(84, 84, 84)
GRAY34 = RGB(87, 87, 87)
GRAY35 = RGB(89, 89, 89)
GRAY36 = RGB(92, 92, 92)
GRAY37 = RGB(94, 94, 94)
GRAY38 = RGB(97, 97, 97)
GRAY39 = RGB(99, 99, 99)
GRAY4 = RGB(10, 10, 10)
GRAY40 = RGB(102, 102, 102)
GRAY42 = RGB(107, 107, 107)
GRAY43 = RGB(110, 110, 110)
GRAY44 = RGB(112, 112, 112)
GRAY45 = RGB(115, 115, 115)
GRAY46 = RGB(117, 117, 117)
GRAY47 = RGB(120, 120, 120)
GRAY48 = RGB(122, 122, 122)
GRAY49 = RGB(125, 125, 125)
GRAY5 = RGB(13, 13, 13)
GRAY50 = RGB(127, 127, 127)
GRAY51 = RGB(130, 130, 130)
GRAY52 = RGB(133, 133, 133)
GRAY53 = RGB(135, 135, 135)
GRAY54 = RGB(138, 138, 138)
GRAY55 = RGB(140, 140, 140)
GRAY56 = RGB(143, 143, 143)
GRAY57 = RGB(145, 145, 145)
GRAY58 = RGB(148, 148, 148)
GRAY59 = RGB(150, 150, 150)
GRAY6 = RGB(15, 15, 15)
GRAY60 = RGB(153, 153, 153)
GRAY61 = RGB(156, 156, 156)
GRAY62 = RGB(158, 158, 158)
GRAY63 = RGB(161, 161, 161)
GRAY64 = RGB(163, 163, 163)
GRAY65 = RGB(166, 166, 166)
GRAY66 = RGB(168, 168, 168)
GRAY67 = RGB(171, 171, 171)
GRAY68 = RGB(173, 173, 173)
GRAY69 = RGB(176, 176, 176)
GRAY7 = RGB(18, 18, 18)
GRAY70 = RGB(179, 179, 179)
GRAY71 = RGB(181, 181, 181)
GRAY72 = RGB(184, 184, 184)
GRAY73 = RGB(186, 186, 186)
GRAY74 = RGB(189, 189, 189)
GRAY75 = RGB(191, 191, 191)
GRAY76 = RGB(194, 194, 194)
GRAY77 = RGB(196, 196, 196)
GRAY78 = RGB(199, 199, 199)
GRAY79 = RGB(201, 201, 201)
GRAY8 = RGB(20, 20, 20)
GRAY80 = RGB(204, 204, 204)
GRAY81 = RGB(207, 207, 207)
GRAY82 = RGB(209, 209, 209)
GRAY83 = RGB(212, 212, 212)
GRAY84 = RGB(214, 214, 214)
GRAY85 = RGB(217, 217, 217)
GRAY86 = RGB(219, 219, 219)
GRAY87 = RGB(222, 222, 222)
GRAY88 = RGB(224, 224, 224)
GRAY89 = RGB(227, 227, 227)
GRAY9 = RGB(23, 23, 23)
GRAY90 = RGB(229, 229, 229)
GRAY91 = RGB(232, 232, 232)
GRAY92 = RGB(235, 235, 235)
GRAY93 = RGB(237, 237, 237)
GRAY94 = RGB(240, 240, 240)
GRAY95 = RGB(242, 242, 242)
GRAY97 = RGB(247, 247, 247)
GRAY98 = RGB(250, 250, 250)
GRAY99 = RGB(252, 252, 252)
GREEN = RGB(0, 128, 0)
GREEN1 = RGB(0, 255, 0)
GREEN2 = RGB(0, 238, 0)
GREEN3 = RGB(0, 205, 0)
GREEN4 = RGB(0, 139, 0)
GREENYELLOW = RGB(173, 255, 47)
HONEYDEW1 = RGB(240, 255, 240)
HONEYDEW2 = RGB(224, 238, 224)
HONEYDEW3 = RGB(193, 205, 193)
HONEYDEW4 = RGB(131, 139, 131)
HOTPINK = RGB(255, 105, 180)
HOTPINK1 = RGB(255, 110, 180)
HOTPINK2 = RGB(238, 106, 167)
HOTPINK3 = RGB(205, 96, 144)
HOTPINK4 = RGB(139, 58, 98)
INDIANRED = RGB(176, 23, 31)
INDIANRED = RGB(205, 92, 92)
INDIANRED1 = RGB(255, 106, 106)
INDIANRED2 = RGB(238, 99, 99)
INDIANRED3 = RGB(205, 85, 85)
INDIANRED4 = RGB(139, 58, 58)
INDIGO = RGB(75, 0, 130)
IVORY1 = RGB(255, 255, 240)
IVORY2 = RGB(238, 238, 224)
IVORY3 = RGB(205, 205, 193)
IVORY4 = RGB(139, 139, 131)
IVORYBLACK = RGB(41, 36, 33)
KHAKI = RGB(240, 230, 140)
KHAKI1 = RGB(255, 246, 143)
KHAKI2 = RGB(238, 230, 133)
KHAKI3 = RGB(205, 198, 115)
KHAKI4 = RGB(139, 134, 78)
LAVENDER = RGB(230, 230, 250)
LAVENDERBLUSH1 = RGB(255, 240, 245)
LAVENDERBLUSH2 = RGB(238, 224, 229)
LAVENDERBLUSH3 = RGB(205, 193, 197)
LAVENDERBLUSH4 = RGB(139, 131, 134)
LAWNGREEN = RGB(124, 252, 0)
LEMONCHIFFON1 = RGB(255, 250, 205)
LEMONCHIFFON2 = RGB(238, 233, 191)
LEMONCHIFFON3 = RGB(205, 201, 165)
LEMONCHIFFON4 = RGB(139, 137, 112)
LIGHTBLUE = RGB(173, 216, 230)
LIGHTBLUE1 = RGB(191, 239, 255)
LIGHTBLUE2 = RGB(178, 223, 238)
LIGHTBLUE3 = RGB(154, 192, 205)
LIGHTBLUE4 = RGB(104, 131, 139)
LIGHTCORAL = RGB(240, 128, 128)
LIGHTCYAN1 = RGB(224, 255, 255)
LIGHTCYAN2 = RGB(209, 238, 238)
LIGHTCYAN3 = RGB(180, 205, 205)
LIGHTCYAN4 = RGB(122, 139, 139)
LIGHTGOLDENROD1 = RGB(255, 236, 139)
LIGHTGOLDENROD2 = RGB(238, 220, 130)
LIGHTGOLDENROD3 = RGB(205, 190, 112)
LIGHTGOLDENROD4 = RGB(139, 129, 76)
LIGHTGOLDENRODYELLOW = RGB(250, 250, 210)
LIGHTGREY = RGB(211, 211, 211)
LIGHTPINK = RGB(255, 182, 193)
LIGHTPINK1 = RGB(255, 174, 185)
LIGHTPINK2 = RGB(238, 162, 173)
LIGHTPINK3 = RGB(205, 140, 149)
LIGHTPINK4 = RGB(139, 95, 101)
LIGHTSALMON1 = RGB(255, 160, 122)
LIGHTSALMON2 = RGB(238, 149, 114)
LIGHTSALMON3 = RGB(205, 129, 98)
LIGHTSALMON4 = RGB(139, 87, 66)
LIGHTSEAGREEN = RGB(32, 178, 170)
LIGHTSKYBLUE = RGB(135, 206, 250)
LIGHTSKYBLUE1 = RGB(176, 226, 255)
LIGHTSKYBLUE2 = RGB(164, 211, 238)
LIGHTSKYBLUE3 = RGB(141, 182, 205)
LIGHTSKYBLUE4 = RGB(96, 123, 139)
LIGHTSLATEBLUE = RGB(132, 112, 255)
LIGHTSLATEGRAY = RGB(119, 136, 153)
LIGHTSTEELBLUE = RGB(176, 196, 222)
LIGHTSTEELBLUE1 = RGB(202, 225, 255)
LIGHTSTEELBLUE2 = RGB(188, 210, 238)
LIGHTSTEELBLUE3 = RGB(162, 181, 205)
LIGHTSTEELBLUE4 = RGB(110, 123, 139)
LIGHTYELLOW1 = RGB(255, 255, 224)
LIGHTYELLOW2 = RGB(238, 238, 209)
LIGHTYELLOW3 = RGB(205, 205, 180)
LIGHTYELLOW4 = RGB(139, 139, 122)
LIMEGREEN = RGB(50, 205, 50)
LINEN = RGB(250, 240, 230)
MAGENTA = RGB(255, 0, 255)
MAGENTA2 = RGB(238, 0, 238)
MAGENTA3 = RGB(205, 0, 205)
MAGENTA4 = RGB(139, 0, 139)
MANGANESEBLUE = RGB(3, 168, 158)
MAROON = RGB(128, 0, 0)
MAROON1 = RGB(255, 52, 179)
MAROON2 = RGB(238, 48, 167)
MAROON3 = RGB(205, 41, 144)
MAROON4 = RGB(139, 28, 98)
MEDIUMORCHID = RGB(186, 85, 211)
MEDIUMORCHID1 = RGB(224, 102, 255)
MEDIUMORCHID2 = RGB(209, 95, 238)
MEDIUMORCHID3 = RGB(180, 82, 205)
MEDIUMORCHID4 = RGB(122, 55, 139)
MEDIUMPURPLE = RGB(147, 112, 219)
MEDIUMPURPLE1 = RGB(171, 130, 255)
MEDIUMPURPLE2 = RGB(159, 121, 238)
MEDIUMPURPLE3 = RGB(137, 104, 205)
MEDIUMPURPLE4 = RGB(93, 71, 139)
MEDIUMSEAGREEN = RGB(60, 179, 113)
MEDIUMSLATEBLUE = RGB(123, 104, 238)
MEDIUMSPRINGGREEN = RGB(0, 250, 154)
MEDIUMTURQUOISE = RGB(72, 209, 204)
MEDIUMVIOLETRED = RGB(199, 21, 133)
MELON = RGB(227, 168, 105)
MIDNIGHTBLUE = RGB(25, 25, 112)
MINT = RGB(189, 252, 201)
MINTCREAM = RGB(245, 255, 250)
MISTYROSE1 = RGB(255, 228, 225)
MISTYROSE2 = RGB(238, 213, 210)
MISTYROSE3 = RGB(205, 183, 181)
MISTYROSE4 = RGB(139, 125, 123)
MOCCASIN = RGB(255, 228, 181)
NAVAJOWHITE1 = RGB(255, 222, 173)
NAVAJOWHITE2 = RGB(238, 207, 161)
NAVAJOWHITE3 = RGB(205, 179, 139)
NAVAJOWHITE4 = RGB(139, 121, 94)
NAVY = RGB(0, 0, 128)
OLDLACE = RGB(253, 245, 230)
OLIVE = RGB(128, 128, 0)
OLIVEDRAB = RGB(107, 142, 35)
OLIVEDRAB1 = RGB(192, 255, 62)
OLIVEDRAB2 = RGB(179, 238, 58)
OLIVEDRAB3 = RGB(154, 205, 50)
OLIVEDRAB4 = RGB(105, 139, 34)
ORANGE = RGB(255, 128, 0)
ORANGE1 = RGB(255, 165, 0)
ORANGE2 = RGB(238, 154, 0)
ORANGE3 = RGB(205, 133, 0)
ORANGE4 = RGB(139, 90, 0)
ORANGERED1 = RGB(255, 69, 0)
ORANGERED2 = RGB(238, 64, 0)
ORANGERED3 = RGB(205, 55, 0)
ORANGERED4 = RGB(139, 37, 0)
ORCHID = RGB(218, 112, 214)
ORCHID1 = RGB(255, 131, 250)
ORCHID2 = RGB(238, 122, 233)
ORCHID3 = RGB(205, 105, 201)
ORCHID4 = RGB(139, 71, 137)
PALEGOLDENROD = RGB(238, 232, 170)
PALEGREEN = RGB(152, 251, 152)
PALEGREEN1 = RGB(154, 255, 154)
PALEGREEN2 = RGB(144, 238, 144)
PALEGREEN3 = RGB(124, 205, 124)
PALEGREEN4 = RGB(84, 139, 84)
PALETURQUOISE1 = RGB(187, 255, 255)
PALETURQUOISE2 = RGB(174, 238, 238)
PALETURQUOISE3 = RGB(150, 205, 205)
PALETURQUOISE4 = RGB(102, 139, 139)
PALEVIOLETRED = RGB(219, 112, 147)
PALEVIOLETRED1 = RGB(255, 130, 171)
PALEVIOLETRED2 = RGB(238, 121, 159)
PALEVIOLETRED3 = RGB(205, 104, 137)
PALEVIOLETRED4 = RGB(139, 71, 93)
PAPAYAWHIP = RGB(255, 239, 213)
PEACHPUFF1 = RGB(255, 218, 185)
PEACHPUFF2 = RGB(238, 203, 173)
PEACHPUFF3 = RGB(205, 175, 149)
PEACHPUFF4 = RGB(139, 119, 101)
PEACOCK = RGB(51, 161, 201)
PINK = RGB(255, 192, 203)
PINK1 = RGB(255, 181, 197)
PINK2 = RGB(238, 169, 184)
PINK3 = RGB(205, 145, 158)
PINK4 = RGB(139, 99, 108)
PLUM = RGB(221, 160, 221)
PLUM1 = RGB(255, 187, 255)
PLUM2 = RGB(238, 174, 238)
PLUM3 = RGB(205, 150, 205)
PLUM4 = RGB(139, 102, 139)
POWDERBLUE = RGB(176, 224, 230)
PURPLE = RGB(128, 0, 128)
PURPLE1 = RGB(155, 48, 255)
PURPLE2 = RGB(145, 44, 238)
PURPLE3 = RGB(125, 38, 205)
PURPLE4 = RGB(85, 26, 139)
RASPBERRY = RGB(135, 38, 87)
RAWSIENNA = RGB(199, 97, 20)
RED1 = RGB(255, 0, 0)
RED2 = RGB(238, 0, 0)
RED3 = RGB(205, 0, 0)
RED4 = RGB(139, 0, 0)
ROSYBROWN = RGB(188, 143, 143)
ROSYBROWN1 = RGB(255, 193, 193)
ROSYBROWN2 = RGB(238, 180, 180)
ROSYBROWN3 = RGB(205, 155, 155)
ROSYBROWN4 = RGB(139, 105, 105)
ROYALBLUE = RGB(65, 105, 225)
ROYALBLUE1 = RGB(72, 118, 255)
ROYALBLUE2 = RGB(67, 110, 238)
ROYALBLUE3 = RGB(58, 95, 205)
ROYALBLUE4 = RGB(39, 64, 139)
SALMON = RGB(250, 128, 114)
SALMON1 = RGB(255, 140, 105)
SALMON2 = RGB(238, 130, 98)
SALMON3 = RGB(205, 112, 84)
SALMON4 = RGB(139, 76, 57)
SANDYBROWN = RGB(244, 164, 96)
SAPGREEN = RGB(48, 128, 20)
SEAGREEN1 = RGB(84, 255, 159)
SEAGREEN2 = RGB(78, 238, 148)
SEAGREEN3 = RGB(67, 205, 128)
SEAGREEN4 = RGB(46, 139, 87)
SEASHELL1 = RGB(255, 245, 238)
SEASHELL2 = RGB(238, 229, 222)
SEASHELL3 = RGB(205, 197, 191)
SEASHELL4 = RGB(139, 134, 130)
SEPIA = RGB(94, 38, 18)
SGIBEET = RGB(142, 56, 142)
SGIBRIGHTGRAY = RGB(197, 193, 170)
SGICHARTREUSE = RGB(113, 198, 113)
SGIDARKGRAY = RGB(85, 85, 85)
SGIGRAY12 = RGB(30, 30, 30)
SGIGRAY16 = RGB(40, 40, 40)
SGIGRAY32 = RGB(81, 81, 81)
SGIGRAY36 = RGB(91, 91, 91)
SGIGRAY52 = RGB(132, 132, 132)
SGIGRAY56 = RGB(142, 142, 142)
SGIGRAY72 = RGB(183, 183, 183)
SGIGRAY76 = RGB(193, 193, 193)
SGIGRAY92 = RGB(234, 234, 234)
SGIGRAY96 = RGB(244, 244, 244)
SGILIGHTBLUE = RGB(125, 158, 192)
SGILIGHTGRAY = RGB(170, 170, 170)
SGIOLIVEDRAB = RGB(142, 142, 56)
SGISALMON = RGB(198, 113, 113)
SGISLATEBLUE = RGB(113, 113, 198)
SGITEAL = RGB(56, 142, 142)
SIENNA = RGB(160, 82, 45)
SIENNA1 = RGB(255, 130, 71)
SIENNA2 = RGB(238, 121, 66)
SIENNA3 = RGB(205, 104, 57)
SIENNA4 = RGB(139, 71, 38)
SILVER = RGB(192, 192, 192)
SKYBLUE = RGB(135, 206, 235)
SKYBLUE1 = RGB(135, 206, 255)
SKYBLUE2 = RGB(126, 192, 238)
SKYBLUE3 = RGB(108, 166, 205)
SKYBLUE4 = RGB(74, 112, 139)
SLATEBLUE = RGB(106, 90, 205)
SLATEBLUE1 = RGB(131, 111, 255)
SLATEBLUE2 = RGB(122, 103, 238)
SLATEBLUE3 = RGB(105, 89, 205)
SLATEBLUE4 = RGB(71, 60, 139)
SLATEGRAY = RGB(112, 128, 144)
SLATEGRAY1 = RGB(198, 226, 255)
SLATEGRAY2 = RGB(185, 211, 238)
SLATEGRAY3 = RGB(159, 182, 205)
SLATEGRAY4 = RGB(108, 123, 139)
SNOW1 = RGB(255, 250, 250)
SNOW2 = RGB(238, 233, 233)
SNOW3 = RGB(205, 201, 201)
SNOW4 = RGB(139, 137, 137)
SPRINGGREEN = RGB(0, 255, 127)
SPRINGGREEN1 = RGB(0, 238, 118)
SPRINGGREEN2 = RGB(0, 205, 102)
SPRINGGREEN3 = RGB(0, 139, 69)
STEELBLUE = RGB(70, 130, 180)
STEELBLUE1 = RGB(99, 184, 255)
STEELBLUE2 = RGB(92, 172, 238)
STEELBLUE3 = RGB(79, 148, 205)
STEELBLUE4 = RGB(54, 100, 139)
TAN = RGB(210, 180, 140)
TAN1 = RGB(255, 165, 79)
TAN2 = RGB(238, 154, 73)
TAN3 = RGB(205, 133, 63)
TAN4 = RGB(139, 90, 43)
TEAL = RGB(0, 128, 128)
THISTLE = RGB(216, 191, 216)
THISTLE1 = RGB(255, 225, 255)
THISTLE2 = RGB(238, 210, 238)
THISTLE3 = RGB(205, 181, 205)
THISTLE4 = RGB(139, 123, 139)
TOMATO1 = RGB(255, 99, 71)
TOMATO2 = RGB(238, 92, 66)
TOMATO3 = RGB(205, 79, 57)
TOMATO4 = RGB(139, 54, 38)
TURQUOISE = RGB(64, 224, 208)
TURQUOISE1 = RGB(0, 245, 255)
TURQUOISE2 = RGB(0, 229, 238)
TURQUOISE3 = RGB(0, 197, 205)
TURQUOISE4 = RGB(0, 134, 139)
TURQUOISEBLUE = RGB(0, 199, 140)
VIOLET = RGB(238, 130, 238)
VIOLETRED = RGB(208, 32, 144)
VIOLETRED1 = RGB(255, 62, 150)
VIOLETRED2 = RGB(238, 58, 140)
VIOLETRED3 = RGB(205, 50, 120)
VIOLETRED4 = RGB(139, 34, 82)
WARMGREY = RGB(128, 128, 105)
WHEAT = RGB(245, 222, 179)
WHEAT1 = RGB(255, 231, 186)
WHEAT2 = RGB(238, 216, 174)
WHEAT3 = RGB(205, 186, 150)
WHEAT4 = RGB(139, 126, 102)
WHITE = RGB(255, 255, 255)
WHITESMOKE = RGB(245, 245, 245)
WHITESMOKE = RGB(245, 245, 245)
YELLOW1 = RGB(255, 255, 0)
YELLOW2 = RGB(238, 238, 0)
YELLOW3 = RGB(205, 205, 0)
YELLOW4 = RGB(139, 139, 0)
# Add colours to colours dictionary
colours["aliceblue"] = ALICEBLUE
colours["antiquewhite"] = ANTIQUEWHITE
colours["antiquewhite1"] = ANTIQUEWHITE1
colours["antiquewhite2"] = ANTIQUEWHITE2
colours["antiquewhite3"] = ANTIQUEWHITE3
colours["antiquewhite4"] = ANTIQUEWHITE4
colours["aqua"] = AQUA
colours["aquamarine1"] = AQUAMARINE1
colours["aquamarine2"] = AQUAMARINE2
colours["aquamarine3"] = AQUAMARINE3
colours["aquamarine4"] = AQUAMARINE4
colours["azure1"] = AZURE1
colours["azure2"] = AZURE2
colours["azure3"] = AZURE3
colours["azure4"] = AZURE4
colours["banana"] = BANANA
colours["beige"] = BEIGE
colours["bisque1"] = BISQUE1
colours["bisque2"] = BISQUE2
colours["bisque3"] = BISQUE3
colours["bisque4"] = BISQUE4
colours["black"] = BLACK
colours["blanchedalmond"] = BLANCHEDALMOND
colours["blue"] = BLUE
colours["blue2"] = BLUE2
colours["blue3"] = BLUE3
colours["blue4"] = BLUE4
colours["blueviolet"] = BLUEVIOLET
colours["brick"] = BRICK
colours["brown"] = BROWN
colours["brown1"] = BROWN1
colours["brown2"] = BROWN2
colours["brown3"] = BROWN3
colours["brown4"] = BROWN4
colours["burlywood"] = BURLYWOOD
colours["burlywood1"] = BURLYWOOD1
colours["burlywood2"] = BURLYWOOD2
colours["burlywood3"] = BURLYWOOD3
colours["burlywood4"] = BURLYWOOD4
colours["burntsienna"] = BURNTSIENNA
colours["burntumber"] = BURNTUMBER
colours["cadetblue"] = CADETBLUE
colours["cadetblue1"] = CADETBLUE1
colours["cadetblue2"] = CADETBLUE2
colours["cadetblue3"] = CADETBLUE3
colours["cadetblue4"] = CADETBLUE4
colours["cadmiumorange"] = CADMIUMORANGE
colours["cadmiumyellow"] = CADMIUMYELLOW
colours["carrot"] = CARROT
colours["chartreuse1"] = CHARTREUSE1
colours["chartreuse2"] = CHARTREUSE2
colours["chartreuse3"] = CHARTREUSE3
colours["chartreuse4"] = CHARTREUSE4
colours["chocolate"] = CHOCOLATE
colours["chocolate1"] = CHOCOLATE1
colours["chocolate2"] = CHOCOLATE2
colours["chocolate3"] = CHOCOLATE3
colours["chocolate4"] = CHOCOLATE4
colours["cobalt"] = COBALT
colours["cobaltgreen"] = COBALTGREEN
colours["coldgrey"] = COLDGREY
colours["coral"] = CORAL
colours["coral1"] = CORAL1
colours["coral2"] = CORAL2
colours["coral3"] = CORAL3
colours["coral4"] = CORAL4
colours["cornflowerblue"] = CORNFLOWERBLUE
colours["cornsilk1"] = CORNSILK1
colours["cornsilk2"] = CORNSILK2
colours["cornsilk3"] = CORNSILK3
colours["cornsilk4"] = CORNSILK4
colours["crimson"] = CRIMSON
colours["cyan2"] = CYAN2
colours["cyan3"] = CYAN3
colours["cyan4"] = CYAN4
colours["darkgoldenrod"] = DARKGOLDENROD
colours["darkgoldenrod1"] = DARKGOLDENROD1
colours["darkgoldenrod2"] = DARKGOLDENROD2
colours["darkgoldenrod3"] = DARKGOLDENROD3
colours["darkgoldenrod4"] = DARKGOLDENROD4
colours["darkgray"] = DARKGRAY
colours["darkgreen"] = DARKGREEN
colours["darkkhaki"] = DARKKHAKI
colours["darkolivegreen"] = DARKOLIVEGREEN
colours["darkolivegreen1"] = DARKOLIVEGREEN1
colours["darkolivegreen2"] = DARKOLIVEGREEN2
colours["darkolivegreen3"] = DARKOLIVEGREEN3
colours["darkolivegreen4"] = DARKOLIVEGREEN4
colours["darkorange"] = DARKORANGE
colours["darkorange1"] = DARKORANGE1
colours["darkorange2"] = DARKORANGE2
colours["darkorange3"] = DARKORANGE3
colours["darkorange4"] = DARKORANGE4
colours["darkorchid"] = DARKORCHID
colours["darkorchid1"] = DARKORCHID1
colours["darkorchid2"] = DARKORCHID2
colours["darkorchid3"] = DARKORCHID3
colours["darkorchid4"] = DARKORCHID4
colours["darksalmon"] = DARKSALMON
colours["darkseagreen"] = DARKSEAGREEN
colours["darkseagreen1"] = DARKSEAGREEN1
colours["darkseagreen2"] = DARKSEAGREEN2
colours["darkseagreen3"] = DARKSEAGREEN3
colours["darkseagreen4"] = DARKSEAGREEN4
colours["darkslateblue"] = DARKSLATEBLUE
colours["darkslategray"] = DARKSLATEGRAY
colours["darkslategray1"] = DARKSLATEGRAY1
colours["darkslategray2"] = DARKSLATEGRAY2
colours["darkslategray3"] = DARKSLATEGRAY3
colours["darkslategray4"] = DARKSLATEGRAY4
colours["darkturquoise"] = DARKTURQUOISE
colours["darkviolet"] = DARKVIOLET
colours["deeppink1"] = DEEPPINK1
colours["deeppink2"] = DEEPPINK2
colours["deeppink3"] = DEEPPINK3
colours["deeppink4"] = DEEPPINK4
colours["deepskyblue1"] = DEEPSKYBLUE1
colours["deepskyblue2"] = DEEPSKYBLUE2
colours["deepskyblue3"] = DEEPSKYBLUE3
colours["deepskyblue4"] = DEEPSKYBLUE4
colours["dimgray"] = DIMGRAY
colours["dimgray"] = DIMGRAY
colours["dodgerblue1"] = DODGERBLUE1
colours["dodgerblue2"] = DODGERBLUE2
colours["dodgerblue3"] = DODGERBLUE3
colours["dodgerblue4"] = DODGERBLUE4
colours["eggshell"] = EGGSHELL
colours["emeraldgreen"] = EMERALDGREEN
colours["firebrick"] = FIREBRICK
colours["firebrick1"] = FIREBRICK1
colours["firebrick2"] = FIREBRICK2
colours["firebrick3"] = FIREBRICK3
colours["firebrick4"] = FIREBRICK4
colours["flesh"] = FLESH
colours["floralwhite"] = FLORALWHITE
colours["forestgreen"] = FORESTGREEN
colours["gainsboro"] = GAINSBORO
colours["ghostwhite"] = GHOSTWHITE
colours["gold1"] = GOLD1
colours["gold2"] = GOLD2
colours["gold3"] = GOLD3
colours["gold4"] = GOLD4
colours["goldenrod"] = GOLDENROD
colours["goldenrod1"] = GOLDENROD1
colours["goldenrod2"] = GOLDENROD2
colours["goldenrod3"] = GOLDENROD3
colours["goldenrod4"] = GOLDENROD4
colours["gray"] = GRAY
colours["gray1"] = GRAY1
colours["gray10"] = GRAY10
colours["gray11"] = GRAY11
colours["gray12"] = GRAY12
colours["gray13"] = GRAY13
colours["gray14"] = GRAY14
colours["gray15"] = GRAY15
colours["gray16"] = GRAY16
colours["gray17"] = GRAY17
colours["gray18"] = GRAY18
colours["gray19"] = GRAY19
colours["gray2"] = GRAY2
colours["gray20"] = GRAY20
colours["gray21"] = GRAY21
colours["gray22"] = GRAY22
colours["gray23"] = GRAY23
colours["gray24"] = GRAY24
colours["gray25"] = GRAY25
colours["gray26"] = GRAY26
colours["gray27"] = GRAY27
colours["gray28"] = GRAY28
colours["gray29"] = GRAY29
colours["gray3"] = GRAY3
colours["gray30"] = GRAY30
colours["gray31"] = GRAY31
colours["gray32"] = GRAY32
colours["gray33"] = GRAY33
colours["gray34"] = GRAY34
colours["gray35"] = GRAY35
colours["gray36"] = GRAY36
colours["gray37"] = GRAY37
colours["gray38"] = GRAY38
colours["gray39"] = GRAY39
colours["gray4"] = GRAY4
colours["gray40"] = GRAY40
colours["gray42"] = GRAY42
colours["gray43"] = GRAY43
colours["gray44"] = GRAY44
colours["gray45"] = GRAY45
colours["gray46"] = GRAY46
colours["gray47"] = GRAY47
colours["gray48"] = GRAY48
colours["gray49"] = GRAY49
colours["gray5"] = GRAY5
colours["gray50"] = GRAY50
colours["gray51"] = GRAY51
colours["gray52"] = GRAY52
colours["gray53"] = GRAY53
colours["gray54"] = GRAY54
colours["gray55"] = GRAY55
colours["gray56"] = GRAY56
colours["gray57"] = GRAY57
colours["gray58"] = GRAY58
colours["gray59"] = GRAY59
colours["gray6"] = GRAY6
colours["gray60"] = GRAY60
colours["gray61"] = GRAY61
colours["gray62"] = GRAY62
colours["gray63"] = GRAY63
colours["gray64"] = GRAY64
colours["gray65"] = GRAY65
colours["gray66"] = GRAY66
colours["gray67"] = GRAY67
colours["gray68"] = GRAY68
colours["gray69"] = GRAY69
colours["gray7"] = GRAY7
colours["gray70"] = GRAY70
colours["gray71"] = GRAY71
colours["gray72"] = GRAY72
colours["gray73"] = GRAY73
colours["gray74"] = GRAY74
colours["gray75"] = GRAY75
colours["gray76"] = GRAY76
colours["gray77"] = GRAY77
colours["gray78"] = GRAY78
colours["gray79"] = GRAY79
colours["gray8"] = GRAY8
colours["gray80"] = GRAY80
colours["gray81"] = GRAY81
colours["gray82"] = GRAY82
colours["gray83"] = GRAY83
colours["gray84"] = GRAY84
colours["gray85"] = GRAY85
colours["gray86"] = GRAY86
colours["gray87"] = GRAY87
colours["gray88"] = GRAY88
colours["gray89"] = GRAY89
colours["gray9"] = GRAY9
colours["gray90"] = GRAY90
colours["gray91"] = GRAY91
colours["gray92"] = GRAY92
colours["gray93"] = GRAY93
colours["gray94"] = GRAY94
colours["gray95"] = GRAY95
colours["gray97"] = GRAY97
colours["gray98"] = GRAY98
colours["gray99"] = GRAY99
colours["green"] = GREEN
colours["green1"] = GREEN1
colours["green2"] = GREEN2
colours["green3"] = GREEN3
colours["green4"] = GREEN4
colours["greenyellow"] = GREENYELLOW
colours["honeydew1"] = HONEYDEW1
colours["honeydew2"] = HONEYDEW2
colours["honeydew3"] = HONEYDEW3
colours["honeydew4"] = HONEYDEW4
colours["hotpink"] = HOTPINK
colours["hotpink1"] = HOTPINK1
colours["hotpink2"] = HOTPINK2
colours["hotpink3"] = HOTPINK3
colours["hotpink4"] = HOTPINK4
colours["indianred"] = INDIANRED
colours["indianred"] = INDIANRED
colours["indianred1"] = INDIANRED1
colours["indianred2"] = INDIANRED2
colours["indianred3"] = INDIANRED3
colours["indianred4"] = INDIANRED4
colours["indigo"] = INDIGO
colours["ivory1"] = IVORY1
colours["ivory2"] = IVORY2
colours["ivory3"] = IVORY3
colours["ivory4"] = IVORY4
colours["ivoryblack"] = IVORYBLACK
colours["khaki"] = KHAKI
colours["khaki1"] = KHAKI1
colours["khaki2"] = KHAKI2
colours["khaki3"] = KHAKI3
colours["khaki4"] = KHAKI4
colours["lavender"] = LAVENDER
colours["lavenderblush1"] = LAVENDERBLUSH1
colours["lavenderblush2"] = LAVENDERBLUSH2
colours["lavenderblush3"] = LAVENDERBLUSH3
colours["lavenderblush4"] = LAVENDERBLUSH4
colours["lawngreen"] = LAWNGREEN
colours["lemonchiffon1"] = LEMONCHIFFON1
colours["lemonchiffon2"] = LEMONCHIFFON2
colours["lemonchiffon3"] = LEMONCHIFFON3
colours["lemonchiffon4"] = LEMONCHIFFON4
colours["lightblue"] = LIGHTBLUE
colours["lightblue1"] = LIGHTBLUE1
colours["lightblue2"] = LIGHTBLUE2
colours["lightblue3"] = LIGHTBLUE3
colours["lightblue4"] = LIGHTBLUE4
colours["lightcoral"] = LIGHTCORAL
colours["lightcyan1"] = LIGHTCYAN1
colours["lightcyan2"] = LIGHTCYAN2
colours["lightcyan3"] = LIGHTCYAN3
colours["lightcyan4"] = LIGHTCYAN4
colours["lightgoldenrod1"] = LIGHTGOLDENROD1
colours["lightgoldenrod2"] = LIGHTGOLDENROD2
colours["lightgoldenrod3"] = LIGHTGOLDENROD3
colours["lightgoldenrod4"] = LIGHTGOLDENROD4
colours["lightgoldenrodyellow"] = LIGHTGOLDENRODYELLOW
colours["lightgrey"] = LIGHTGREY
colours["lightpink"] = LIGHTPINK
colours["lightpink1"] = LIGHTPINK1
colours["lightpink2"] = LIGHTPINK2
colours["lightpink3"] = LIGHTPINK3
colours["lightpink4"] = LIGHTPINK4
colours["lightsalmon1"] = LIGHTSALMON1
colours["lightsalmon2"] = LIGHTSALMON2
colours["lightsalmon3"] = LIGHTSALMON3
colours["lightsalmon4"] = LIGHTSALMON4
colours["lightseagreen"] = LIGHTSEAGREEN
colours["lightskyblue"] = LIGHTSKYBLUE
colours["lightskyblue1"] = LIGHTSKYBLUE1
colours["lightskyblue2"] = LIGHTSKYBLUE2
colours["lightskyblue3"] = LIGHTSKYBLUE3
colours["lightskyblue4"] = LIGHTSKYBLUE4
colours["lightslateblue"] = LIGHTSLATEBLUE
colours["lightslategray"] = LIGHTSLATEGRAY
colours["lightsteelblue"] = LIGHTSTEELBLUE
colours["lightsteelblue1"] = LIGHTSTEELBLUE1
colours["lightsteelblue2"] = LIGHTSTEELBLUE2
colours["lightsteelblue3"] = LIGHTSTEELBLUE3
colours["lightsteelblue4"] = LIGHTSTEELBLUE4
colours["lightyellow1"] = LIGHTYELLOW1
colours["lightyellow2"] = LIGHTYELLOW2
colours["lightyellow3"] = LIGHTYELLOW3
colours["lightyellow4"] = LIGHTYELLOW4
colours["limegreen"] = LIMEGREEN
colours["linen"] = LINEN
colours["magenta"] = MAGENTA
colours["magenta2"] = MAGENTA2
colours["magenta3"] = MAGENTA3
colours["magenta4"] = MAGENTA4
colours["manganeseblue"] = MANGANESEBLUE
colours["maroon"] = MAROON
colours["maroon1"] = MAROON1
colours["maroon2"] = MAROON2
colours["maroon3"] = MAROON3
colours["maroon4"] = MAROON4
colours["mediumorchid"] = MEDIUMORCHID
colours["mediumorchid1"] = MEDIUMORCHID1
colours["mediumorchid2"] = MEDIUMORCHID2
colours["mediumorchid3"] = MEDIUMORCHID3
colours["mediumorchid4"] = MEDIUMORCHID4
colours["mediumpurple"] = MEDIUMPURPLE
colours["mediumpurple1"] = MEDIUMPURPLE1
colours["mediumpurple2"] = MEDIUMPURPLE2
colours["mediumpurple3"] = MEDIUMPURPLE3
colours["mediumpurple4"] = MEDIUMPURPLE4
colours["mediumseagreen"] = MEDIUMSEAGREEN
colours["mediumslateblue"] = MEDIUMSLATEBLUE
colours["mediumspringgreen"] = MEDIUMSPRINGGREEN
colours["mediumturquoise"] = MEDIUMTURQUOISE
colours["mediumvioletred"] = MEDIUMVIOLETRED
colours["melon"] = MELON
colours["midnightblue"] = MIDNIGHTBLUE
colours["mint"] = MINT
colours["mintcream"] = MINTCREAM
colours["mistyrose1"] = MISTYROSE1
colours["mistyrose2"] = MISTYROSE2
colours["mistyrose3"] = MISTYROSE3
colours["mistyrose4"] = MISTYROSE4
colours["moccasin"] = MOCCASIN
colours["navajowhite1"] = NAVAJOWHITE1
colours["navajowhite2"] = NAVAJOWHITE2
colours["navajowhite3"] = NAVAJOWHITE3
colours["navajowhite4"] = NAVAJOWHITE4
colours["navy"] = NAVY
colours["oldlace"] = OLDLACE
colours["olive"] = OLIVE
colours["olivedrab"] = OLIVEDRAB
colours["olivedrab1"] = OLIVEDRAB1
colours["olivedrab2"] = OLIVEDRAB2
colours["olivedrab3"] = OLIVEDRAB3
colours["olivedrab4"] = OLIVEDRAB4
colours["orange"] = ORANGE
colours["orange1"] = ORANGE1
colours["orange2"] = ORANGE2
colours["orange3"] = ORANGE3
colours["orange4"] = ORANGE4
colours["orangered1"] = ORANGERED1
colours["orangered2"] = ORANGERED2
colours["orangered3"] = ORANGERED3
colours["orangered4"] = ORANGERED4
colours["orchid"] = ORCHID
colours["orchid1"] = ORCHID1
colours["orchid2"] = ORCHID2
colours["orchid3"] = ORCHID3
colours["orchid4"] = ORCHID4
colours["palegoldenrod"] = PALEGOLDENROD
colours["palegreen"] = PALEGREEN
colours["palegreen1"] = PALEGREEN1
colours["palegreen2"] = PALEGREEN2
colours["palegreen3"] = PALEGREEN3
colours["palegreen4"] = PALEGREEN4
colours["paleturquoise1"] = PALETURQUOISE1
colours["paleturquoise2"] = PALETURQUOISE2
colours["paleturquoise3"] = PALETURQUOISE3
colours["paleturquoise4"] = PALETURQUOISE4
colours["palevioletred"] = PALEVIOLETRED
colours["palevioletred1"] = PALEVIOLETRED1
colours["palevioletred2"] = PALEVIOLETRED2
colours["palevioletred3"] = PALEVIOLETRED3
colours["palevioletred4"] = PALEVIOLETRED4
colours["papayawhip"] = PAPAYAWHIP
colours["peachpuff1"] = PEACHPUFF1
colours["peachpuff2"] = PEACHPUFF2
colours["peachpuff3"] = PEACHPUFF3
colours["peachpuff4"] = PEACHPUFF4
colours["peacock"] = PEACOCK
colours["pink"] = PINK
colours["pink1"] = PINK1
colours["pink2"] = PINK2
colours["pink3"] = PINK3
colours["pink4"] = PINK4
colours["plum"] = PLUM
colours["plum1"] = PLUM1
colours["plum2"] = PLUM2
colours["plum3"] = PLUM3
colours["plum4"] = PLUM4
colours["powderblue"] = POWDERBLUE
colours["purple"] = PURPLE
colours["purple1"] = PURPLE1
colours["purple2"] = PURPLE2
colours["purple3"] = PURPLE3
colours["purple4"] = PURPLE4
colours["raspberry"] = RASPBERRY
colours["rawsienna"] = RAWSIENNA
colours["red1"] = RED1
colours["red2"] = RED2
colours["red3"] = RED3
colours["red4"] = RED4
colours["rosybrown"] = ROSYBROWN
colours["rosybrown1"] = ROSYBROWN1
colours["rosybrown2"] = ROSYBROWN2
colours["rosybrown3"] = ROSYBROWN3
colours["rosybrown4"] = ROSYBROWN4
colours["royalblue"] = ROYALBLUE
colours["royalblue1"] = ROYALBLUE1
colours["royalblue2"] = ROYALBLUE2
colours["royalblue3"] = ROYALBLUE3
colours["royalblue4"] = ROYALBLUE4
colours["salmon"] = SALMON
colours["salmon1"] = SALMON1
colours["salmon2"] = SALMON2
colours["salmon3"] = SALMON3
colours["salmon4"] = SALMON4
colours["sandybrown"] = SANDYBROWN
colours["sapgreen"] = SAPGREEN
colours["seagreen1"] = SEAGREEN1
colours["seagreen2"] = SEAGREEN2
colours["seagreen3"] = SEAGREEN3
colours["seagreen4"] = SEAGREEN4
colours["seashell1"] = SEASHELL1
colours["seashell2"] = SEASHELL2
colours["seashell3"] = SEASHELL3
colours["seashell4"] = SEASHELL4
colours["sepia"] = SEPIA
colours["sgibeet"] = SGIBEET
colours["sgibrightgray"] = SGIBRIGHTGRAY
colours["sgichartreuse"] = SGICHARTREUSE
colours["sgidarkgray"] = SGIDARKGRAY
colours["sgigray12"] = SGIGRAY12
colours["sgigray16"] = SGIGRAY16
colours["sgigray32"] = SGIGRAY32
colours["sgigray36"] = SGIGRAY36
colours["sgigray52"] = SGIGRAY52
colours["sgigray56"] = SGIGRAY56
colours["sgigray72"] = SGIGRAY72
colours["sgigray76"] = SGIGRAY76
colours["sgigray92"] = SGIGRAY92
colours["sgigray96"] = SGIGRAY96
colours["sgilightblue"] = SGILIGHTBLUE
colours["sgilightgray"] = SGILIGHTGRAY
colours["sgiolivedrab"] = SGIOLIVEDRAB
colours["sgisalmon"] = SGISALMON
colours["sgislateblue"] = SGISLATEBLUE
colours["sgiteal"] = SGITEAL
colours["sienna"] = SIENNA
colours["sienna1"] = SIENNA1
colours["sienna2"] = SIENNA2
colours["sienna3"] = SIENNA3
colours["sienna4"] = SIENNA4
colours["silver"] = SILVER
colours["skyblue"] = SKYBLUE
colours["skyblue1"] = SKYBLUE1
colours["skyblue2"] = SKYBLUE2
colours["skyblue3"] = SKYBLUE3
colours["skyblue4"] = SKYBLUE4
colours["slateblue"] = SLATEBLUE
colours["slateblue1"] = SLATEBLUE1
colours["slateblue2"] = SLATEBLUE2
colours["slateblue3"] = SLATEBLUE3
colours["slateblue4"] = SLATEBLUE4
colours["slategray"] = SLATEGRAY
colours["slategray1"] = SLATEGRAY1
colours["slategray2"] = SLATEGRAY2
colours["slategray3"] = SLATEGRAY3
colours["slategray4"] = SLATEGRAY4
colours["snow1"] = SNOW1
colours["snow2"] = SNOW2
colours["snow3"] = SNOW3
colours["snow4"] = SNOW4
colours["springgreen"] = SPRINGGREEN
colours["springgreen1"] = SPRINGGREEN1
colours["springgreen2"] = SPRINGGREEN2
colours["springgreen3"] = SPRINGGREEN3
colours["steelblue"] = STEELBLUE
colours["steelblue1"] = STEELBLUE1
colours["steelblue2"] = STEELBLUE2
colours["steelblue3"] = STEELBLUE3
colours["steelblue4"] = STEELBLUE4
colours["tan"] = TAN
colours["tan1"] = TAN1
colours["tan2"] = TAN2
colours["tan3"] = TAN3
colours["tan4"] = TAN4
colours["teal"] = TEAL
colours["thistle"] = THISTLE
colours["thistle1"] = THISTLE1
colours["thistle2"] = THISTLE2
colours["thistle3"] = THISTLE3
colours["thistle4"] = THISTLE4
colours["tomato1"] = TOMATO1
colours["tomato2"] = TOMATO2
colours["tomato3"] = TOMATO3
colours["tomato4"] = TOMATO4
colours["turquoise"] = TURQUOISE
colours["turquoise1"] = TURQUOISE1
colours["turquoise2"] = TURQUOISE2
colours["turquoise3"] = TURQUOISE3
colours["turquoise4"] = TURQUOISE4
colours["turquoiseblue"] = TURQUOISEBLUE
colours["violet"] = VIOLET
colours["violetred"] = VIOLETRED
colours["violetred1"] = VIOLETRED1
colours["violetred2"] = VIOLETRED2
colours["violetred3"] = VIOLETRED3
colours["violetred4"] = VIOLETRED4
colours["warmgrey"] = WARMGREY
colours["wheat"] = WHEAT
colours["wheat1"] = WHEAT1
colours["wheat2"] = WHEAT2
colours["wheat3"] = WHEAT3
colours["wheat4"] = WHEAT4
colours["white"] = WHITE
colours["whitesmoke"] = WHITESMOKE
colours["whitesmoke"] = WHITESMOKE
colours["yellow1"] = YELLOW1
colours["yellow2"] = YELLOW2
colours["yellow3"] = YELLOW3
colours["yellow4"] = YELLOW4
colours = OrderedDict(sorted(colours.items(), key=lambda t: t[0]))
