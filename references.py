import os


dataPath = "./data/documentation/"
input_files = [x for x in os.listdir('./data/documentation/') if x[-4:] == '.pdf']

outputPath = "./dbs/documentation/"