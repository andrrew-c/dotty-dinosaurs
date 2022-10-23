from code.functions import Simulations


if __name__ == "__main__":

    # # Start small with 2 players
    num_players = 4

    # Simulations = 1
    num_simulations = 10000

    # Initialise simulation
    sim = Simulations(num_players, num_simulations)

    # Run simulations
    sim.run_simulations()

    # Print out winning records
    sim.winner_records