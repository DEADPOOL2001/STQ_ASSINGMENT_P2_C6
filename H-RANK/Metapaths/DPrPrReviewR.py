import pymongo

def DPrPrReviewR():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request = db["pull_request"]
    pull_request_review = db["pull_request_review"]

    paths = []
    numberOfPaths = 0
    limit = 100

    for pr in pull_request.find({}):
        developer_id = pr["creator_id"]
        pr_id = pr["_id"]
        for pr_review in pull_request_review.find({"pull_request_id": pr_id}):
            if "creator_id" not in pr_review.keys():
                continue
            path = {"D": developer_id, "Pr": pr_id, "PrReview": pr_review["_id"], "R": pr_review["creator_id"]}
            paths.append(path)
            numberOfPaths += 1
            if numberOfPaths > limit:
                break

        if numberOfPaths > limit:
            break

    return paths
