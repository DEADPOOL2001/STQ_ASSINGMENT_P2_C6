import pymongo

def DFPrPrReviewR():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["smartshark"]
    files = db["file"]
    pull_requests = db["pull_request"]
    pull_request_reviews = db["pull_request_review"]
    pull_request_files = db["pull_request_file"]

    paths = []
    numberOfPaths = 0
    limit = 100

    for file in files.find({}):
        if numberOfPaths > limit:
            break
        Ds = set()
        PrPrReviewRs = set()
        for pr_file in pull_request_files.find({"path": file["path"]}):
            pr_id = pr_file["pull_request_id"]
            pr = pull_requests.find_one({"_id": pr_id})
            if "creator_id" in pr.keys():
                Ds.add(pr["creator_id"])
            for pr_review in pull_request_reviews.find({"pull_request_id": pr_id}):
                if "creator_id" in pr_review.keys():
                    PrPrReviewRs.add((pr_id, pr_review["_id"], pr_review["creator_id"]))
        for D in Ds:
            for PrPrReviewR in PrPrReviewRs:
                temp = {"D": D, "F": file["path"], "Pr": str(PrPrReviewR[0]), "PrReview": str(PrPrReviewR[1]), "R": str(PrPrReviewR[2])}
                paths.append(temp)
                numberOfPaths += 1
                if numberOfPaths > limit:
                    break
            if numberOfPaths > limit:
                break
    return paths
