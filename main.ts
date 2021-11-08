let a_button = 0
let lightning_timer = 0
let lightning_distance = 0
let display_complete = 0
input.onButtonPressed(Button.A, function () {
    a_button += 1
    while (a_button > 0) {
        lightning_timer += 1
        basic.pause(1000)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Press the A button when you see the lightning.")
    basic.showString("Press the B button when you see the thunder.")
    basic.showString("Press A + B to repeat the lightning distance.")
})
input.onButtonPressed(Button.B, function () {
    a_button = 0
    if (lightning_timer > 0) {
        basic.showString("" + (lightning_timer))
        basic.showString(" seconds.")
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
        lightning_distance = lightning_timer * 340
        basic.showString(" Thunder is ")
        basic.showString("" + (lightning_distance))
        basic.showString(" metres away.")
        display_complete = 1
    }
})
input.onGesture(Gesture.Shake, function () {
    if (display_complete == 1) {
        basic.showString(" Thunder is ")
        basic.showString("" + (lightning_distance))
        basic.showString(" metres away.")
    }
})
