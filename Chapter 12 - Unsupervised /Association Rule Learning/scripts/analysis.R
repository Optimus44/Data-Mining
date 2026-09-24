# =============================================================================
# analysis.R
# Association Rule Learning on the Groceries Dataset
# Unsupervised Learning Method — Assignment: Association Rule Learning
# =============================================================================
#
# Requires the `arules` package. Install once with:
#   install.packages("arules")
#
# Run from the project root:
#   Rscript scripts/analysis.R
#
# Outputs (written to results/):
#   top10_items.csv, top10_items.png
#   frequent_itemsets.csv
#   association_rules.csv
#   top_rules_by_metric.csv
#   rules_scatter.png
# =============================================================================

library(arules)

set.seed(1)
dir.create("results", showWarnings = FALSE)

# ---- Q1: Load and explore the data --------------------------------------
trans <- read.transactions(
  "data/groceries.csv",
  format = "basket",
  sep = ","
)

n_transactions <- length(trans)
n_items        <- ncol(trans)

cat("Number of transactions:", n_transactions, "\n")
cat("Number of unique items:", n_items, "\n")

item_freq <- sort(itemFrequency(trans, type = "relative"), decreasing = TRUE)
top10 <- head(item_freq, 10)

write.csv(
  data.frame(item = names(top10),
             support = as.numeric(top10),
             count = round(as.numeric(top10) * n_transactions)),
  "results/top10_items.csv", row.names = FALSE
)

png("results/top10_items.png", width = 1000, height = 600, res = 120)
par(mar = c(4, 9, 3, 1))
itemFrequencyPlot(trans, topN = 10, type = "relative", horiz = TRUE, las = 1,
                   col = "#3E7CB1",
                   main = "Top 10 Most Frequent Items - Groceries Dataset")
dev.off()

# ---- Q2: Frequent itemsets (>= 2 items) ----------------------------------
MIN_SUPPORT  <- 0.02
MIN_CONFIDENCE <- 0.25

itemsets <- apriori(
  trans,
  parameter = list(support = MIN_SUPPORT, minlen = 2, target = "frequent itemsets")
)
itemsets <- sort(itemsets, by = "support")

itemsets_df <- data.frame(
  itemset = labels(itemsets),
  support = quality(itemsets)$support,
  count   = quality(itemsets)$count
)
write.csv(itemsets_df, "results/frequent_itemsets.csv", row.names = FALSE)
cat("Frequent itemsets (size >= 2, support >=", MIN_SUPPORT, "):", nrow(itemsets_df), "\n")

# ---- Q3: Association rules -------------------------------------------------
rules <- apriori(
  trans,
  parameter = list(support = MIN_SUPPORT, confidence = MIN_CONFIDENCE, minlen = 2)
)
rules <- sort(rules, by = "lift")

rules_df <- data.frame(
  antecedent = labels(lhs(rules)),
  consequent = labels(rhs(rules)),
  support    = quality(rules)$support,
  confidence = quality(rules)$confidence,
  lift       = quality(rules)$lift
)
write.csv(rules_df, "results/association_rules.csv", row.names = FALSE)
cat("Association rules (support >=", MIN_SUPPORT, ", confidence >=", MIN_CONFIDENCE, "):",
    nrow(rules_df), "\n")

# ---- Q5: Highest confidence / lift / support rules -------------------------
top_conf <- rules_df[which.max(rules_df$confidence), ]
top_lift <- rules_df[which.max(rules_df$lift), ]
top_supp <- rules_df[which.max(rules_df$support), ]

write.csv(
  rbind(
    data.frame(metric = "confidence", top_conf),
    data.frame(metric = "lift", top_lift),
    data.frame(metric = "support", top_supp)
  ),
  "results/top_rules_by_metric.csv", row.names = FALSE
)

# ---- Supporting plot: support vs confidence, coloured by lift -------------
# (Base R only, so this doesn't add an arulesViz dependency on top of arules.)
png("results/rules_scatter.png", width = 900, height = 700, res = 120)
cols <- colorRampPalette(c("#B7D3E8", "#08306B"))(100)
col_idx <- pmin(100, pmax(1, round((rules_df$lift - min(rules_df$lift)) /
              (max(rules_df$lift) - min(rules_df$lift)) * 99) + 1))
plot(rules_df$support, rules_df$confidence, pch = 19, col = cols[col_idx],
     cex = 1.4, xlab = "Support", ylab = "Confidence",
     main = "Association Rules: Support vs Confidence (color = Lift)")
dev.off()

cat("\nDone. All results written to results/\n")
