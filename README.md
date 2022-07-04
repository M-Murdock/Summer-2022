# Summer-2022

---

### /

`GreekExercises.ipynb` contains some rough preliminary code for checking English -> Greek translations. As of right now, it can identify missing or incorrect accents and breathing marks, check the forms of each word, identify extraneous or missing words, and recognize when a word is valid Greek but does not belong in a particular sentence. Note that some edge cases are not being accounted for; for instance, if a word is both missing the correct accents and in the incorrect form, it is marked as invalid. Ideally, if this situation arises then the user should be alerted about both mistakes and the word should be marked as valid.

`HomericaQuizzes.ipynb` contains preliminary code for interactive exercises based on the [Homerica quizzes](https://github.com/gregorycrane/Homerica/tree/master/quizzes). As of now, error-checking is extremely basic (i.e. it can check accents and determine whether the input matches the specified answer exactly). Also: the regex I'm using to read each quiz question is not 100% accurate all the time, and probably needs to be tweaked a little.

`MultipleChoice.ipynb` is an experimentation with a couple of things: 
1. Using [Stanza](https://stanfordnlp.github.io/stanza/index.html) to create multiple-choice questions about the structure of a given sentence. Just as with `HomericaQuizzes.ipynb`, questions are drawn from `lib/quiz_questions.txt`. 
2. Generating a list of words with possible and impossible accents. The user is then asked to identify the words with impossible accents. This utilizes modules from [greek-accentuation](https://github.com/jtauber/greek-accentuation).
3. Using [greek-accentuation](https://github.com/jtauber/greek-accentuation) to break a word into syllables, ask the user to identify the antepenult, penult, or ultima of the word
4. Drill accent rules by asking the user to identify possible legal locations of a given accent
5. A single word is randomly chosen, along with several possible and impossible accentuations of that word. The user is then asked to identify all the possible accentuations.

---

### user-profile-system/

`user-profile-system` is an experimental django registration app created using [this](https://dev.to/earthcomfy/creating-a-django-registration-login-app-part-i-1di5) tutorial. Run `user-profile-system/user-profile.ipynb` to start up the web app.

---

### lib/

`quiz_questions.txt` contains a set of Greek sentences and their translations, drawn from `a_hs.txt`

`a_hs.txt` is a set of quiz questions based on the [Homerica quizzes](https://github.com/gregorycrane/Homerica/tree/master/quizzes). 

`CrosbyShaefferSentences - Lesson 1.tsv` contains the questions and answers from Crosby and Shaeffer Lesson 1

`tlg0012-tbankplus.txt` and `tlg0012.tlg001.perseus-grc1.tb.xml` are treebanks of the first book of the Iliad

`verbs.tsv` and `paradigms.tsv` are [lists of forms](https://github.com/jtauber/greek-inflexion/tree/master/homer-data) from Pharr's Homeric Greek

