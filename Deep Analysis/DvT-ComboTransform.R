
# Tyler Edwards
# DvT Dataset Combo Merging
# 2 - 6 - 2021

library("readxl")
DvT = read_excel("C:/Users/Ty/Documents/~RD/DvT.xlsx", sheet = 3)

# ------------------------ P1 Combos ------------------------------------------
P1Combos = c()
P1ActCount = c()
for (i in 1:nrow(DvT))
{
  if(is.na(DvT$P1_RESULT[i])){} # Skip NAs
  else if(DvT$P1_RESULT[i] == "hit") # First row read is a hit
  {
    j = 1 # Combo counter and iteration
    combo = c(DvT$P1_ACTION[i])
    if(toString(DvT$P1_RESULT[i + j]) == "combo" || toString(DvT$P1_DESC[i + j]) == "combo") # Next action isn't NA
    {
      while(toString(DvT$P1_RESULT[i + j]) == "combo" || toString(DvT$P1_DESC[i + j]) == "combo") # Next RESULT is a combo 
      {
        combo = c(combo, DvT$P1_ACTION[i + j])
        j = j + 1
        # print(toString(DvT$P1_RESULT[i + j]))
        # print(toString(DvT$P1_DESC[i + j]))
      } 
      print(paste(combo, collapse = " | "))
      P1Combos = rbind(P1Combos, paste(combo, collapse = " | "))
      P1ActCount = rbind(P1ActCount, j)
    }
  }
}

P1Combos = as.data.frame(cbind(P1Combos, P1ActCount))
colnames(P1Combos) = c("Combo", "Actions")
P1.Combo.Count = as.data.frame(table(P1Combos$Combo))
colnames(P1.Combo.Count) = c("Combo", "Frequency")

P1Combos = merge(P1.Combo.Count, P1Combos, by = "Combo")
P1Combos = unique(P1Combos)

write.csv(P1Combos, "P1-Combos.csv", row.names = FALSE)

# ------------------------ P2 Combos ------------------------------------------
P2Combos = c()
P2ActCount = c()

for (i in 1:nrow(DvT))
{
  if(is.na(DvT$P2_RESULT[i])){} # Skip NAs
  else if(toString(DvT$P2_RESULT[i]) == "hit" | toString(DvT$P2_ACTION[i]) == "throw" & toString(DvT$P2_RESULT[i]) == "success") # Accounts for throw combos
  {
    j = 1 # Combo counter and iteration
    combo = c(DvT$P2_ACTION[i])
    if(toString(DvT$P2_RESULT[i + j]) == "combo" || toString(DvT$P2_DESC[i + j]) == "combo") # Next action isn't NA
    {
      while(toString(DvT$P2_RESULT[i + j]) == "combo" || toString(DvT$P2_DESC[i + j]) == "combo") # Next RESULT is a combo 
      {
        combo = c(combo, DvT$P2_ACTION[i + j])
        j = j + 1
        # print(toString(DvT$P2_RESULT[i + j]))
        # print(toString(DvT$P2_DESC[i + j]))
      } 
      print(paste(combo, collapse = " | "))
      P2Combos = rbind(P2Combos, paste(combo, collapse = " | "))
      P2ActCount = rbind(P2ActCount, j)
      
    }
  }
}

P2Combos = as.data.frame(cbind(P2Combos, P2ActCount))
colnames(P2Combos) = c("Combo", "Actions")
P2.Combo.Count = as.data.frame(table(P2Combos$Combo))
colnames(P2.Combo.Count) = c("Combo", "Frequency")

P2Combos = merge(P2.Combo.Count, P2Combos, by = "Combo")
P2Combos = unique(P2Combos)

write.csv(P2Combos, "P2-Combos.csv", row.names = FALSE)

