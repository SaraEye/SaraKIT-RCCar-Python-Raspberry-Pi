import pygame
import sarakitdevices as sk

def initialize_pygame():
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Initialized joystick: {joystick.get_name()}")

def main():
    initialize_pygame()

    sk.BLDCMotor_PolePairs(0, 11)
    sk.BLDCMotor_PolePairs(1, 11)
    sk.BLDCMotor_InitFOC(0,0,0,0)
    sk.BLDCMotor_On(0, True)  # speed
    sk.BLDCMotor_On(1, True)  # steering

    startX = -10
    running = True
    print("\rStart Loop (q to quit)")
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        print("\n\rButtonA pressed")
                    elif event.button == 1:
                        print("\n\rButtonB pressed")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Exiting on 'q' key press")
                        running = False

            # Get joystick axes for steering and speed
            px = -pygame.joystick.Joystick(0).get_axis(0) * 25
            py = -pygame.joystick.Joystick(0).get_axis(3) * 100

            print(f"\rPX: {px + startX:.2f}, PY: {py:.2f}", end='')

            # Update motor positions based on joystick inputs
            direction = 1 if py > 0 else -1
            abs_torque = abs(int(py))  # Convert to integer and take the absolute value

            sk.BLDCMotor_MoveToAngle(1, int(px + startX), 1, 80, True)
            sk.BLDCMotor_MoveContinuousTorque(0, direction, abs_torque)

    finally:
        sk.BLDCMotor_MoveStop(0)
        sk.BLDCMotor_MoveStop(1)
        pygame.joystick.quit()
        pygame.quit()

if __name__ == "__main__":
    main()
