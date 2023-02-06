# Love Island project

## Justification
  Suicide became one of the most important preventable causes of death in between the population from the developed countries, being even the number one for countries like Spain.
    
   One of the main causes can be related with the stereotypes sold by the media which influence straightforward to the self-esteem of people, by implementing models and standards far from reality, provoking negative influence on the individual.
    
   According to this, we can find examples in the United Kingdom where, for example, in 1999, a popular tv show showed a suicidal attempt. A week after, it was found an increased of the 17% on suicidal attemps. 
   [reference](http://www.mediawise.org.uk/wp-content/uploads/2011/03/Los-Medios-de-Communicacion-y-el-Suicidio.pdf)

    
   For this reason our project is focused to analyse the influence of a TV program like Love Island makes over the adolescents/young adults range in terms of self-esteem and, in the lastest, on de influence of any suicidal conduct triggered by this TV Show.
    
   Love Island is a reality show which has been focused due to unhealthy behaviors in relationships and how it influence on their spectators (mainly women between 16–34 years old); for this reason, we analysed the hypotesis of being even an trigger from the suicidal point of view.
[reference_2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8022790/)


## Methods

   In order to analyse if there's a cause-effect relation in between this TV show and the increase of the suicidal attemps we collected data through kaggle.com from the WHO about the suicidal registration in between 2005 to 2019.
   
   Because the TV program it was produced in the United Kingdom, the main filter applied was to collect the data on those years from UK. After more clearance of columns and null values, we ended it up with the following columns : 
![column_1](/pics/data_frame_uk.png)
   
   On the other side, to be able to check the cause/effect of our hypothesis, It's been done some webscrapping from their producers website to get a new dataframe with the episodes, years, season and months. The idea to relate both data frames is to see if,as more episodes are produced, more suicidal attemps happened.
   
   
## Results
As a result of the research we can observe in general a tendency to increase the number of suicides in the United Kingdom. More specific to the range of ages mentioned before it's been a steady increse of numbers until 2017 were the inclination got increase.

![suicide no by ages](/pics/age_suic.jpg)

We can relate this increase with the increase of number of episodes of Love Island as seen below; during 2015 there were produced around 35 episodes, while, in 2019 it increased to around 58.

![love island episodes](/pics/epis_years.jpg)

Finally, when we put all the results together we found relevant info: the first one is the peak of suicide numbers in 2018 matching with the highest amount of episodes produced; on the other side, we can see in 2019 with the same amount of episodes, the numbers reduce to half.

![suicide vs episodes](/pics/su_ep.jpg)

## Conclusions

After analysing the data available, we could find somehow of relation in between the increase of episodes of Love Island with the increase of number of suicides, instead, we found results which contradics this hypothesis, so, it brings us to the point where makes us think if the number of suicide decreased in 2019 as a resilience ability in between this population or, simply, there's no correlation.
