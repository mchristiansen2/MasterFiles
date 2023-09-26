## Madison Christiansen
## DSC520-T304 
## Week 3  
## Exercise 3.2 2014 American Community Survey

install.packages("ggplot2")
install.packages("readxl")
install.packages("pastecs")
library(ggplot2)
library(readxl)
library(tidyverse)
library(pastecs)

## load the data file
setwd("/Users/madisonchristiansen/desktop")
getwd()
acsdoc = read.csv("2014ACS.csv")

## ID: Variable Character, unique identifier
## ID2: Variable Character, same identifier not including the starting '0500000US0'
## Geography: String, location of the individual
## PopGroupID: Integer, unique identifier based on the geography
## POPGROUP.display-label: String, label for the population
## RacesReported: Integer, the number of races in the location
## HSDegree: Integer, the number of individuals with a HS degree in the location
## BachDegree: Integer, the number of individuals with a bachelors degree in the location

## following function outputs
str(acsdoc)
nrow(acsdoc)
ncol(acsdoc)
names(acsdoc)

## creating a histogram of the 'HSDegree' variable
ggplot(acsdoc, aes(HSDegree))+ geom_histogram(bins = 50) +  ggtitle("HSDegree - 2014 American Community Survey") + ylab("Frequency") + xlab("% of People Who Have a High School Degree")
## adding a normal curve
ggplot(data = acsdoc) + 
  geom_histogram(mapping = aes(x = HSDegree, y=..density..), binwidth = 1,bins = 50) + ggtitle("HSDegree - 2014 American Community Survey") + ylab("Frequency") + xlab("% of People Who Have a High School Degree") +
  stat_function(fun = dnorm, colour = "pink", args = list(mean = mean(acsdoc$HSDegree), sd = sd(acsdoc$HSDegree)))

## probability plot of HSDegree
ggplot(acsdoc, aes(sample = HSDegree)) + stat_qq(col = 'green') + stat_qq_line() + ggtitle("HSDegree - 2014 American Community Survey") 

## look at data for normality
stat.desc(acsdoc$HSDegree, basic=FALSE, norm=TRUE)



