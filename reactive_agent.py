from time import sleep
from enum import Enum, auto

class TrafficLightState(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

class TrafficLight:
    """Environment: Traffic Light"""
    def __init__(self):
        self.states = list(TrafficLightState)
        self.index = 0

    @property
    def current_state(self):
        return self.states[self.index]

    def next_state(self):
        self.index = (self.index + 1) % len(self.states)
        return self.current_state

class ReactiveAgent:
    """Simple Reactive Agent"""
    ACTIONS = {
        TrafficLightState.RED: "Stop",
        TrafficLightState.YELLOW: "Prepare to move",
        TrafficLightState.GREEN: "Go"
    }

    def perceive_and_act(self, state: TrafficLightState):
        action = self.ACTIONS.get(state, "No action defined")
        print(f"Agent observes: {state.name} -> Action: {action}")

def main(cycles: int = 10, delay: float = 1.0):
    light = TrafficLight()
    agent = ReactiveAgent()

    for _ in range(cycles):
        current = light.current_state
        print(f"\nTraffic Light State: {current.name}")
        agent.perceive_and_act(current)
        sleep(delay)
        light.next_state()

if __name__ == "__main__":
    main()
