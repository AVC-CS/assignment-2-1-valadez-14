def main():
   
    ##################################################
   # Comlete your code here
   #Use m_perc and f_perc for your results
    ##################################################
     numMales = input("Enter Number of males registered in the class:\n")
     numFemales = input("Enter Number of males registered in the class:\n")
     numMales = int(numMales)
     numFemales =  int(numFemales)
     total = numMales + numFemales
     m_perc = numMales/total * 100
     f_perc = numFemales/total * 100

     print(f'The total number of students:\t\t\t\t{total}')
     print(f'The number of males and females:\t\t\t{numMales}\t {numFemales}')
     print(f'The percentage of males and females:\t\t\t{m_perc:.2f}%\t {f_perc:.2f}%')



    

    ########################################
    # Do not delete the return statement
    ########################################
    
     return m_perc, f_perc


if __name__ == '__main__':
    main()
