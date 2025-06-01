import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


friends = ["Alex", "Jamie", "Taylor", "Morgan"]
episodes = ["Ep1", "Ep2", "Ep3", "Ep4"]

ratings = np.array([
    [8, 9, 6, 7],
    [7, 8, 7, 9],
    [6, 7, 8, 8],
    [9, 8, 9, 10]
])

reactions = np.array([
    ["Thought-provoking", "Emotional", "Unsettling", "Powerful"],
    ["Emotional", "Emotional", "Thought-provoking", "Intense"],
    ["Unsettling", "Thought-provoking", "Unsettling", "Emotional"],
    ["Powerful", "Emotional", "Powerful", "Thought-provoking"]
])

# 1. Average score per episode
avg_ratings = ratings.mean(axis=0)
print("Average score per episode:")
for ep, avg in zip(episodes, avg_ratings):
    print(f"{ep}: {avg:.2f}")

# 2. Favorite episode
fav_ep_idx = np.argmax(avg_ratings)
print(f"\nFavorite episode: {episodes[fav_ep_idx]} (Avg score: {avg_ratings[fav_ep_idx]:.2f})")

# 3. Toughest critic
avg_per_friend = ratings.mean(axis=1)
toughest_idx = np.argmin(avg_per_friend)
print(f"\nToughest critic: {friends[toughest_idx]} (Avg rating given: {avg_per_friend[toughest_idx]:.2f})")

# 4. Visualizations

# a) Bar plot: Average score per episode
plt.figure(figsize=(6,4))
sns.barplot(x=episodes, y=avg_ratings, palette="viridis")
plt.ylim(0, 10)
plt.ylabel("Average Rating")
plt.title("Average Episode Ratings")
plt.show()

# b) Heatmap: Who gave what ratings
plt.figure(figsize=(8,5))
sns.heatmap(ratings, annot=True, fmt="d", cmap="YlGnBu", xticklabels=episodes, yticklabels=friends)
plt.title("Friends’ Ratings per Episode")
plt.xlabel("Episode")
plt.ylabel("Friend")
plt.show()

# c) Count plot: Reaction frequencies

reactions_flat = reactions.flatten()
reaction_counts = pd.Series(reactions_flat).value_counts()
plt.figure(figsize=(8,4))
sns.barplot(x=reaction_counts.index, y=reaction_counts.values, palette="coolwarm")
plt.ylabel("Frequency")
plt.title("Reaction Frequencies")
plt.xticks(rotation=30)
plt.show()