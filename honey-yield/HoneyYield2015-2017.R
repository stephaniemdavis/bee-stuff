library(tidyverse)
library(plyr)
library(readxl)
library(jsonlite)
noah_bar <- read_xlsx('jun-24.xlsx')
head(noah_bar)

# Chart Weight by Year using geom_col
ggplot(data = noah_bar,mapping = aes(x = Year, y = Weight )) + geom_col()
  
# How do I plot each year's weight total by the top 5 locations? i.e. The
# locations comprising the 5 highest weight totals for each year. For example,
# in 2015: Massachuetts aggregate honey harvest was 4014 lbs, 
# and Boston - 944 lbs., Cape Cod - 472 lbs., Duxbury - 328 lbs.,
# Medfield - 253 lbs., Cambridge - 204 lbs. were the top 5 2015 local producers

# SERENDIPITY - added the color aes and mapped Location variable to it.
# Not what I want but it's a start
ggplot(data = noah_bar,mapping = aes(x = Year, y = Weight )) + geom_col(mapping = aes(color = Location))

