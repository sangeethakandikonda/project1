{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a288e5ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "class Download:\n",
    "\n",
    "    bold_start = \"\\033[1m\"\n",
    "    bold_end = \"\\033[0;0m\"\n",
    "\n",
    "    def __init__(self, data):\n",
    "        self.data = data\n",
    "\n",
    "    # download the modified DataFrame as .csv file\n",
    "    def download(self):\n",
    "        toBeDownload = {}\n",
    "        for column in self.data.columns.values:\n",
    "            toBeDownload[column] = self.data[column]\n",
    "\n",
    "        newFileName = input(\"\\nEnter the \" + self.bold_start +\"FILENAME\" + self.bold_end +\" you want? (Press -1 to go back):  \")\n",
    "        if newFileName==\"-1\":\n",
    "            return\n",
    "        newFileName = newFileName + \".csv\"\n",
    "        # index=False as this will not add an extra column of index.\n",
    "        pd.DataFrame(self.data).to_csv(newFileName, index = False)\n",
    "        \n",
    "        print(\"Hurray!! It is done....\\U0001F601\")\n",
    "        \n",
    "        if input(\"Do you want to exit now? (y/n) \").lower() == 'y':\n",
    "            print(\"Exiting...\\U0001F44B\")\n",
    "            exit()\n",
    "        else:\n",
    "            return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f8abbf9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
