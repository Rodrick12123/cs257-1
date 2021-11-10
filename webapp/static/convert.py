''' 
File Converter
'''
import csv

def main():
    with open('wcmatches.csv', 'w', newline='') as f1:
        with open('wcplayers.csv', 'w', newline='') as f2:
            with open('wc.csv', 'w', newline='') as f3:
                with open('worldcupmatches.csv', mode='r') as infile1:
                    with open('worldcuppayers.csv', mode='r') as infile2:
                        with open('worldcups.csv', mode='r') as infile3:
                            reader1 = csv.reader(infile1)
                            csvwriter1 = csv.writer(f1)
                            next(reader1)
                            reader2 = csv.reader(infile2)
                            csvwriter2 = csv.writer(f2)
                            next(reader2)
                            reader3 = csv.reader(infile3)
                            csvwriter3 = csv.writer(f3)
                            next(reader3)

                            for row in reader1:  
                                csvwriter1.writerow([row[0]] + [row[1]] + [row[2]] + [row[3]] + [row[4]] + [row[5]] + 
                                [row[6]] + [row[7]] + [row[8]] + [row[9]] + [row[10]] + [row[11]] + [row[12]]+ [row[13]] 
                                + [row[14] ] + [row[15]]+ [row[16]] 
                                + [row[17] ] + [row[18]])
                            for row2 in reader2:
                                csvwriter2.writerow([row2[0]] + [row2[1]] + [row2[2]] + [row2[3]] + [row2[4]] + [row2[5]] + 
                                [row2[6]] + [row2[7]] + [row2[8]])
                            for row3 in reader3:
                                csvwriter3.writerow([row3[0]] + [row3[1]] + [row3[2]] + [row3[3]] + [row3[4]] + [row3[5]] + 
                                [row3[6]] + [row3[7]] + [row3[8]] + [row3[9]])


if __name__ == "__main__":
    main()
        