"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    
    songs = load_songs("data/songs.csv")

    # Starter example profile (kept as is)
    user_prefs = {"genre": "lofi", "mood": "chill", "energy": 0.4}

    # ✅ Added more users (DO NOT change original one)
    user2 = {"genre": "Pop", "mood": "Happy", "energy": 0.9}
    user3 = {"genre": "Rock", "mood": "Sad", "energy": 0.8}
    user4 = {"genre": "Classical", "mood": "Happy", "energy": 0.95}  # edge case

    print("\n--- User 1 (Lofi Chill) ---")
    recommendations = recommend_songs(user_prefs, songs, k=5)
    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- User 2 (High Energy Pop) ---")
    recommendations = recommend_songs(user2, songs, k=5)
    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- User 3 (Sad Rock) ---")
    recommendations = recommend_songs(user3, songs, k=5)
    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

    print("\n--- Edge Case User ---")
    recommendations = recommend_songs(user4, songs, k=5)
    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()