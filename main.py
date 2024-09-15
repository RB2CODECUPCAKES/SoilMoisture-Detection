LEVEL = 0

def on_forever():
    global LEVEL
    LEVEL = pins.analog_read_pin(AnalogReadWritePin.P1)
    if LEVEL <= 450:
        basic.show_string("PERFECT!")
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P16, 1)
    elif LEVEL > 450 and LEVEL <= 600:
        LIGHT = 0
        basic.show_string("AVERAGE!")
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P16, 0)
        if LIGHT > 200:
            music.play(music.create_sound_expression(WaveShape.SINE,
                    5000,
                    5000,
                    255,
                    255,
                    9999,
                    SoundExpressionEffect.WARBLE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.LOOPING_IN_BACKGROUND)
    elif LEVEL > 600:
        basic.show_string("LOW!")
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P16, 0)
        music.play(music.create_sound_expression(WaveShape.SQUARE,
                5000,
                5000,
                255,
                255,
                9999,
                SoundExpressionEffect.TREMOLO,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
basic.forever(on_forever)
