# Movie Recommendation System using Machine Learning

## Deployed in Streamlit -> (https://movies-recommender-systems.streamlit.app)


![background](https://github.com/Rhariharan08/Movie-Recommender-System/assets/171643933/aba21540-5db1-4822-aabd-3386967fac23)

## Description
This project uses machine learning models to construct a content-based movie recommendation system. Users can recommend movies to the system using their feedback. For data from 1886 to 2017, it utilizes a Kaggle dataset; for data from 2018 to 2023, it uses web scraping techniques from Wikipedia. The TMDBv3 API is used by the project to retrieve movie data and genres. Recommendations are generated using cosine similarity and Auto vectorizer from Transformers. The system is set up as an application called Streamlit.


## Introduction
The objective of this project is to create a customized movie recommendation system that improves user experience by making recommendations for films that suit user preferences and tastes. The system can make movie recommendations based on content similarity by utilizing cosine similarity and Auto vectorization.

## Dataset
**Sources**: Wikipedia (2018–2023) and Kaggle (1886–2017).
 <br />
 <br />
**Features**: Genres, movie titles, and more metadata.
 <br />
 <br />
**APIs Utilized**: TMDBv3 to retrieve movie details and genres.
 <br />

 
## Data Preprocessing

The dataset is preprocessed in multiple stages before being used for recommendation generation.

**Data collection** involves merging new data that was collected from Wikipedia with historical data from Kaggle.
 <br />
  <br />
**Genre and Details Fetching**: Obtaining comprehensive movie information via the TMDBv3 API.
 <br />
  <br />
**Text processing**: preparing and cleaning up movie synopses in order to vectorize them.
 <br />

 
## Model
The recommendation system uses a content-based filtering approach:

**Auto Vectorizer**: Converts movie descriptions into numerical vectors.
 <br />
  <br />
**Cosine Similarity**: Measures similarity between movie vectors to recommend similar movies.
 <br />

 
## Deployment
The recommendation system is deployed using Streamlit, providing an interactive interface for users to get movie recommendations.

### Key Features of the Streamlit Application
**User Input**: Users can input movie names to get recommendations.
 <br />
  <br />
**Real-time Recommendation**: Provides real-time movie suggestions based on input.
 <br />
  <br />
**User-Friendly Interface**: The Streamlit interface is designed to be intuitive and easy to use.
 <br />

 
## How to Run the Streamlit Application
To run the Streamlit application locally:

Install the required dependencies by running `pip install -r requirements.txt`.
 <br />
  <br />
Run the Streamlit application script by executing `streamlit run app.py`.
 <br />
  <br />
Access the application in your web browser at the provided local URL.
 <br />

 
## Results
The recommendation system effectively suggests movies based on user input, leveraging content similarity. The deployment on Streamlit makes it accessible and easy to use.

### Performance Metrics
The system demonstrates high performance with low error rates:

**Root Mean Squared Error (RMSE)**: 0.57
 <br />
  <br />
**Mean Squared Error (MSE)**: 0.46
 <br />

 
## Benefits


**Reliability**: The system provides accurate movie recommendations by effectively capturing content similarity.
 <br />
  <br />
**User Experience**: Enhances user experience by offering personalized recommendations.
 <br />
  <br />
**Scalability**: Capable of handling a large dataset, making it suitable for real-world applications.
 <br />
  <br />
