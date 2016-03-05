data <- read.csv("./Users/2013301000021.csv", header = T, na.strings = "")
summary(data)

getGPA <- function(df){
      df <- df[!is.na(df$Score),]
      df$g <- 1
      df[df$Score >= 60, ]$g <- 1
      df[df$Score >= 64, ]$g <- 1.5
      df[df$Score >= 68, ]$g <- 2
      df[df$Score >= 72, ]$g <- 2.3
      df[df$Score >= 75, ]$g <- 2.7
      df[df$Score >= 78, ]$g <- 3
      df[df$Score >= 82, ]$g <- 3.3
      df[df$Score >= 85, ]$g <- 3.7
      df[df$Score >= 90, ]$g <- 4
      return(df)
}

data <- data[data$Score >= 60, ]
data <- getGPA(data)
semester1 <- data[data$Year == 2013 & data$Semester == "Shang", ]
semester2 <- data[data$Year == 2013 & data$Semester == "Xia", ]
semester3 <- data[data$Year == 2014 & data$Semester == "Shang", ]
semester4 <- data[data$Year == 2014 & data$Semester == "Xia", ]
semester5 <- data[data$Year == 2015 & data$Semester == "Shang", ]

getTotalGPA <- function(df) {
      sum(df$Credit * df$g, na.rm = T) / sum(df$Credit, na.rm = T)
}

s1 <- semester1[semester1$Class == "ZhuanBi" | semester1$Class == "ZhuanXuan", ]
s2 <- semester2[semester2$Class == "ZhuanBi" | semester2$Class == "ZhuanXuan", ]
s3 <- semester3[semester3$Class == "ZhuanBi" | semester3$Class == "ZhuanXuan", ]
s4 <- semester4[semester4$Class == "ZhuanBi" | semester4$Class == "ZhuanXuan", ]
s5 <- semester5[semester5$Class == "ZhuanBi" | semester5$Class == "ZhuanXuan", ]

gpa0 <- c(getTotalGPA(semester1), getTotalGPA(semester2), getTotalGPA(semester3), getTotalGPA(semester4), getTotalGPA(semester5))
gpa1 <- c(getTotalGPA(s1), getTotalGPA(s2), getTotalGPA(s3), getTotalGPA(s4), getTotalGPA(s5))
info <- data.frame(gpa = c(gpa0, gpa1), se = rep(c(1, 2, 3, 4, 5), 2), class = factor(rep(c("Total", "Main"), each = 5)))
ggplot(data = info, aes(x = se, y = gpa, group = factor(class))) + geom_line(aes(color = factor(class)))