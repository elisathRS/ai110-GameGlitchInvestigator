# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
  The first time I run the game, it showed a number guessing game where the player guesses a number between 1 and 100 . It included an input box for guesses, buttons to submit or start a new game,   and    a debug section showing details like the secret number, attempts, and score.
  
- List at least two concrete bugs you noticed at the start
     1. The first time I played, I guessed the number 30, and the game told me to go lower even though the correct number was 51. I expected the game to tell me to go higher.
     2. Hard mode seems easier than Normal mode. When I set the difficulty to Normal, the range was from 1 to 100. However, when I switched to Hard, the range changed to 1 to 50, which actually makes           the game easier.
     3. Starting a new game resets the attempts to 0, but the initial session state sets the attempts to 1.

        
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  Claude and Copilot
  
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I ensured that my code passed all the tests in the provided test file, while also running it live and walking through the happy path to verify whether the issue was fixed or still recurring. Passing    the tests confirmed that my code handles the happy path correctly.
  
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  The issue happened because Streamlit reruns the whole script whenever the user interacts with the app. Without storing the value in st.session_state, the secret number was recreated each time     the script ran.
  
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit reruns the whole app every time you interact with it, like replaying a story from the start. Session state is like the history of what already happened in the story—it remembers your     past actions, scores, or guesses so the app doesn’t forget them when it reruns.
  
- What change did you make that finally gave the game a stable secret number?
  
  The fix that finally kept the secret number stable was saving it in st.session_state and generating it only once when the game begins or when the difficulty changes.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    
    One habit I would like to keep is developing focused test cases for particular bugs. Doing this helped me make sure my solutions worked and avoided future errors.
    
- What is one thing you would do differently next time you work with AI on a coding task?

  The next time I collaborate with AI on a coding project, I will take extra time to analyze its recommendations before using them. Even though AI is helpful, some of its suggestions may be       repetitive or unnecessary.
  
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project helped me see AI-generated code differently. I realized that while AI can be very useful for debugging, it’s still up to me to fully understand the code and confirm that it satisfies the project requirements.
