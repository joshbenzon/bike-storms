# Tech Report (BikeStorms)

### How many data points are there in total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?

-   There are about 700 data points in total, where there are 3 features from each group: weather, bike, and taxi. There are split pretty evenly. We believe this is enough data to perform our analysis later on, as this represents a good selection of New York bike, taxi, and weather data.

### What are the identifying attributes?

-   The identifying attributes are: for weather, it's the "weatherDescription", for bikes, it's the "avgBikeDistance", and for taxis, it's the "avgTaxiDistance".

### Where is the data from?

-   This data is from the NYC Taxi and Limousine Commission (taxi), the Amazon News - CitiBike (bike), and Meteo (weather).

#### How did you collect your data?

-   We web scraped and created an API call to collect our weather data. Our other two datasets were CSV parquet files.

#### Is the source reputable?

-   This data source is pretty reputable and trustworthy. The data collected from both the NYC Taxi and Limousine Commission, Amazon News, and Meteo are reliable in terms of rough estimates our numerical data of time durations, distances, and temperature.

#### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?

-   We sampled from a New York setting and population, as this will given more data about bikes and taxis due to its popularity in usage. It's pretty large compared to other cities and places. Most of our data doesn't seem to exhibit any kind of sampling bias. However, there is a possibility that most of the data is gathered towards New York City, where most of CitiBike and taxi usage is more prevalent due to tourism.

#### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)

-   All of this data is published publicly online. Likewise, we could consider other bike and driving services as well, such as Uber, Lyft, Spin, etc.

### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

-   This data is actually pretty clean. For example, our weather data contains the most important determining factors, such as the temperature, precipitation, and a description of the whole weather. Likewise, both our bike and taxi data show a pretty decent estimate of the duration, distance, and number of trips on a specific date.

#### How did you check for the cleanliness of your data? What was your threshold reference?

-   We mostly looked at if our data set had enough data points for most (if not all) of the dates in order to look for patterns. We especially looked at general data (and even outliers) in specific date ranges, such as in the summer or winter. Some threshold references we considered was the amount of missing rows or dates that didn't have any missing or inaccurate measurements for each group.

#### Did you implement any mechanism to clean your data? If so, what did you do?

-   We made sure that if there were any duplicate dates, we removed them from all three groups, as well as any dates that contained missing data.

#### Are there missing values? Do these occur in fields that are important for your project's goals?

-   Currently, our time frame for our data is from January 2021 - November 2022. We currently don't have any data for December 2022. A few (perhaps one or two) rows that have partially missing data. To keep consistency, we filled a default value for each column feature. This doesn't occur in fields that are important.

#### Are there duplicates? Do these occur in fields that are important for your project's goals?

-   There are currently no duplicates in our data set.This doesn't occur in fields that are important.

#### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)

-   The weather data is fairly uniform in regards to the time of the month, but generally, "skewed" depending on the time of season. The bike distances are fairly uniform, centering from 1 to 3 miles. On the other hand, the taxis distances are slightly skewed towards distances from the 10 miles range with the minimum being around 2 miles and maximum around 20 miles.

#### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?

-   All of our data types are in the correct format!

#### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?

-   We do not need to throw any data away, as the date and features in weather, bike, and taxi are all important for our analysis.

### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

-   The data collection for taxis and bikes are most accessible and have the most amount and accuracy in places that are cities and higher populations, as these will more likely to use services, such as CitiBike and taxis. Hence, our next steps in our analysis will focus on the relation between all three of these groups in regards to distances and amount of usage in relation to the weather. Likewise, we also observed that certain weather descriptions seem to correlate to either low or missing data points, as there may have been a difficult time collecting this data at the time being.
