import anki_vector
from anki_vector.util import degrees
from anki_vector.connection import ControlPriorityLevel
import threading


class VectorInstructions:
    def __init__(self):
        self.instructions = []
        self._is_executing = False
        self._lock = threading.Lock()

    def add_instruction(self, instruction):
        with self._lock:
            self.instructions.append(instruction)
            if not self._is_executing:
                self._is_executing = True
                threading.Thread(target=self._execute_instructions).start()

    def _execute_instructions(self):
        with anki_vector.Robot(control_priority_level=ControlPriorityLevel.OVERRIDE_BEHAVIORS_PRIORITY) as robot:
            while True:
                with self._lock:
                    if len(self.instructions) == 0:
                        self._is_executing = False
                        break
                    instruction = self.instructions.pop(0)

                try:
                    robot.behavior.execute_behavior_action(instruction)
                except Exception as e:
                    print(f"Error executing instruction: {e}")


# Example usage:
vector_instructions = VectorInstructions()

# Add a drive instruction
vector_instructions.add_instruction(
    anki_vector.behavior.BehaviorAction(
        anki_vector.behavior.DriveOffCharger(),
        anki_vector.behavior.DriveStraight(distance_mm=100, speed=100),
        anki_vector.behavior.TurnInPlace(angle=degrees(90)),
        anki_vector.behavior.DriveStraight(distance_mm=-100, speed=100),
    )
)

# Add a lift instruction
vector_instructions.add_instruction(
    anki_vector.behavior.BehaviorAction(
        anki_vector.behavior.SetLiftHeight(height=1.0),
        anki_vector.behavior.SetLiftHeight(height=0.0),
    )
)