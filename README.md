# Movies Sentiment Analysis

The Movie Sentiment Analysis project aims to analyze user sentiments or opinions about movies based on a dataset obtained from Kaggle. This dataset consists of a collection of user reviews about various films, which are associated with positive or negative sentiment labels.

In this project, I will use sentiment analysis techniques to classify movie reviews as positive or negative. The main goal of sentiment analysis is to understand the opinions, feelings, or responses contained within user reviews. 

Thus, this project will provide insights into the comparison between the Scikit-Learn Random Forest and the CuML Random Forest algorithms within the context of a sentiment analysis project.


## Dataset
Dataset: https://www.kaggle.com/datasets/yasserh/imdb-movie-ratings-sentiment-analysis

Target: 0 - Negative, 1 - Positive

## Results
Based on the evaluation metrics, the results of the classification performance for the Random Forest algorithm are as follows.

|        | Scikit-Learn RFC        | CuML RFC        |
|--------|-------------|--------|
| Prec   | 0.8185 | 0.8117 | 
| Rec    | 0.8185 | 0.81  | 
| F1     | 0.8184 | 0.8098 | 
| Running Time     | 15.48 s | 1.41 s |

## Conclusion
The classification performance results indicate that both Scikit-Learn and CuML achieved similar precision and recall scores, with Scikit-Learn slightly outperforming CuML in these metrics. However, CuML demonstrated a significantly faster running time, completing the task in just 1.41 seconds compared to Scikit-Learn's 15.48 seconds.

In summary, while Scikit-Learn offers marginally better accuracy, CuML provides a much more efficient solution in terms of speed, making it a compelling choice for applications where time is critical.