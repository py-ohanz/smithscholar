import praw
import pandas as pd



reddit = praw.Reddit(client_id = "", client_secret = "", user_agent = "scrape", username = "", password = "")

sub = ['Askreddit']

for s in sub:
    subreddit = reddit.subreddit(s)

    query = ['gaming']

    for item in query:
        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num" : [],
            "created" : [],
            "body" : [],
        }
        comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            'comment_link_id' : [],
        }

        for submission in subreddit.search(query, sort = "top", limit=1):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            post_dict["comms_num"].append(submission.num_comments)
            post_dict["created"].append(submission.created)
            post_dict["body"].append(submission.selftext)

            submission.comments.replace_more(limit=1)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)

        post_comments = pd.DataFrame(comments_dict)

        post_comments.to_csv(s +"_comments_" + item + "subbreddit.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_" + item + "subreddit.csv")
