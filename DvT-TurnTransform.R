
# Tyler Edwards
# DvT Dataset Turn Transformation
# 3 - 3 - 2021
# Identifies turns gained and lost after blocks in the action data


library("readxl")
library("xlsx")

DvT = read_excel("../DvT.xlsx", sheet = 3)

# ------------------------ P1 Turns ------------------------------------------
P1Turns = c()

for (i in 1:nrow(DvT)) # Parse rows
{
  if(is.na(DvT$P1_ACTION[i])){} # Skip NAs
  else if(toString(DvT$P1_RESULT[i]) == "c.block" 
          || toString(DvT$P1_RESULT[i]) == "s.block") # Looking for blocks instead of hit
  {
    P1Action = c(DvT$P1_ACTION[i])
    if(!is.na(DvT$P1_ACTION[i + 1])) # Next action isn't NA
    {
      #if(DvT$P1_ACTION[i + 2] ==)
      P1Action = c(P1Action, DvT$P1_ACTION[i+1], "Won")
    }
    else # Player doesn't have next action
    {
      P1Action = c(P1Action, "", "Lost")
    }
    P1Turns = rbind(P1Turns, P1Action)
  }
}

P1Turn.Final = as.matrix.data.frame(table(P1Turns[,1], P1Turns[,3]), rownames.force = TRUE)
colnames(P1Turn.Final) = c("Lost", "Won")
