
def RGB(r, g, b):
    return (r << 16) | (g << 8) | b

def DEGREES(n):
    # Convert degrees to Furmans
    return 65536 * n / 360

NEVER                = 0
LESS                 = 1
LEQUAL               = 2
GREATER              = 3
GEQUAL               = 4
EQUAL                = 5
NOTEQUAL             = 6
ALWAYS               = 7

ARGB1555             = 0
L1                   = 1
L4                   = 2
L8                   = 3
RGB332               = 4
ARGB2                = 5
ARGB4                = 6
RGB565               = 7
PALETTED             = 8
TEXT8X8              = 9
TEXTVGA              = 10
BARGRAPH             = 11
PALETTED565          = 14       # FT810
PALETTED4444         = 15       # FT810
PALETTED8            = 16       # FT810
L2                   = 17       # FT810

GLFORMAT             = 31       # FT815
ASTC_4x4             = 0x93B0   # BT815
ASTC_5x4             = 0x93B1   # BT815
ASTC_5x5             = 0x93B2   # BT815
ASTC_6x5             = 0x93B3   # BT815
ASTC_6x6             = 0x93B4   # BT815
ASTC_8x5             = 0x93B5   # BT815
ASTC_8x6             = 0x93B6   # BT815
ASTC_8x8             = 0x93B7   # BT815
ASTC_10x5            = 0x93B8   # BT815
ASTC_10x6            = 0x93B9   # BT815
ASTC_10x8            = 0x93BA   # BT815
ASTC_10x10           = 0x93BB   # BT815
ASTC_12x10           = 0x93BC   # BT815
ASTC_12x12           = 0x93BD   # BT815


NEAREST              = 0
BILINEAR             = 1

BORDER               = 0
REPEAT               = 1

KEEP                 = 1
REPLACE              = 2
INCR                 = 3
DECR                 = 4
INVERT               = 5

DLSWAP_DONE          = 0
DLSWAP_LINE          = 1
DLSWAP_FRAME         = 2

INT_SWAP             = 1
INT_TOUCH            = 2
INT_TAG              = 4
INT_SOUND            = 8
INT_PLAYBACK         = 16
INT_CMDEMPTY         = 32
INT_CMDFLAG          = 64
INT_CONVCOMPLETE     = 128

TOUCHMODE_OFF        = 0
TOUCHMODE_ONESHOT    = 1
TOUCHMODE_FRAME      = 2
TOUCHMODE_CONTINUOUS = 3

ZERO                 = 0
ONE                  = 1
SRC_ALPHA            = 2
DST_ALPHA            = 3
ONE_MINUS_SRC_ALPHA  = 4
ONE_MINUS_DST_ALPHA  = 5

BITMAPS              = 1
POINTS               = 2
LINES                = 3
LINE_STRIP           = 4
EDGE_STRIP_R         = 5
EDGE_STRIP_L         = 6
EDGE_STRIP_A         = 7
EDGE_STRIP_B         = 8
RECTS                = 9

OPT_MONO             = 1
OPT_NODL             = 2
OPT_FLAT             = 256
OPT_CENTERX          = 512
OPT_CENTERY          = 1024
OPT_CENTER           = (OPT_CENTERX | OPT_CENTERY)
OPT_NOBACK           = 4096
OPT_NOTICKS          = 8192
OPT_NOHM             = 16384
OPT_NOPOINTER        = 16384
OPT_NOSECS           = 32768
OPT_NOHANDS          = 49152
OPT_RIGHTX           = 2048
OPT_SIGNED           = 256

LINEAR_SAMPLES       = 0
ULAW_SAMPLES         = 1
ADPCM_SAMPLES        = 2


# The built-in audio samples
HARP = 0x40     # Instruments
XYLOPHONE = 0x41
TUBA = 0x42
GLOCKENSPIEL = 0x43
ORGAN = 0x44
TRUMPET = 0x45
PIANO = 0x46
CHIMES = 0x47
MUSICBOX = 0x48
BELL = 0x49
CLICK = 0x50     # Percussive
SWITCH = 0x51
COWBELL = 0x52
NOTCH = 0x53
HIHAT = 0x54
KICKDRUM = 0x55
POP = 0x56
CLACK = 0x57
CHACK = 0x58
MUTE = 0x60     # Management
UNMUTE = 0x61

