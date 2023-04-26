# Hypothesis (Double) Report (BikeStorms)

## Hypothesis #3: The total number of bike rides and taxi rides both decrease when there is rain.

### Results

-   Bike rides decreased "significantly", taxi rides did not decrease "significantly"

Bike rides in heavy rain vs. non-heavy rain:
t-statistic: -3.404155276683802
p-value: 0.0007016901668847413
Mean bike rides in heavy rain: 72337.26119402985
Mean bike rides in non-heavy rain: 83200.93274336284

Taxi rides in heavy rain vs. non-heavy rain:
t-statistic: -0.13461250781619294
p-value: 0.8929571131834464
Mean taxi rides in heavy rain: 95811
Mean taxi rides in non-heavy rain: 96140

### Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

-   We used a "two-sided t-test" from the scipy.stats module was used to evaluate whether there was a significant difference in the means of the number of bike rides and taxi rides during heavy rain and non-heavy rain. A t-test was chosen because it is a commonly used statistical test to compare the means of two groups and determine whether the difference between them is statistically significant. We did consider a "two-sided z-test," but we were not interested in the probabilities of events occuring but more so the counts. To measure success or failure, we used the p-value obtained from the t-test since it indicatse the probability of observing a difference as extreme as the one we observed by chance alone, assuming the null hypothesis that there is no significant difference in the means of bike and taxi rides during heavy rain and non-heavy rain. We didn't face any challenges since the t-test was the right choice for the hypothesis at hand. There was no need to clean or restructure the data as it was already in a suitable format for the t-test analysis. We simply separated the data into two groups: one for heavy rain and another for non-heavy rain and then calculated the mean and variance of the number of bike and taxi rides for each group before conducting the t-test.

### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

-   Based on the results of the t-tests, we can conclude that there was a significant decrease in the mean number of bike rides during heavy rain compared to non-heavy rain. However, there was no significant difference in the mean number of taxi rides during heavy rain and non-heavy rain.

Therefore, we accept the hypothesis that the total number of bike rides decreases when there is rain, but we reject the hypothesis that the total number of taxi rides decreases when there is rain.

Intuitively, the results make sense as biking in the rain can be unpleasant and potentially dangerous, whereas taking a taxi can provide a more comfortable and convenient option for transportation during rainy weather. It's important to note that the decrease in bike rides was significant but not necessarily large in absolute terms.

Overall, we are confident in the results as we conducted the t-tests carefully and they intuitively make sense.

### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?

-   They partially did. We hypothesized that the total number of bike rides and taxi rides both decrease when there is rain because rain can make it more difficult and less appealing to travel by bike or taxi. Biking in the rain can be uncomfortable and potentially hazardous due to slippery roads, and taxi rides may be more difficult to come by during rainy weather. Our results showed, however, that yes the number of bike rides do significanrtly decrease in heavy rain but the number of taxi rides do not decrease significantly.

Upon retrospection, this makes sense. People are potentially taking less bike rides in heavy rain sincew it is unpleasant and sometimes hazardous to bike in wet conditions. Taxi riders, however, are covered and shielded from the rain and regardless of weather, people always have places to go. That might contribute to the rejection of the hypothesis on the taxi rides portion.

### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

-   I believe that the tools for analysis used in this case, specifically the two-sample t-test, were appropriate for comparing the means of the two groups of data (heavy rain and non-heavy rain) and determining whether the differences observed are statistically significant. However, it's important to keep in mind that no statistical test can provide definitive answers, and there may be other factors affecting the results that were not accounted for in this analysis.

### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?

-   The data used in this analysis seems adequate for the purpose of testing the hypothesis. However, it's important to note that the data only covers a certain time period and location, so the results may not be generalizable to other locations or time periods. Additionally, there could be other factors affecting the number of bike and taxi rides that were not accounted for in this analysis, such as the availability of public transportation, outside temperature, or spikes in tourism. To remedy these issues, we could consider collecting data from multiple locations and time periods or incorporating additional variables into the analysis to better understand the factors affecting bike and taxi ride numbers during rainy weather.
