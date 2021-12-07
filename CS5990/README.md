# Movie Likelihood Based on Movie Review
Python based Machine Learning Model to know if a Movie will be Liked Highly or Low based on its Review.

+ 'clean_data.py' Removes Noise from Provided Input like :
	- HTML Tags
	- Special Characters
	- Accented Chracters
	- English Stop Words
	- Gets Words to their Base Form (Lemmatisation)

+ 'create_cleaned_data.py' Implements Functionalities from 'clean_data.py' on Entire Original Dataset to create a Cleaned Dataset.

+ 'text_formatting.py' Provides 2 Functionalities :
	- Implements 'clean_data.py' functionalities on Provided Input.
	- Formats Provided Input into ML Model Acceptable Format.

+ 'train_model.py' Trains ML Model and Exports Trained ML Model.
