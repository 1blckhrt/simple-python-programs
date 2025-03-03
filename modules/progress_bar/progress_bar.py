import sys

def start_bar(
    current: int,
    total: int,
    bar_length: int,
    fill_char: str,
    empty_char: str,
    last_progress: float = -1
): 
    """
    Displays a progress bar in the console.
    """
    if current > total:
        current = total
    if current < 0:
        current = 0
    
    progress = (current / total) * 100
    
    if progress == last_progress:
        return last_progress
    
    filled_length = int((current / total) * bar_length)
    
    percentage = f"{progress:.1f}%"
    
    bar = f"{fill_char * filled_length}{empty_char * (bar_length - filled_length)}"
    
    full_bar = f"[{bar}] {percentage}"

    sys.stdout.write(f"\r{full_bar}")
    sys.stdout.flush()
    
    if current == total:
        print("\nDone!")
