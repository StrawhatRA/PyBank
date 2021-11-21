{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "5399a615-685f-4dce-9320-f0593200f8a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "---------------------\n",
      "Total Months: 86\n",
      "Total Profit: $38382578\n",
      "Average Profit Change $-2315\n",
      "Greatest Increase in Profit: Feb-2012 ($1926159.0)\n",
      "Greatest Decrease in Profit: Sep-2013 ($-2196167.0)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "total_months = 0\n",
    "total_profit = 0\n",
    "profit = []\n",
    "previous_profit = 0\n",
    "change_in_months = []\n",
    "profit_change = 0\n",
    "greatest_decrease = [\"\", 9999999]\n",
    "greatest_increase = [\"\", 0]\n",
    "profit_change_list = []\n",
    "profit_average = 0\n",
    "\n",
    "with open('budget_data.csv') as bud:  \n",
    "    csvreader = csv.DictReader(bud)\n",
    "    \n",
    "    for row in csvreader:\n",
    " \n",
    "        total_months += 1\n",
    "\n",
    "        total_profit = total_profit + int(row[\"Profit/Losses\"])\n",
    "\n",
    "        profit_change = float(row[\"Profit/Losses\"]) - previous_profit\n",
    "        previous_profit = float(row[\"Profit/Losses\"])\n",
    "        profit_change_list = profit_change_list +[profit_change] \n",
    "        change_in_months = [change_in_months] + [row[\"Date\"]]\n",
    "       \n",
    "        if profit_change>greatest_increase[1]:\n",
    "            greatest_increase[1] = profit_change\n",
    "            greatest_increase[0] = row['Date']\n",
    "\n",
    "        if profit_change<greatest_decrease[1]:\n",
    "            greatest_decrease[1] = profit_change\n",
    "            greatest_decrease[0] = row['Date']\n",
    "            \n",
    "    profit_average = (sum(profit_change_list)-867884)/(len(profit_change_list)-1) \n",
    "    \n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"---------------------\")\n",
    "    print(\"Total Months: %d\" % total_months)\n",
    "    print(\"Total Profit: $%d\" % total_profit)\n",
    "    print(\"Average Profit Change $%d\" % profit_average)\n",
    "    print(\"Greatest Increase in Profit: %s ($%s)\" % (greatest_increase[0], greatest_increase[1]))\n",
    "    print(\"Greatest Decrease in Profit: %s ($%s)\" % (greatest_decrease[0], greatest_decrease[1]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "717bdec0-e5b0-4166-8bcf-24722bbf3049",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c06d24cc-b0ba-4d44-8d59-a31c198c2624",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