RAM_CMD = 0x308000
RAM_DL = 0x300000
REG_CLOCK = 0x302008
REG_CMDB_SPACE = 0x302574
REG_CMDB_WRITE = 0x302578
REG_CMD_DL = 0x302100
REG_CMD_READ = 0x3020f8
REG_CMD_WRITE = 0x3020fc
REG_CPURESET = 0x302020
REG_CSPREAD = 0x302068
REG_DITHER = 0x302060
REG_DLSWAP = 0x302054
REG_FRAMES = 0x302004
REG_FREQUENCY = 0x30200c
REG_GPIO = 0x302094
REG_GPIO_DIR = 0x302090
REG_HCYCLE = 0x30202c
REG_HOFFSET = 0x302030
REG_HSIZE = 0x302034
REG_HSYNC0 = 0x302038
REG_HSYNC1 = 0x30203c
REG_ID = 0x302000
REG_INT_EN = 0x3020ac
REG_INT_FLAGS = 0x3020a8
REG_INT_MASK = 0x3020b0
REG_MACRO_0 = 0x3020d8
REG_MACRO_1 = 0x3020dc
REG_OUTBITS = 0x30205c
REG_PCLK = 0x302070
REG_PCLK_POL = 0x30206c
REG_PLAY = 0x30208c
REG_PLAYBACK_FORMAT = 0x3020c4
REG_PLAYBACK_FREQ = 0x3020c0
REG_PLAYBACK_LENGTH = 0x3020b8
REG_PLAYBACK_LOOP = 0x3020c8
REG_PLAYBACK_PLAY = 0x3020cc
REG_PLAYBACK_READPTR = 0x3020bc
REG_PLAYBACK_START = 0x3020b4
REG_PWM_DUTY = 0x3020d4
REG_PWM_HZ = 0x3020d0
REG_ROTATE = 0x302058
REG_SOUND = 0x302088
REG_SWIZZLE = 0x302064
REG_TAG = 0x30207c
REG_TAG_X = 0x302074
REG_TAG_Y = 0x302078
REG_TAP_CRC = 0x302024
REG_TOUCH_ADC_MODE = 0x302108
REG_TOUCH_CHARGE = 0x30210c
REG_TOUCH_DIRECT_XY = 0x30218c
REG_TOUCH_DIRECT_Z1Z2 = 0x302190
REG_TOUCH_MODE = 0x302104
REG_TOUCH_OVERSAMPLE = 0x302114
REG_TOUCH_RAW_XY = 0x30211c
REG_TOUCH_RZ = 0x302120
REG_TOUCH_RZTHRESH = 0x302118
REG_TOUCH_SCREEN_XY = 0x302124
REG_TOUCH_SETTLE = 0x302110
REG_TOUCH_TAG = 0x30212c
REG_TOUCH_TAG_XY = 0x302128
REG_TOUCH_TRANSFORM_A = 0x302150
REG_TOUCH_TRANSFORM_B = 0x302154
REG_TOUCH_TRANSFORM_C = 0x302158
REG_TOUCH_TRANSFORM_D = 0x30215c
REG_TOUCH_TRANSFORM_E = 0x302160
REG_TOUCH_TRANSFORM_F = 0x302164
REG_TRACKER = 0x309000
REG_TRIM = 0x302180
REG_VCYCLE = 0x302040
REG_VOFFSET = 0x302044
REG_VOL_PB = 0x302080
REG_VOL_SOUND = 0x302084
REG_VSIZE = 0x302048
REG_VSYNC0 = 0x30204c
REG_VSYNC1 = 0x302050

def VERTEX2II(x, y, handle, cell):
    return ((2 << 30) | ((x & 511) << 21) | ((y & 511) << 12) | ((handle & 31) << 7) | ((cell & 127) << 0))

RED                  = 2
GREEN                = 3
BLUE                 = 4
ALPHA                = 5

# These are 815 registers
REG_FLASH_SIZE = 0x00309024 
REG_FLASH_STATUS = 0x003025f0 

