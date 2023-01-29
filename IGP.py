def extract():
    cluster1_profit = 0
    cluster1_quantity = 0
    for item in cluster1:
        cluster1_profit += float(item[0].replace("$", "").replace(",", ""))
        cluster1_quantity += float(item[1])

    cluster2_profit = 0
    cluster2_quantity = 0
    for item in cluster2:
        cluster2_profit += float(item[0].replace("$", "").replace(",", ""))
        cluster2_quantity += float(item[1])

    cluster3_profit = 0
    cluster3_quantity = 0
    for item in cluster3:
        cluster3_profit += float(item[0].replace("$", "").replace(",", ""))
        cluster3_quantity += float(item[1])
    return cluster1_profit, cluster1_quantity, cluster2_profit, cluster2_quantity, cluster3_profit, cluster3_quantity


# write the calculated profit and quantity to the txt file

clus1Prof, clus1Quan, clus2Prof, clus2Quan, clus3Prof, clus3Quan = extract()
with open("cluster_report.txt", "a") as file:
    file.write("\n")
    file.write("PROFIT REPORT\n")
    file.write("="*13 + "\n")
    file.write("Cluster 1: $" + str(clus1Prof) + "\n")
    file.write("Cluster 2: $" + str(clus2Prof) + "\n")
    file.write("Cluster 3: $" + str(clus3Prof) + "\n")
    file.write("\n")
    file.write("QUANTITY REPORT\n")
    file.write("="*15 + "\n")
    file.write("Cluster 1: " + str(clus1Quan) + "\n")
    file.write("Cluster 2: " + str(clus2Quan) + "\n")
    file.write("Cluster 3: " + str(clus3Quan) + "\n")
