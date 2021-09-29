def catchConfirmed():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # # # # #
                . # # # .
    """)
    music.play_tone(131, music.beat(BeatFraction.WHOLE))
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 100)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, 100)
    basic.pause(1000)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
def startGame():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    DFRobotMaqueenPlus.servo_run(Servos.S2, 0)
    basic.pause(500)
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, 50)
    basic.pause(750)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
def idle():
    DFRobotMaqueenPlus.servo_run(Servos.S1, randint(0, 180))
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
    basic.pause(1500)
C = 0
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
DFRobotMaqueenPlus.i2c_init()
DFRobotMaqueenPlus.PID(PID.OFF)
DFRobotMaqueenPlus.servo_run(Servos.S1, 90)

def on_forever():
    huskylens.request()
    if huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        startGame()
        DFRobotMaqueenPlus.servo_run(Servos.S1, 90)
    else:
        idle()
basic.forever(on_forever)

def on_in_background():
    global C
    while True:
        C = DFRobotMaqueenPlus.ultra_sonic(PIN.P1, PIN.P2)
        if C < 10 and C != 0:
            catchConfirmed()
control.in_background(on_in_background)
