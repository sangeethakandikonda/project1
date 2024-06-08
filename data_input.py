{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "64ba3e17",
   "metadata": {},
   "outputs": [],
   "source": [
    "from os import path\n",
    "import sys\n",
    "import pandas as pd\n",
    "# argv.py\n",
    "class DataInput:\n",
    "    \n",
    "    bold_start = \"\\033[1m\"\n",
    "    bold_end = \"\\033[0;0m\"\n",
    "\n",
    "    # all extensions supported by this project.\n",
    "    supported_file_extensions = [\n",
    "        '.csv',\n",
    "    ]\n",
    "\n",
    "    # function to convert all the column names of any specific dataset into lowercase.\n",
    "    def change_to_lower_case(self, data):\n",
    "        for column in data.columns.values:\n",
    "            data.rename(columns = {column : column.lower()}, inplace = True)\n",
    "        return data\n",
    "\n",
    "    # function that takes any dataset from the input file and convert it into DataFrame.\n",
    "    # The print statements are well defined and tells about the state of the errors.\n",
    "    def inputFunction(self):\n",
    "        try:\n",
    "            filename, file_extension = path.splitext(sys.argv[1])\n",
    "            if file_extension == \"\":\n",
    "                raise SystemExit(f\"Provide the \" + self.bold_start + \"DATASET\" + self.bold_end +\" name (with extension).\\U0001F643\")\n",
    "\n",
    "            if file_extension not in self.supported_file_extensions:\n",
    "                raise SystemExit(f\"This file extension is not \" + self.bold_start + \"supported.\\U0001F643\" + self.bold_end)\n",
    "        \n",
    "        except IndexError:\n",
    "            raise SystemExit(f\"Provide the \" + self.bold_start + \"DATASET\" + self.bold_end +\" name (with extension).\\U0001F643\")\n",
    "        \n",
    "        try:\n",
    "            data = pd.read_csv(filename+file_extension)\n",
    "        except pd.errors.EmptyDataError:\n",
    "            raise SystemExit(f\"The file is \"+ self.bold_start + \"EMPTY\" + self.bold_end + \"\\U0001F635\")\n",
    "\n",
    "        except FileNotFoundError:\n",
    "            raise SystemExit(f\"File \" + self.bold_start + \"doesn't\" + self.bold_end + \" exist\\U0001F635\")\n",
    "\n",
    "        data = self.change_to_lower_case(data)\n",
    "\n",
    "        return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "794d2cab",
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
