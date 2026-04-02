# 🎵 Music Recommender Simulation

## Project Summary

In this project, I created a simple music recommender system that suggests songs based on a user's taste profile. It compares song features like genre, mood, energy, and tempo with what the user prefers.

Platforms like Spotify and YouTube use similar ideas. They use collaborative filtering, which looks at other users’ behavior such as likes, skips, and playlists. They also use content-based filtering, which focuses on song features like genre, tempo, and mood.

This project shows how user data and song features can be used together to generate personalized song recommendations.
---

## How The System Works

## How The System Works

In real-world systems like Spotify or YouTube, recommendation engines use both user behavior (likes, skips, playlists) and song features to predict what users will enjoy. They often combine collaborative filtering and content-based filtering to improve recommendations.

In this project, the system uses content-based filtering. It compares song features with a user’s preferences to recommend songs that match their taste.

### Features Used

- **Song features:** genre, mood, energy, tempo_bpm, valence, danceability, acousticness  
- **UserProfile features:** preferred genre, preferred mood, target energy level, and preference for acoustic music  

### Scoring Rule

The recommender assigns a score to each song based on how well it matches the user’s preferences.

- **Categorical features (genre, mood):**  
  If the song matches the user’s preference, it gets a score of 1. Otherwise, it gets 0.

- **Numerical features (energy, tempo, valence):**  
  The score is based on how close the song’s value is to the user’s preference using:  
  score = 1 - |song_value - user_value|

- **Weighted total score:**  
  genre (0.3), mood (0.3), energy (0.2), tempo (0.1), valence (0.1)

### Ranking Rule

After calculating scores for all songs, the system sorts them from highest to lowest score and recommends the top k songs.

### Algorithm Recipe

The recommender system assigns a score to each song based on how well it matches the user’s preferences.

- **+2.0 points for a genre match**  
  If the song’s genre matches the user’s favorite genre, it receives 2 points.

- **+1.0 point for a mood match**  
  If the song’s mood matches the user’s preferred mood, it receives 1 point.

- **Similarity score for energy**  
  The system calculates how close the song’s energy is to the user’s target energy using:  
  score += (1 - |song_energy - user_energy|)

After calculating the total score for each song, all songs are sorted from highest to lowest score. The system then recommends the top k songs with the highest scores.

### Limitations and Bias

This recommender system has some limitations. It mainly focuses on matching genre and mood, which means it may over-prioritize these features and ignore other important aspects of music. For example, a song with a different genre but a very similar vibe might not be recommended.

The system also uses simple numerical comparisons for features like energy, which may not fully capture how users perceive music. Additionally, because the dataset is small, the recommendations may not be very diverse.

In real-world systems, much larger datasets and more advanced methods are used to reduce bias and improve recommendation quality.

flowchart TD
    A[Start] --> B["Input: User Preferences<br/>(genre, mood, energy)"]
    B --> C[Load songs from CSV]
    C --> D[Initialize empty scores list]
    D --> E[For each song in songs]
    E --> F{Genre match?}
    F -->|Yes| G[genre_score = 2]
    F -->|No| H[genre_score = 0]
    G --> I{Mood match?}
    H --> I
    I -->|Yes| J[mood_score = 1]
    I -->|No| K[mood_score = 0]
    J --> L["energy_similarity = 1 - <br/>abs(energy difference)"]
    K --> L
    L --> M["total_score = genre_score <br/>+ mood_score + energy"]
    M --> N[Store song with score]
    N --> O{More songs?}
    O -->|Yes| E
    O -->|No| P[Sort by score descending]
    P --> Q[Select top K songs]
    Q --> R[Output recommendations]
    R --> S[End]
    


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

