"""
AgriMANET Priority-Aware Packet Scheduler
Author: MacDonald Uwachukwunenye
Description: Simulates an adaptive Weighted Round Robin (WRR) queueing system 
             for heterogeneous agricultural data telemetry over dynamic MANET nodes.
"""

import queue
import time
from typing import Dict, Any, List

class AgriPacket:
    def __init__(self, packet_id: int, data_type: str, priority_level: int, payload_size_kb: float):
        """
        Represents a structured data packet traversing the Agri-MANET.
        Priority Levels: 3 (Critical/Pest Outbreak), 2 (Market/Logistics), 1 (Routine Sensor)
        """
        self.packet_id: int = packet_id
        self.data_type: str = data_type
        self.priority_level: int = priority_level
        self.payload_size_kb: float = payload_size_kb
        self.timestamp: float = time.time()

    def __repr__(self) -> str:
        return f"[Packet {self.packet_id} | {self.data_type} | Priority: {self.priority_level}]"


class AgriMANETScheduler:
    def __init__(self):
        # Multi-queue system mapping priority levels to dedicated buffers
        self.queues: Dict[int, queue.Queue] = {
            3: queue.Queue(),  # High Priority: Disease/Pest Alerts
            2: queue.Queue(),  # Medium Priority: Logistics & Pricing Data
            1: queue.Queue()   # Low Priority: Routine Soil Moisture Logs
        }
        # Weighted execution allocation per cycle (ratio 5:3:1)
        self.weights: Dict[int, int] = {3: 5, 2: 3, 1: 1}

    def ingress_packet(self, packet: AgriPacket) -> None:
        """Enqueues incoming telemetry payload into the corresponding priority queue."""
        if packet.priority_level in self.queues:
            self.queues[packet.priority_level].put(packet)
            print(f"-> Ingress: {packet} buffered successfully.")
        else:
            raise ValueError(f"Invalid network priority class: {packet.priority_level}")

    def process_scheduling_cycle(self) -> List[AgriPacket]:
        """
        Executes a Weighted Round Robin cycle to schedule packets for transmission.
        Ensures high-priority agricultural intelligence clears constraints fast without starving lower queues.
        """
        scheduled_transmissions: List[AgriPacket] = []
        
        for priority_class in:
            tokens = self.weights[priority_class]
            while tokens > 0 and not self.queues[priority_class].empty():
                packet = self.queues[priority_class].get()
                scheduled_transmissions.append(packet)
                tokens -= 1
                
        return scheduled_transmissions


# Demonstration Execution
if __name__ == "__main__":
    print("=== Initializing Agri-MANET Optimization Simulation ===\n")
    network_scheduler = AgriMANETScheduler()

    # Simulating sudden multi-source field ingress data
    mock_traffic: List[AgriPacket] = [
        AgriPacket(101, "Soil Moisture Log", priority_level=1, payload_size_kb=12.5),
        AgriPacket(102, "Locust Swarm Alert", priority_level=3, payload_size_kb=4.2),
        AgriPacket(103, "Market Price Update", priority_level=2, payload_size_kb=8.0),
        AgriPacket(104, "Blight Outbreak Vector", priority_level=3, payload_size_kb=15.1),
        AgriPacket(105, "Weather Forecast Broadcast", priority_level=2, payload_size_kb=24.0),
    ]

    for p in mock_traffic:
        network_scheduler.ingress_packet(p)

    print("\n=== Executing Data-Aware Packet Scheduling Cycle ===")
    transmission_queue = network_scheduler.process_scheduling_cycle()
    
    print("\nOptimized Transmission Order (High-Priority AI Metrics First):")
    for index, packet in enumerate(transmission_queue, 1):
        print(f"Slot {index}: {packet}")
