# Importing necessary libraries
library(dplyr)
library(stringr)

# Reading the data file
mental_health_data <- read.table("Data_File_csv.csv", sep=",", header = TRUE)

# Dropping column with very sparse value
mental_health_data$Tech_Role <- NULL

# Removing spaces from a column
mental_health_data$Gender <- trimws(mental_health_data$Gender)

# Modifying data in No_Employees to have mean of values of the range
mental_health_data[mental_health_data[,2] == "25-Jun",2] <- "6-25"
mental_health_data[mental_health_data[,2] == "5-Jan",2] <- "1-5"

# Converting Range values in No. of Employees in the organization to the mean of the range.
for (row in 1:nrow(mental_health_data)) {
  if (str_detect(tidyr::replace_na(mental_health_data[row,2],""),"-") == TRUE) {
    mental_health_data[row,2] = as.integer(mean(as.integer(unlist(strsplit(mental_health_data[row,2],"-")))))
  }

  if (tidyr::replace_na(mental_health_data[row,2],"") == "More than 1000") {
    mental_health_data[row,2] = as.integer(1000)
  }

}
mental_health_data$No_Employees <- as.integer(mental_health_data$No_Employees)

# Converting all blank strings to NA
mental_health_data <- mutate_all(mental_health_data, list(~na_if(.,"")))
mental_health_data <- mutate_all(mental_health_data, list(~na_if(.,"NULL")))


## Converting target column "May be" to "Yes" to perform a logistic regression
## Converting Yes to 1 and No to 0
mental_health_data$Current_Mental_Illness <- as.character(mental_health_data$Current_Mental_Illness)
mental_health_data[mental_health_data$Current_Mental_Illness == 'Maybe',28] <- 1
mental_health_data[mental_health_data$Current_Mental_Illness == 'Yes',28] <- 1
mental_health_data[mental_health_data$Current_Mental_Illness == 'No',28] <- 0

mental_health_data$Current_Mental_Illness <- as.factor(mental_health_data$Current_Mental_Illness)

# Converting categorical columns to factors
mental_health_data[,1] = as.factor(mental_health_data[,1])
mental_health_data[,3:15] = lapply(mental_health_data[,3:15], as.factor)
mental_health_data[,16:27] = lapply(mental_health_data[,16:27], as.factor)
mental_health_data[,29] = as.factor(mental_health_data[,29])
mental_health_data[,30] = as.factor(mental_health_data[,30])
mental_health_data[,31:32] = lapply(mental_health_data[,31:32], as.factor)
mental_health_data[,34:36] = lapply(mental_health_data[,34:36], as.factor)

# Viewing the columns and their types
str(mental_health_data)

# Imputing NA data with values for integer/categorical columns
library(mice)
data_imputed <- mice(mental_health_data)

mental_health_imputed_data <- complete(data_imputed)

# Viweing the data after cleansing.
nrow(mental_health_imputed_data)
nrow(mental_health_data)

str(mental_health_imputed_data)


###########################################################################################################
## Modelling "Current Mental Illness" as target variable
## Fitting a Logistic Regression Model on all factors
all_data_model <- mental_health_imputed_data[,-35]

glm_all <- glm(Current_Mental_Illness ~ . , family = binomial(link="logit"), data = all_data_model);
summary(glm_all);

## Fitting only significant features after stepwise selection of significant factors
model_data <- mental_health_imputed_data[,c(28,5,10,27,29,31,32,33,20)]
glm1 <- glm(Current_Mental_Illness ~ . , family = binomial(link="logit"), data = model_data);
summary(glm1)


###########################################################################################################
## Modelling "Treatment_from_Mental_health_professional" as target variable

## Fitting a Logistic Regression Model on all factors
glm2 <- glm(Treatment_from_Mental_health_professional ~ . , family = binomial(link="logit"), data = model_data2);
summary(glm2);


## Model after stepwise selection of significant factors
model2 <- mental_health_imputed_data[,c(6,9,18,20,27,29,31,30)]
glm2 <- glm(Treatment_from_Mental_health_professional ~. , family=binomial(link="logit"), data=model2)
summary(glm2)
