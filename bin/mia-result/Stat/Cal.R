setwd("C:/Code/MIALab_project/bin/mia-result/Stat") #set my working directory
data <- read.csv(file="Test.csv", header=TRUE)
data
data$X <- ordered(data$X,levels = c("Without PP", "With PP"))

library(dplyr)
group_by(data, X) %>%
  summarise(
    count = n(),
    mean = mean(STD, na.rm = TRUE),
    sd = sd(STD, na.rm = TRUE),
    median = median(STD, na.rm = TRUE),
    IQR = IQR(STD, na.rm = TRUE)
  )

library("ggpubr")
ggboxplot(data, x = "X", y = "STD", color = "X", palette = c("#00AFBB", "#E7B800"),order = c("Without PP", "With PP"),ylab = "Dice standart deviation", xlab = "Post-processing")

#library("ggpubr")
#ggline(data, x = "X", y = "STD", add = c("mean_se", "jitter"), order = c("Without PP", "With PP"),ylab = "Dice standart deviation", xlab = "Post-processing")

kruskal.test(STD ~ X, data = data)

wilcox.test(STD ~ X, data = data, paired = TRUE)
