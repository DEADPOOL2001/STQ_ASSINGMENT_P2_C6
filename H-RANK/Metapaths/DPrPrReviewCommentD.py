import pymongo

def DPrPrReviewCommentD():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request = db["pull_request"]
    pull_request_review = db["pull_request_review"]
    pull_request_review_comment = db["pull_request_review_comment"]

    paths = []
    numberOfPaths = 0
    limit = 100

    for pr in pull_request.find({}):
        developer_id = pr["creator_id"]
        pr_id = pr["_id"]
        for pr_review in pull_request_review.find({"pull_request_id": pr_id}):
            for pr_review_comment in pull_request_review_comment.find({"pull_request_review_id": pr_review["_id"]}):
                if numberOfPaths > limit:
                    break
                if "creator_id" not in pr_review_comment.keys():
                    continue
                path = {"D1": developer_id, "Pr": pr_id, "PrReview": pr_review_comment["_id"], "D2": pr_review_comment["creator_id"]}
                paths.append(path)
                numberOfPaths += 1
        if numberOfPaths > limit:
            break

    return paths
