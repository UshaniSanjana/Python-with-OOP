import matplotlib.pyplot as plt
from community import Community

# Example usage
community = Community()
days_infected_data, hospitalized_data, fatalities_data, recovered_data = community.run_simulation(num_days=50)
community.plot_charts(days_infected_data, hospitalized_data, fatalities_data, recovered_data)
