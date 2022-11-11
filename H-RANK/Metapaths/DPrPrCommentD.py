import pymongo

def DPrPrCommentD():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    pull_request = db["pull_request"]
    pull_request_comment = db["pull_request_comment"]

    paths = []
    numberOfPaths = 0
    limit = 100

    for pr in pull_request.find({}):
        developer_id = pr["creator_id"]
        pr_id = pr["_id"]
        for pr_comment in pull_request_comment.find({"pull_request_id": pr_id}):
            if "author_id" not in pr_comment.keys():
                continue
            if numberOfPaths > limit:
                break
            path = {"D1": developer_id, "Pr": pr_id, "PrComment": pr_comment["_id"],
                    "D2": pr_comment["author_id"]}
            paths.append(path)
            numberOfPaths += 1
        if numberOfPaths > limit:
            break
    return paths
