#! /usr/bin/env python3

import os
import requests

feedback_dir = "/data/feedback"
corpweb = "http://104.155.187.56/feedback/"

def process_file(text_file, id):
        out_dict={}
        with open(os.path.join(feedback_dir,text_file),"r") as f: data = f.readlines()
        #print(data)
        keys = ["id", "title", "name", "date", "feedback"]
        values = [id, data[0], data[1], data[2], data[3]]
        #print(values)
        out_dict = dict(zip(keys,values))
        #print(out_dict)
        r = requests.post(corpweb, data=out_dict)
        print(r.status_code)


def main():
        textfiles = os.listdir(feedback_dir)
        print(textfiles)
        id = 0
        for text_file in textfiles:
                process_file(text_file, id)
                id += 1



if __name__=="__main__":
        main()
