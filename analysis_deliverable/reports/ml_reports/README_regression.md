# Machine Learning (Regression) Report (BikeStorms)

## Model #1:

### Results

-   Temperature and Taxi Duration are positively correlated.

### Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

-   I theorized that higher temperatures in the summertime would lead to people taking longer taxi rides. However, I thought colder temperatures would lead to people taking longer taxi rides. Thus, I originally intended on doing some kind of polynomial fit. I was surprised that in an initial visualization where I just plotted the data as a scatterplot, the data appeared to be fairly linear. The best model for this thus turned out to be a linear regression ML model. It yielded a testing R^2 value of .18 and a training R^2 value of .20. I feel like these are pretty good results.
I did not need to clean or restructure the data beyond just extracting the two columns I wanted to compare.


### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

-   I accept the results. I thus think that this model can make a rough guess of the taxi duration based on an input temperature. In other words, I believe that colder temperatures lead to shorter trips and warmer temperatures lead to longer trips. The summer is full of trips to the beach and the winter people are simply hibernating. I don’t know if I have full confidence in the results because of only getting a R^2 value of 0.2 roughly. I am torn though, because a cursory look at avgTemp vs totalTaxiTrips also indicates the same pattern. Cold weather means shorter and less taxi trips. Warm weather means longer and more taxi trips. This runs a bit counter to what my intuition would have guessed but seems totally justifiable.

### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?

-   No, I expanded on this above.

### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

-   Yes. The data visualization suggests that a linear model is a logical choice.

### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?

-   I wish I had even more data - I could have scraped 5 years of taxi and weather data.
