data <- read.csv("./Users/2013301000021.csv", header = T, na.strings = "", encoding = "GB2312")
summary(data)

getGPA <- function(df){
      df[df$Score >= 60, ]$g <- 1
      df[df$Score >= 64, ]$g <- 1.5
      df[df$Score >= 68, ]$g <- 2
      df[df$Score >= 72, ]$g <- 2.3
      df[df$Score >= 75, ]$g <- 2.7
      df[df$Score >= 78, ]$g <- 3
      df[df$Score >= 82, ]$g <- 3.3
      df[df$Score >= 85, ]$g <- 3.7
      df[df$Score >= 90, ]$g <- 4
}

data <- data[data$Score >= 60, ]
getGPA(data)
semester1 <- data[data$Year == 2013 & data$Semester == "上", ]
semester2 <- data[data$Year == 2013 & data$Semester == "下", ]
semester3 <- data[data$Year == 2014 & data$Semester == "上", ]
semester4 <- data[data$Year == 2014 & data$Semester == "下", ]
semester5 <- data[data$Year == 2015 & data$Semester == "上", ]
semester6 <- data[data$Year == 2015 & data$Semester == "下", ]

getTotalGPA <- function(df){
      df$Credit * df$g / sum(df$Credit)
}

s1 <- semester1[semester1$Class == "专业必修" | semester1$Class == "专业选修", ]
s2 <- semester2[semester2$Class == "专业必修" | semester2$Class == "专业选修", ]
s3 <- semester3[semester3$Class == "专业必修" | semester3$Class == "专业选修", ]
s4 <- semester4[semester4$Class == "专业必修" | semester4$Class == "专业选修", ]
s5 <- semester5[semester5$Class == "专业必修" | semester5$Class == "专业选修", ]
s6 <- semester6[semester6$Class == "专业必修" | semester6$Class == "专业选修", ]

gpa0 <- c(getTotalGPA(semester1), getTotalGPA(semester2), getTotalGPA(semester3), getTotalGPA(semester4), getTotalGPA(semester5), getTotalGPA(semester6))
gpa1 <- c(getTotalGPA(s1), getTotalGPA(s2), getTotalGPA(s3), getTotalGPA(s4), getTotalGPA(s5), getTotalGPA(s6))
# info <- data.frame(gpa = c(gpa0, gpa1), se = rep(c(1, 2, 3, 4, 5, 6), 2), class = factor(rep(c("Total", "Main"), nrow(data))))
# info
