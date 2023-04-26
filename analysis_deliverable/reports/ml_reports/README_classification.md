# Machine Learning (Classification: K-Nearest Neighbor) Report (BikeStorms)

## Model #2:

### Results

-   Training Set Accuracy: 0.586
-   Testing Set Accuracy: 0.479

-   To find the optimal K value for my K-Nearest Neighbor analysis, I trained my KNN model with various k values and plotted the training and validation accuracies. From that plot, I saw that a k value of 7 gave the highest validation accuracy.
-   I then I re-trained my KNN model with k = 7 and got an accuracy of about 0.59 for the training set and an accuracy of about 0.48 for the testing set.
-   These accuracies fall below 70%-90% range, which sugguests that the average duration, average distance, and total number of CitiBike trips are not sufficient metrics predict the weather on a given day.

### Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

-   I wanted to predict the weather on a given day in New York City from the average duration, distance, and number of CitiBike trips on that day. Since this is a classification task involving categorical labels, I knew that using a supervised machine learning algorithm would be suitable for this task. I decided to implement K-Nearest Neighbors; however, other supervised learning techiques could have worked such as suport vector machines or decision trees.
-   After finding the optimal k value of 7, I used the training set accuracy and testing set accuracy to measure the success of my analysis.
-   From our final cleaned data set, I took the columns 'avgBikeDuration', 'avgBikeDistance', and 'totalBikeTrips' for the x or independent values. I also took the 'weatherDescription' column and used one-hot encoding to generate the y values or labels. Becaused we missed a couple of Nan values in the 'avgBikeDuration' column, I needed to remove those rows before compeleting the classification task.

### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

-   The training accuracy of 0.59 and testing accuracy of 0.48 suggests that the weather on a given day in New York City cannot not be accurately predicted from the average duration, average distance, and total number of CitiBike trips on that day.
-   We had 4 weather labels corresponding to Heavy Rain, Light Rain, Clear, and Snowing. Since these categories are extremely broad and only relate to precipitation conditions, I understand why it would be difficult to predict these labels from 3 metrics alone (average duration, average distance, total number of trips). To improve our classification model, we needed to use more than 3 metrics to predict the weather description.

### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?

-   The results did not correspond with my initial belief that the weather would impact the number of people who chose to ride CitiBikes, how far they would ride, and for how long. I incorrectly thought that these metrics would be enough to then predict the weather on a given day.

### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

-   In general, we used the correct classification algorithm for the task; however, we did not have sufficient data for the K-Nearest Neighbor model to produce meaningful results.

### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?

-   I think we could have obtained more accurate classifications with more data. We only retrieved CitiBike data from the past two years, but several more years worth of data is available.
