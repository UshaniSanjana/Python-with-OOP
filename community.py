from family import Family
from person import Person
import random
import matplotlib.pyplot as plt

class Community:
    def __init__(self, num_families=100000):
        self.families = [self.create_family() for _ in range(num_families)]
        self.infected_count = 0
        self.hospitalized_count = 0
        self.fatality_count = 0
        self.recovered_count = 0
        self.infected_families=0

    def create_family(self):
        num_members = random.randint(2, 7)
        return Family([Person(self.get_age_group()) for _ in range(num_members)])

    def get_age_group(self):
        rand_num = random.random()
        if rand_num <= 0.2:
            #print("child")
            return "children"
        elif rand_num <= 0.5:
            #print("adult")
            return "adults"
        else:
            #print("seniiuo")
            return "senior_citizens"

    # Other methods remain unchanged

    def simulate_day(self):
        daily_infected = 0
        daily_hospitalized = 0
        daily_fatalities = 0
        daily_recovered = 0

        for family in self.families:
            family.update_family()

        for family in self.families:
            if family.is_infected():
                self.infected_families+=1

                daily_infected += family.infect_count
                if random.random() <= 0.001:  # 0.1% fatality rate
                    daily_fatalities += 1
                else:
                    daily_hospitalized += 1

        

        daily_recovered = sum(
            1 for family in self.families if all(not member.infected for member in family.members)
        )

        for family in self.families:
            family.update_family()

        print("Daily Infected:", daily_infected)
        print("Daily Hospitalized:", daily_hospitalized)
        print("Daily Fatalities:", daily_fatalities)
        print("Daily Recovered:", daily_recovered)
        print("Infected family numbers : ", self.infected_families)

        return daily_infected, daily_hospitalized, daily_fatalities, daily_recovered


    def run_simulation(self, num_days=50):
        days_infected_data = []
        hospitalized_data = []
        fatalities_data = []
        recovered_data = []

        rand_num1=random.randint(0,100000)

        self.families[rand_num1].members[1].infect()

        for day in range(1, num_days + 1):
            daily_infected, daily_hospitalized, daily_fatalities, daily_recovered = self.simulate_day()

            print(f"Day {day}: Infected={daily_infected}, Hospitalized={daily_hospitalized}, Fatalities={daily_fatalities}, Recovered={daily_recovered}")

            self.infected_count += daily_infected
            self.hospitalized_count += daily_hospitalized
            self.fatality_count += daily_fatalities
            self.recovered_count += daily_recovered

            days_infected_data.append(self.infected_count)
            hospitalized_data.append(self.hospitalized_count)
            fatalities_data.append(self.fatality_count)
            recovered_data.append(self.recovered_count)

        return days_infected_data, hospitalized_data, fatalities_data, recovered_data

    def plot_charts(self, days_infected_data, hospitalized_data, fatalities_data, recovered_data):
        output_directory = "/absolute/path/to/output/directory"  # Update with the actual absolute path
        print("Output directory:", output_directory)

        plt.figure(figsize=(10, 6))

        plt.subplot(2, 2, 1)
        plt.plot(days_infected_data, label='Infected')
        plt.title('Daily Infected Patients')
        plt.xlabel('Days')
        plt.ylabel('Count')
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(hospitalized_data, label='Hospitalized')
        plt.title('Total Hospitalized Patients')
        plt.xlabel('Days')
        plt.ylabel('Count')
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(fatalities_data, label='Fatalities')
        plt.title('Total Fatalities')
        plt.xlabel('Days')
        plt.ylabel('Count')
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(recovered_data, label='Recovered')
        plt.title('Recovered People')
        plt.xlabel('Days')
        plt.ylabel('Count')
        plt.legend()

        plt.tight_layout()
        plt.show()
    
    plt.tight_layout()
    plt.savefig("output_charts.png")  # Save the plot to a file instead of displaying it
    

