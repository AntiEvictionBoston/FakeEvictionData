from eviction import RandomEviction
import os
import json

def gather_user_input():
    params = {}
    if os.path.isfile("Master_Address_List.csv"):
        params["csv_file"] = "Master_Address_List.csv"
        print("Found Master_Address_List.csv")
    else:
        params["csv_file"] = input("Enter the CSV filename: ")
    params["start_date"] = input("Enter the start year: ")
    params["end_date"] = input("Enter the end year: ")
    params["start_date"] += '-01-01'
    params["end_date"] += '-01-01'
    params["number_to_generate"] = int(input("Enter the number of evictions to generate:"))
    return params


if __name__ == '__main__':
    params = gather_user_input()
    random_eviction = RandomEviction(params)
    if os.path.isfile("evictions.json"):
        raise IOError("Evictions file already present - move or delete to generate another")
    evictions = []

    for i in range(params["number_to_generate"]):
        evictions.append(random_eviction.generate())
    evictions.sort(key = lambda d: d["date"])

    with open("./evictions.json", "w") as f:
        json.dump(evictions, f)

    print("%d evictions saved to 'evictions.json'" %(params["number_to_generate"]))
