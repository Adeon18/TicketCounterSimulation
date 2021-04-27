"""
The main simulation module with the simulation class
"""

from arrays import Array
from llistqueue import Queue
from people import TicketAgent, Passanger


class TicketCounterSimulation:
    """
    The simulation class for an airpost ticket counter
    """
    def __init__(self, num_agents, num_minutes, time_between_entry, service_time):
        """
        num_agents: The number of servers
        num_minutes: the number of customers
        time_between_entry: average time between a new customer entry
        service_time: The time needed to service a customer
        """
        self._arrive_prob = 1.0 / time_between_entry
        self._service_time = service_time
        self._num_minutes = num_minutes
        # Simulation Components
        self._passenger_queue = Queue()
        self._agent_queue = Array(num_agents)
        for i in range(num_agents):
            self._agent_queue[i] = TicketAgent(i+1)
        # Simulation Variables
        self._total_wait_time = 0
        self._num_passengers = 0
    
    def run(self):
        """
        Run the simulation step by step
        """
        for time in range(self._num_minutes + 1):
            self._handle_arrival(time)
            self._handle_service_begin(time)
            self._handle_service_end(time)
    
    def print_results(self):
        """*
        Print the results
        """
        number_served = self._num_passengers - len(self._passenger_queue)
        avg_wait = float(self._total_wait_time) / number_served
        print()
        print(f"Number of passengers served = {number_served}")
        print(f"Number of passengers remaining in line = {len(self._passengerQ)}")
        print(f"The average wait time was {avg_wait} minutes.")