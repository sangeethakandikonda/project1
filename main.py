{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "86fd9277",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_119366/2225403994.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mdata_description\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDataDescription\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdata_input\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDataInput\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mimputation\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mImputation\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdownload\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDownload\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mcategorical\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mCategorical\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/data_description.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     96\u001b[0m   {\n\u001b[1;32m     97\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 98\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     99\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"2ffd7518\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    100\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "from data_description import DataDescription\n",
    "from data_input import DataInput\n",
    "from imputation import Imputation\n",
    "from download import Download\n",
    "from categorical import Categorical\n",
    "from feature_scaling import FeatureScaling\n",
    "\n",
    "class Preprocessor:\n",
    "\n",
    "    bold_start = \"\\033[1m\"\n",
    "    bold_end = \"\\033[0;0m\"\n",
    "    \n",
    "    # The Task associated with this class. This is also the main class of the project.\n",
    "    tasks = [\n",
    "        '1. Data Description',\n",
    "        '2. Handling None Values',\n",
    "        '3. Encoding Categorical Data',\n",
    "        '4. Feature Scaling of the Dataset',\n",
    "        '5. Download the modified dataset'\n",
    "    ]\n",
    "\n",
    "    data = 0\n",
    "    \n",
    "    def __init__(self):\n",
    "        self.data = DataInput().inputFunction()\n",
    "        print(\"\\n\\n\" + self.bold_start + \"WELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\\N{grinning face}\" + self.bold_end + \"\\n\\n\")\n",
    "\n",
    "    # function to remove the target column of the DataFrame.\n",
    "    def removeTargetColumn(self):\n",
    "        print(\"Columns\\U0001F447\\n\")\n",
    "        for column in self.data.columns.values:\n",
    "            print(column, end = \"  \")\n",
    "        \n",
    "        while(1):\n",
    "            column = input(\"\\nWhich is the target variable:(Press -1 to exit)  \").lower()\n",
    "            if column == \"-1\":\n",
    "                exit()\n",
    "            choice = input(\"Are you sure?(y/n) \")\n",
    "            if choice==\"y\" or choice==\"Y\":\n",
    "                try:\n",
    "                    self.data.drop([column], axis = 1, inplace = True)\n",
    "                except KeyError:\n",
    "                    print(\"No column present with this name. Try again......\\U0001F974\")\n",
    "                    continue\n",
    "                print(\"Done.......\\U0001F601\")\n",
    "                break\n",
    "            else:\n",
    "                print(\"Try again with the correct column name...\\U0001F974\")\n",
    "        return\n",
    "    \n",
    "    def printData(self):\n",
    "        print(self.data)\n",
    "\n",
    "    # main function of the Preprocessor class.\n",
    "    def preprocessorMain(self):\n",
    "        self.removeTargetColumn()\n",
    "        while(1):\n",
    "            print(\"\\nTasks (Preprocessing)\\U0001F447\\n\")\n",
    "            for task in self.tasks:\n",
    "                print(task)\n",
    "\n",
    "            while(1):\n",
    "                try:\n",
    "                    choice = int(input(\"\\nWhat do you want to do? (Press -1 to exit):  \"))\n",
    "                except ValueError:\n",
    "                    print(\"Integer Value required. Try again.....\\U0001F974\")\n",
    "                    continue\n",
    "                break\n",
    "\n",
    "            if choice == -1:\n",
    "                exit()\n",
    "\n",
    "            # moves the control into the DataDescription class.\n",
    "            elif choice==1:\n",
    "                DataDescription(self.data).describe()\n",
    "\n",
    "\n",
    "            # moves the control into the Imputation class.\n",
    "            elif choice==2:\n",
    "                self.data = Imputation(self.data).imputer()\n",
    "                \n",
    "\n",
    "            # moves the control into the Categorical class.\n",
    "            elif choice==3:\n",
    "                self.data = Categorical(self.data).categoricalMain()\n",
    "\n",
    "\n",
    "            # moves the control into the FeatureScaling class.\n",
    "            elif choice==4:\n",
    "                self.data = FeatureScaling(self.data).scaling()\n",
    "\n",
    "\n",
    "            # moves the control into the Download class.\n",
    "            elif choice==5:\n",
    "                Download(self.data).download()\n",
    "            \n",
    "            else:\n",
    "                print(\"\\nWrong Integer value!! Try again..\\U0001F974\")\n",
    "\n",
    "# obj is the object of our Preprocessor class(main class).\n",
    "obj = Preprocessor()\n",
    "# the object 'obj' calls the main function of our Preprocessor class.\n",
    "obj.preprocessorMain()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "468fdf2b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0f0aab1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef2ccc5a",
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
