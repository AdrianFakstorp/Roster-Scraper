# Case Pool Generator

The purpose of this program is up ultimately be able to create a list of 12 CSGO Skin prizes based on a user-inputted value. To do this, the program creates a set of JSON files that contain a list of all skins from a given case. The JSON files also prices each of those skins against a pricing API. This is all done in `Case_URL_Parser.py`

From there, `prize_list_forumlator.py` will ask the user for an input on their case choice and their budget choice. Once those are determined, the program will iterate through the selected case-JSON and choose skins to fill into each of the 12 ranks, based on the selected budget. To do that, the program will start with the 1st place value, and compile a list of all the skins that fill that specific spot. If there is more than one skin in that list, the program will randomly select a skin from that list and set it as the 1st place prize. It will then move on to the subsequent placements. It should be noted that when selecting skins, the program will only choose skins that have not already been chosen for the main prizing list. This duplicate check will happen regardless of Stattrak prefix or the skins wear.

The output will be both in the terminal and in the `output.txt` file found in `/jsonCase Storage` folder.

## Getting Started

This program can simply be used through two main Python scripts: `Case_URL_Parser.py` and `prize_list_forumlator.py`. There are a number of peripheral scripts that will be touched on later. For now ensure that those two are in your program folder.

#Pricing API
For `Case_URL_Parser.py` to work, you will need change your config.py file to have a working pricing API.

The pricing API outputs in the following JSON format:

>{"data":[{"market_name":"blah", price:22.20, amount:22.20}, …etc]} }


## Case JSONs

The program folder will come with most of the cases already, which can be found in the `/jsonCase Storage` folder. If you want to update an existing case with more up-to-date prices, or add a new case, you can run the `Case_URL_Parser.py` script.

This script will ask you for the full steam URL for the case that you want. To see which case you already exist, you can look at the json files in the `/jsonCase Storage` folder, or you can run the `caselist_print.py` script.

## Price LIsts

By default, this program comes with 3 pricing breakdowns for $50, $60, $100. To add more, you will have to use the `Price_list_generator.py` script. 
