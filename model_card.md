# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
**VibeMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  
This recommender suggests songs based on a user’s preferred genre, mood, and energy level. It assumes that users know their preferences and want songs with similar characteristics. This system is designed for classroom exploration, not for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.
The model uses features like genre, mood, and energy from each song. It compares these with the user’s preferences. If the genre matches, it adds 2 points, and if the mood matches, it adds 1 point. It also calculates how close the song’s energy is to the user’s preferred energy. All these values are combined to create a score, and songs with the highest scores are recommended.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  
The dataset contains 18 songs from songs.csv. Each song includes features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset includes a limited range of genres and moods, so it does not represent all types of music. Some user preferences may not be well covered.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  
The system works well for users whose preferences match the available data, such as Lofi Chill users. It correctly prioritizes songs that match both genre and mood. The scoring system is simple and easy to understand, which makes the recommendations transparent.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The recommender system has a limitation because it relies heavily on genre and energy similarity. During the experiment, when the mood feature was removed, the recommendations became less accurate and were mostly based on energy alone.

This creates a bias where songs with similar energy are recommended even if they do not match the user’s mood or genre preference. As a result, the system may ignore important aspects of user taste, leading to less personalized recommendations.

Additionally, the small dataset limits diversity, which can cause the same songs to appear frequently for different users.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested the recommender system using multiple user profiles, including Lofi Chill, High Energy Pop, Sad Rock, and an edge case with unusual preferences. I looked at the top recommended songs and checked whether they matched the user’s genre, mood, and energy preferences.

For the Lofi Chill user, the results felt accurate because the top songs matched both genre and mood, and had similar energy levels. However, for other users, many recommendations were based mostly on energy similarity, which made them feel less personalized.

One surprising result was that some songs kept appearing for different users, even when their preferences were very different. This happened because the system relies heavily on energy similarity, especially when genre and mood do not match.

Overall, the system works well when there are strong matches in genre and mood, but performs worse when those features do not align.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  
I would improve the model by adding more songs to increase diversity. I would also include more features like tempo and valence in the scoring. Additionally, I would try to balance the recommendations so the same songs do not appear for different users.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
My biggest learning moment in this project was understanding how simple scoring rules can still create meaningful recommendations. Even though the algorithm is basic, it was able to suggest songs that felt relevant when the user preferences matched well.
Using AI tools like Copilot helped me write and modify code faster, especially when implementing and testing changes. However, I had to double-check the results to make sure the logic was correct and matched the assignment requirements.
One thing that surprised me was how simple algorithms can still “feel” like real recommendations. Even with just genre, mood, and energy, the system could produce reasonable suggestions.
If I continued this project, I would improve it by adding more features and a larger dataset, and by making the recommendations more diverse so the same songs do not appear repeatedly.