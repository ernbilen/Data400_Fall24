#read in data
co2emis <- read.csv("/Users/magsb/Downloads/per-capita-co2-sector.csv")
asthma <- read.csv("/Users/magsb/Documents/Downloads/county_asthma.csv")
miles <- read.csv("/Users/magsb/Downloads/miles.csv")

#packages
library(ggplot2)
library(tidyverse)
library(gridExtra)
library(reshape2)

#add data column to asthma dataframe
asthma$per_diag <- 
  c(8.61, 7.94, 7.99, 6.15, 6.01, 8.98, 17.27, 8.97, 10.33)

#EDA
co2emis |> 
  ggplot(aes(x = Year, y = manufacturing.and.construction, color = "blue")) + 
  geom_point()

co2emis |> 
  ggplot(aes(x = Year, y = energy.production, color = "green")) + 
  geom_point()



plot3 <- asthma |> 
  ggplot(aes(x = County, y = conventional_wells+unconventional_wells, fill = County)) +
  geom_col() +
  labs(
    y = "Number of Wells",
    title = "Number of Unconventional and Conventional Wells"
  ) + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  scale_fill_brewer(palette="Paired") + 
  theme(legend.position = "none")
plot3
  
plot2 <- asthma |> 
  ggplot(aes(x= County, y = Asthma_hosp, fill = County)) + 
  geom_col() +
  labs(
    y = "Hospitalization Rate",
    title = "Hospitalization Rate for Childhood Asthma",
    caption = "Number of children hospitalized per 100,000"
  ) + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  scale_fill_brewer(palette="Paired") + 
  theme(legend.position = "none")
plot2

plot1 <- miles |> 
  ggplot(aes(x = County, y = truck_dvmt, fill = County )) + 
  geom_col() +
  labs(y = "Daily Vehicular Miles Traveled", 
       title = "Truck only DVMT per County")+ 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  scale_fill_brewer(palette="Paired") + 
  theme(legend.position = "none")
plot1



grid.arrange(plot1, plot2, plot3, ncol=3)



trucks <- miles |> 
  ggplot(aes(x = County, y = truck_dvmt, fill = County )) + 
  geom_col() +
  labs(y = "Daily Vehicular Miles Traveled for Trucks", 
       title = "Truck DVMT per county")+ 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

trucks



df2 <- melt(asthma, id.vars='County')
df2 <- df2 |> filter(variable == "Asthma_hosp" | variable == "per_diag")
head(df2)

ggplot(df2, aes(x=County, y=value, fill=variable)) +
  geom_bar(stat='identity', position='dodge') + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

plot4 <- asthma |> 
  ggplot(aes(x= County, y = per_diag, fill = County)) + 
  geom_col() +
  labs(
    y = "Percent Diagnosed",
    title = "Percent of K-12 Students Diagnosed with Asthma"
  ) + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
  scale_fill_brewer(palette="Paired") + 
  theme(legend.position = "none")
plot4