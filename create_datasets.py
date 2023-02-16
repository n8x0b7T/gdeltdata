import pandas as pd

hand_labeled_df = pd.read_csv("merged_snorkel.csv").sample(frac=1).reset_index(drop=True)

rss_df = pd.read_csv("rss.csv")
rss_df = rss_df[rss_df['snorkel_label'] == -1]
rss_df = rss_df.assign(label=0).sample(300)

PROTEST = hand_labeled_df[hand_labeled_df['label'] == 1]

NOT_PROTEST = hand_labeled_df[hand_labeled_df['label'] == 0]
NOT_PROTEST = pd.concat([NOT_PROTEST, rss_df])

def even_lables(bigger, smaller):
    return bigger.sample(len(smaller))



if len(PROTEST) > len(NOT_PROTEST):
    PROTEST = even_lables(PROTEST, NOT_PROTEST)
else:
    NOT_PROTEST = even_lables(NOT_PROTEST, PROTEST)


print(len(PROTEST), len(NOT_PROTEST))
pd.concat([PROTEST, NOT_PROTEST]).to_csv("combined.csv", index=False)
