import collections

class Users:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"User({self.user_id}: {self.name}, Age: {self.age})"

class SocialNetwork:
    def __init__(self):
        # Maps user_id to User object
        self.users = {}
        # Adjacency list: maps user_id to a set of friend user_ids
        self.adj_list = {}

    def add_user(self, user_id, name, age):
        """
        Time Complexity: O(1)
        Space Complexity: O(1) per user
        """
        if user_id in self.users:
            print(f"User with ID {user_id} already exists.")
            return False
        
        try:
            age = int(age)
            if age <= 0:
                print("Age must be a positive number.")
                return False
        except ValueError:
            print("Invalid age. Please enter a number.")
            return False
        
        self.users[user_id] = Users(user_id, name, age)
        self.adj_list[user_id] = set()
        print(f"User '{name}' added successfully.")
        return True

    def remove_user(self, user_id):
        """
        Time Complexity: O(D_max) where D_max is the maximum degree of the user being removed.
        Space Complexity: O(1)
        """
        if user_id not in self.users:
            print(f"User ID {user_id} not found.")
            return False
        
        # Create a copy of the set of friends to iterate over
        # Ensure user_id is in adj_list before accessing, though add_user ensures this.
        if user_id in self.adj_list:
            for friend_id in list(self.adj_list[user_id]):
                if friend_id in self.adj_list: # Defensive check
                    self.adj_list[friend_id].discard(user_id) # Use discard to avoid KeyError if not present
            del self.adj_list[user_id]
        
        del self.users[user_id]
        print(f"User {user_id} removed successfully.")
        return True

    def add_friendship(self, user_id1, user_id2):
        """
        Adds a bidirectional connection.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if user_id1 not in self.users or user_id2 not in self.users:
            print("One or both users do not exist.")
            return False
        
        if user_id1 == user_id2:
            print("A user cannot be friends with themselves.")
            return False
            
        self.adj_list[user_id1].add(user_id2)
        self.adj_list[user_id2].add(user_id1)
        print(f"Friendship added between {user_id1} and {user_id2}.")
        return True

    def remove_friendship(self, user_id1, user_id2):
        """
        Removes a bidirectional connection.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if user_id1 not in self.users or user_id2 not in self.users:
            print("One or both users do not exist.")
            return False
            
        if user_id2 in self.adj_list[user_id1]:
            self.adj_list[user_id1].remove(user_id2)
            self.adj_list[user_id2].remove(user_id1)
            print(f"Friendship removed between {user_id1} and {user_id2}.")
            return True
        else:
            print("These users are not friends.")
            return False

    def get_mutual_friends(self, user_id1, user_id2):
        """
        Time Complexity: O(min(D1, D2)) where D is the number of friends, because of set intersection.
        Space Complexity: O(min(D1, D2)) for returning the list
        """
        if user_id1 not in self.users or user_id2 not in self.users:
            # This message is handled by the caller (suggest_friends) if users don't exist.
            # For direct calls, it's still useful.
            print("One or both users do not exist.")
            return []
            
        mutuals = self.adj_list[user_id1].intersection(self.adj_list[user_id2])
        return list(mutuals)

    def suggest_friends(self, user_id):
        """
        Suggests friends by ranking non-friends based on the number of mutual friends.
        Time Complexity: O(V * D_avg) where V is total users and D_avg is the average degree.
        More precisely, O(V * D_max) where D_max is the maximum degree, due to get_mutual_friends.
        Space Complexity: O(V) to store the suggestions.
        """
        if user_id not in self.users:
            print("User does not exist.")
            return []
            
        suggestions = []
        my_friends = self.adj_list[user_id]
        
        for other_id in self.users:
            if other_id == user_id or other_id in my_friends:
                continue
            
            # No need to check if other_id exists here, as we are iterating over self.users
            mutual_count = len(self.get_mutual_friends(user_id, other_id))
            if mutual_count > 0:
                suggestions.append((other_id, mutual_count))
                
        # Sort by mutual friend count in descending order
        suggestions.sort(key=lambda x: x[1], reverse=True)
        return suggestions

    def shortest_path(self, start_id, target_id):
        """
        Breadth-First Search (BFS) to find the shortest path between two users.
        Time Complexity: O(V + E) where V is vertices and E is edges.
        Space Complexity: O(V) for the queue and visited structures.
        """
        if start_id not in self.users or target_id not in self.users:
            print("One or both users do not exist.")
            return None
            
        if start_id == target_id:
            return [start_id]
            
        queue = collections.deque([[start_id]])
        visited = set([start_id])
        
        while queue:
            path = queue.popleft()
            current_user = path[-1]
            
            for neighbor in self.adj_list[current_user]:
                if neighbor == target_id:
                    return path + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
                    
        return None # No path found

    def display_network(self):
        """
        Time Complexity: O(V + E)
        """
        print("\n--- Social Network Adjacency List ---")
        for user_id, friends in self.adj_list.items():
            friend_names = [self.users[fid].name for fid in friends]
            print(f"{self.users[user_id].name} ({user_id}) -> {', '.join(friend_names) if friend_names else 'No friends'}")
        print("-------------------------------------")

if __name__ == "__main__":
    main()