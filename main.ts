let LEVEL = 0
basic.forever(function () {
    LEVEL = pins.analogReadPin(AnalogReadWritePin.P0)
    if (LEVEL <= 350) {
        basic.showIcon(IconNames.Happy)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P16, 1)
    } else if (LEVEL > 350 && LEVEL <= 600) {
        basic.showIcon(IconNames.Confused)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P16, 0)
    } else if (LEVEL > 600) {
        basic.showIcon(IconNames.Sad)
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P16, 0)
        music.play(music.createSoundExpression(WaveShape.Noise, 4053, 4336, 255, 0, 9999, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.LoopingInBackground)
    }
})
