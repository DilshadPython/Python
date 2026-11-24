"""
Demonstrates event-controlled while loops driven by state conditions or sentinel signals.
"""
from typing import List


def event_control_loop(events: List[str], exit_signal: str = 'exit') -> List[str]:
    """Process incoming event sequence until exit_signal is encountered."""
    idx = 0
    processed: List[str] = []
    while idx < len(events):
        event = events[idx]
        if event == exit_signal:
            break
        processed.append(event)
        idx += 1
    return processed


if __name__ == '__main__':
    stream = ['start', 'load_data', 'process_job', 'exit', 'post_job']
    output = event_control_loop(stream)
    print(f"Processed events before exit: {output}")
