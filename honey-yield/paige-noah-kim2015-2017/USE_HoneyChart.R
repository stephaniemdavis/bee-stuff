library(readxl)
library(tidyverse)
dtib <- read_xlsx("USEthis_honey_june27.xlsx")
gg <- ggplot(data = dtib,mapping = aes(x = Year, y = Weight, fill = Location)) + 
geom_col(position = "dodge") +
  labs(y = "Weight(lbs.)") +
  labs(title = "2015-2017 Honey Yields", subtitle = "Massachusetts and Top 5 Local Municipalities") +
  labs(caption = "(based on data from Buzz. Special reserves excluded.)")


