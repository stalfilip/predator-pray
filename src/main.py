import engine as pps
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    game_map = pps.Map()
    num_turns = 200

    prey_counts = []
    predator_counts = []
    empty_count = []

    print(f"Running {num_turns} turns...")
    for turn in range(num_turns):
        if (turn+1) % (num_turns // 5) == 0:
            print(f"Turn {turn+1}/{num_turns}")        
        game_map.turn()
        empty, prey, predator = game_map.count_species()
        empty_count.append(empty)
        prey_counts.append(prey)
        predator_counts.append(predator)
        # time.sleep(0.5)  # Removed for faster execution when not viewing interactively

    # Plotting the results
    print("Done with simulation")
    plt.plot(empty_count, label='Grass')
    plt.plot(prey_counts, label='Prey')
    plt.plot(predator_counts, label='Predator')
    plt.xlabel('Turns')
    plt.ylabel('Count')
    plt.title('Predator and Prey Counts Over Time')
    plt.legend()

    # Generate a unique filename using the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(f'plots/plot_{timestamp}.png')  # Save the figure to a file

if __name__ == "__main__":
    main()