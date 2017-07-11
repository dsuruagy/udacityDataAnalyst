# Remove 
rm(reddit)

# Load data
reddit <- read.csv('reddit.csv')
str(reddit)

# View factor data on a table
table(reddit$employment.status)
table(reddit$education)

# View a summary of all data
summary(reddit)

# View the levels of a factor variable
levels(reddit$age.range)
levels(reddit$income.range)

# View levels in a plot
#install.packages('ggplot2', dependencies = T)
library(ggplot2)
qplot(data=reddit, x=age.range)
qplot(data=reddit, x=income.range)

# Order the factor levels in the age.range variable in order to create
# a graph with a natural order
#?factor
reddit$age.range <- factor(x=reddit$age.range, levels=c("Under 18","18-24","25-34","35-44","45-54","55-64","65 or Above"), ordered = TRUE)

reddit$income.range <- ordered(reddit$income.range, levels= c("Under $20,000","$20,000 - $29,999","$30,000 - $39,999","$40,000 - $49,999","$50,000 - $69,999","$70,000 - $99,999","$100,000 - $149,999","$150,000 or more"))
