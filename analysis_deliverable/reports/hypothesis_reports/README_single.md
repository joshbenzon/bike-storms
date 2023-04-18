# Hypothesis (Single) Report (BikeStorms)

## Hypothesis #1: If the weather description shows "heavy rain", the average bike ride distance will decrease.

### Results

-   Data Length of Distance with Rain: 134
-   Average of Distance with Rain: 1.8142546459449929

-   Data Length of Distance with No Rain: 565
-   Average of Distance with No Rain: 1.8399409586695346

-   Decreased!

-   T-Stat: -1.8010274810380886
-   P-Value: 0.07213067348930136

### Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

-   We used a "one-sided t-test," because we only have one sample to compare to (average bike distance). We did consider a "one-sided z-test," but our data isn't the whole population but rather a sample of the bike data. There wasn't any metrics to measure success/failure. We did not have any challenges nor did we have to clean our data.

### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

-   Ho (Null Hypothesis): There is no significant difference in the average bike distance when the weather description is "Heavy Rain" compared to when it's not.
-   Ha (Alternative Hypothesis): There is a significant difference in average bike distance when the weather description is "Heavy Rain" compared to when it's not.

-   Since the p-value is higher than 0.05 (5%), we fail to reject the null hypothesis, and cannot accept the alternate hypothesis. There does not seem to be a significant difference in the average bike distance when the weather description is "Heavy Rain" compared to when it's not.
-   The results make sense, and we're pretty confident on them based on the data sample size!

### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?

-   Yes! While the difference between the two average bike distances weren't statistically significant, it was fairly close. When there's rain, people would ride bikes less farther in order to not be wet. So, it makes sense that the average bike distances decreased when it rained.

### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

-   Yes! Since we're only comparing one variable (average bike distance) compared to one weather description ("Heavy Rain") from a sample, the "one-sided t-test" is appropriate. I don't think any other method could have been used, since the data is only numerical (and not categorical).

### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?

-   The data was pretty accurate for the analysis! Since we gathered the average bike distance from each data point and classified the weather description into four categories, it was adequate classification. Likewise, one aspect of the data that was problematic was that in our dataset, if there was only one small part of the data (or 1 hour of the day) that was raining, snowing, etc. the entire weather description would be labeled as that label. One remedy is to possible split the data into different time slots (or hour slots) and then analyze the average bike distances within the time slots.

## Hypothesis #2: If the weather description shows "clear", the average taxi ride duration will increase.

### Results

-   Data Length of Duration with Clear: 354
-   Average of Duration with Clear: 999

-   Data Length of Duration with No Clear: 345
-   Average of Duration with No Clear: 992

-   Increased!

-   T-Stat: 0.9954910943369788
-   P-Value: 0.3198429413678037

### Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?

-   We used a "one-sided t-test," because we only have one sample to compare to (average taxi duration). We did consider a "one-sided z-test," but our data isn't the whole population but rather a sample of the taxi data. There wasn't any metrics to measure success/failure. We did not have any challenges nor did we have to clean our data.

### What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

-   Ho (Null Hypothesis): There is no significant difference in the average taxi duration when the weather description is "Clear" compared to when it's not.
-   Ha (Alternative Hypothesis): There is a significant difference in the average taxi duration when the weather description is "Clear" compared to when it's not.

-   Since the p-value is higher than 0.05 (5%), we fail to reject the null hypothesis, and cannot accept the alternate hypothesis. There does not seem to be a significant difference in the average taxi duration when the weather description is "Clear" compared to when it's not.
-   The results make sense, and we're pretty confident on them based on the data sample size!

### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?

-   Yes! The difference between the two average bike distances weren't statistically significant. When the weather is clear, people would ride taxis more, because it would be easier to ride a car when there's no rain or it's not snowing (or be less prone to a car accident).

### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

-   Yes! Since we're only comparing one variable (average taxi duration) from a sample compared to one weather description ("Clear"), the "one-sided t-test" is appropriate. I don't think any other method could have been used, since the data is only numerical (and not categorical).

### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?

-   The data was pretty accurate for the analysis! Since we gathered the average taxi duration from each data point and classified the weather description into four categories, it was adequate classification. Likewise, one aspect of the data that was problematic was that in our dataset, if there was only one small part of the data (or 1 hour of the day) that was raining, snowing, etc. the entire weather description would be labeled as that label. One remedy is to possible split the data into different time slots (or hour slots) and then analyze the average taxi duration within the time slots.
