from f_Kokel import *

def main():
    # location of input raster data:
    file_dir = ''

    # Check for input mistakes and get list of file names:
    CheckPath(file_dir)
    filenames_precip = glob.glob(file_dir + "\*.txt")  # Get all txt files in the path directory, and save them in a list

    a=len(filenames_precip)
    print('number of files:',a)

    # INITIATE MATRIX WHERE ALL THE FILES WILL BE SAVED
    nr = int(len(filenames_precip))  # number of rows
    # print("Number of files: ", nr)
    nc = 5  # There are 5 columns in each row: year, month, day, hour, rain (temperature or another parameter)
    tdm = np.empty(((nr, nc)), dtype=np.dtype('f4'))  # Initiate the 2D matrix, fill it with 0s
    i = 0  # counter for number of filenames, to iterate in "for file" loop

    # -----MAIN  LOOP: Iterates through every file in the given folder-----#
    for file in filenames_precip:
        name = os.path.basename(filenames_precip[i])  # gets name of file being read
        print("File: ", name)
        storm_array = np.array(pd.read_csv(file, delimiter=' ', header=None, skiprows=6))
        storm_array2 = np.where(storm_array==-9999, np.nan, storm_array) #-9999 is set to be nan
        storm_array_mean = np.nanmean(storm_array2) #calculation of the mean value for the whole array
        print(storm_array_mean)
        result_list = Prec(name, storm_array_mean, tdm, i)
        i += 1  # increases counter

    print(result_list)

    #SAVE RESULTING FILES:
    np.savetxt('Prec_Kokel' ,result_list,fmt='%1.4f', header = 'Year,Month,Day,Hour,Mean Precipitation [mm]', delimiter = ',')

   #SaveFiles2(tdm, savepath)



if __name__ == '__main__':
    main()



