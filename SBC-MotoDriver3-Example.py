# Import all required libraries
import SBC_MotoDriver3_Lib
import time
import sys

# Main Loop
if __name__ == '__main__':
    try:
        # Initialization of the board with I2C address 0x15 and oe_pin 17
        SBC_MotoDriver3_Lib.init(0x15, 17)
        # Pull the oe_pin low to activate the board
        SBC_MotoDriver3_Lib.enabled(True)
        # Starts the I2C communication
        SBC_MotoDriver3_Lib.begin()
        # Switch off all outputs
        SBC_MotoDriver3_Lib.allOff()
        # Define the RPM and the maximum number of steps for the stepper motor
        SBC_MotoDriver3_Lib.StepperSpeed(30, 2048)
        while True:
            print("Normal usage")
            # Switch on all even outputs
            SBC_MotoDriver3_Lib.allOn(True, False)
            time.sleep(1)
            SBC_MotoDriver3_Lib.allOff()
            time.sleep(1)
            # Switch on all odd outputs
            SBC_MotoDriver3_Lib.allOn(False, True)
            time.sleep(1)
            SBC_MotoDriver3_Lib.allOff()
            time.sleep(1)
            # Switch on a specific output
            SBC_MotoDriver3_Lib.on(0)
            time.sleep(2)
            # Switch off a specific output
            SBC_MotoDriver3_Lib.off(0)
            time.sleep(.5)
            # A specific output is faded in to a specific value over a specific time.
            SBC_MotoDriver3_Lib.fadeIn(0, 20, 250)
            SBC_MotoDriver3_Lib.fadeOut(0, 20, 0)
            time.sleep(1)
            # Sets the Pwm value of a specific output
            SBC_MotoDriver3_Lib.pwm(0, 199)
            time.sleep(1)
            # Read the status of the specified output
            print(SBC_MotoDriver3_Lib.ledStatus(0))
            print(SBC_MotoDriver3_Lib.pwmStatus(0))
            time.sleep(2)
            SBC_MotoDriver3_Lib.allOff()
            time.sleep(1)
#            print("Stepper")
#            # Let the stepper motor move the desired number of steps on the desired pins at the previously set speed.
#            SBC_MotoDriver3_Lib.Stepper(2000, 4, 5, 6, 7)
#            time.sleep(5)
            
    except KeyboardInterrupt:
        SBC_MotoDriver3_Lib.allOff()
        sys.exit(0)