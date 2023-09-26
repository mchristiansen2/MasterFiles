## Madison Christiansen
## DSC520-T304 
## Week 5
## Exercise 5.2 Data Transformations


install.packages('dplyr')
install.packages("purrr")
install.packages("knitr")
library(dplyr)
library(purrr)
library(knitr)

setwd("/Users/madisonchristiansen/desktop")
housingfile <- read.csv(file='week-6-housing.csv')

str(housingfile)
ncol(housingfile)
names(housingfile)
nrow(housingfile)

## GroupBy, Summarize
group_by(housingfile, sq_ft_lot) %>% summarize(AvgPrice_size = mean(Sale.Price))
## Mutate
mutate(housingfile, Price.SqFt = Sale.Price - square_feet_total_living)
## Filter
filter(housingfile, bedrooms > 3)
## Select
select(housingfile, sq_ft_lot) # %>% summarize(mean(sq_ft_lot))
## Arrange
arrange(housingfile, Sale.Price)

## Purrr package - 2 functions. 
## Discard, Compact, zip_n, Keep
h_address = housingfile$addr_full
keep(h_address, grepl("17021 NE 113TH CT", h_address))
compact(housingfile)

## cbind
housingfile_1st = housingfile[1:5,]
housingfile_2nd = housingfile[6,]
cbind(housingfile_1st, housingfile_2nd)
## rbind
housing_1st = housingfile[1:14,]
housing_2nd = housingfile[15:26,]
rbind(housing_1st, housing_2nd)

## Split string, concatenate results 
split1 = strsplit(housingfile$addr_full, split = " ")
sapply(list(split1), paste)

knitr::stitch("DSC520_5.2_Christiansen.R")
