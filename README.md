# Summer-2022

`GreekExercises.ipynb` contains some rough preliminary code for checking English -> Greek translations. As of right now, it can identify missing or incorrect accents and breathing marks, check the forms of each word, identify extraneous or missing words, and recognize when a word is valid Greek but does not belong in a particular sentence. Note that some edge cases are not being accounted for; for instance, if a word is both missing the correct accents and in the incorrect form, it is marked as invalid. Ideally, if this situation arises then the user should be alerted about both mistakes and the word should be marked as valid.

`HomericaQuizzes.ipynb` contains preliminary code for interactive exercises based on the [Homerica quizzes](https://github.com/gregorycrane/Homerica/tree/master/quizzes). As of now, error-checking is extremely basic (i.e. it can check accents and determine whether the input matches the specified answer exactly). Also: the regex I'm using to read each quiz question is not 100% accurate all the time, and probably needs to be tweaked a little.

`user-profile-system` is an experimental django registration app created using [this](https://dev.to/earthcomfy/creating-a-django-registration-login-app-part-i-1di5) tutorial. 
