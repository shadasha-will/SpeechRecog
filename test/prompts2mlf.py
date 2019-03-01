#usr/bin/python3
#Author: Shadasha Williams

""" Script that creates a mlf file from a transcription of sentences"""

def run(filename):
    """ function that uses a text file from the path and creat    es a labels file"""
    with open(filename, 'r') as input:
        lines = input.read().split('\n')
        for line in lines:
            if line:
                sent_label = line.split()[0]
                sent = "\n".join(line.split()[1:])
                label = f'"*{sent_label}.lab"'
                print(f'{label}\n{sent}')

run('test_sent_prompts')
