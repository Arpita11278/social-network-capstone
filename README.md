# Social Network Friend Suggestion System

A Capstone Project implementing a text-based social network utilizing Graph Data Structures and Core Algorithms. 

## Core Features
- **Graph Representation**: Uses an Adjacency List (Dictionaries and Sets) to represent the undirected graph of users.
- **Add/Remove Users and Friendships**: Efficient O(1) time complexity for connection management.
- **Mutual Friends Finder**: Uses set intersection to rapidly find common connections.
- **Friend Suggestion Algorithm**: Ranks and suggests new friends based on the highest number of mutual connections (Common Neighbors).
- **Shortest Path (Degrees of Separation)**: Implements Breadth-First Search (BFS) to find the shortest connection path between any two users in the network.

## How to Run

1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python social_network.py
   ```
4. An interactive menu will appear where you can test out all the algorithms and features interactively.

## Data Structures and Algorithm Complexity
- **Graph Data Structure**: The network is an undirected graph where nodes are `Users` and edges are `Friendships`.
- **BFS (Shortest Path)**: Time Complexity `O(V + E)` - Guarantees the shortest path in an unweighted graph.
- **Friend Suggestion**: Time Complexity `O(V * D)` where `V` is total users and `D` is the average number of friends per user.
- **Adjacency List Lookup**: Time Complexity `O(1)` - Implemented using HashMaps (Python dictionaries) and HashSets (Python sets) for optimal performance.
