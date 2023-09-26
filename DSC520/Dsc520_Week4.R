## Madison Christiansen
## DSC520-T304 
## Week 4  
## Exercise 4.2 

install.packages("dplyr")
install.packages("tidy")
install.packages("ggplot2")
library(ggplot2)
library(dplyr)
library(tidyverse)tidyc

## retrieve and read file
setwd("/Users/madisonchristiansen/desktop")
getwd()
scoresdoc = read.csv("scores.csv")

## observational units in this study
str(scoresdoc)
nrow(scoresdoc)
ncol(scoresdoc)
names(scoresdoc)

## categorical= Section variables
## quantitative= Count, Score variables

## subset of data containing regular section
regsec = subset(scoresdoc, Section=="Regular")
## subset of data containing sports section
sportsec = subset(scoresdoc, Section=="Sports")

## plot each sections scores
plot(sporsec$Score, sporsec$Count, main = "Sports Section", xlab = "Score", ylab = "Count of Students", col="red")
plot(regsec$Score, regsec$Count, main = "Regular Section", xlab = "Score", ylab = "Count of Students", col="black")

## plot together
plot(sporsec$Score, sporsec$Count, main = "Sports vs Regular", xlab = "Score", ylab = "Count of Students", col="red")
points(regsec$Score, regsec$Count, col = "black")
mtext(paste(" Black - Regular \nRed - Sports"), side= 3, line =-2, adj=0)

