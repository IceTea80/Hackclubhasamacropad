import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.modules = [
    Layers(),
    EncoderHandler(),
]

keyboard.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19)
keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = keyboard.modules[1]
encoder_handler.pins = ((board.GP1, board.GP0, None),)
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3, KC.N4,
        KC.N5, KC.N6, KC.N7, KC.N8,
        KC.N9, KC.N0, KC.F13, KC.F14,
        KC.F15, KC.F16, KC.F17, KC.F18,
    ],
    [
        KC.MUTE, KC.VOLD, KC.VOLU, KC.PLAY,
        KC.PAUS, KC.STOP, KC.MRWD, KC.MFWD,
        KC.MPRV, KC.MNXT, KC.HOME, KC.END,
        KC.PGUP, KC.PGDN, KC.LCTRL, KC.LGUI,
    ],
]

if __name__ == "__main__":
    keyboard.go()
