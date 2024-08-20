"""
FDS Assignment-6

Que. Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores
"""

def insert_sort(arr,n):
    i=1
    for i in range (n):
        temp=arr[i]
        j=i-1
        while ((j>=0) and (arr[j]>temp)):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp

    print(arr)

    arr2=arr[::-1]
    print("\nTop 5 Scores are: ")
    if (len(arr2))>5:
        for i in range (5):
            print("%f" %arr2[i])
    else:
        for i in range (len(arr2)):
            print("%f" %arr2[i])

def shell_sort(arr,n):
    gap=n//2
    while gap>=1:
        j=gap
        while j<n:
            i=j-gap
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    t=arr[i+gap]
                    arr[i+gap]=arr[i]
                    arr[i]=t
                i=i-gap
            j=j+1
        gap=gap//2

    print(arr)

    arr2=arr[::-1]
    print("\nTop 5 Scores are: ")
    if (len(arr2))>5:
        for i in range (5):
            print("%f" %arr2[i])
    else:
        for i in range (len(arr2)):
            print("%f" %arr2[i])



n=int(input("\nEnter Number of Students whose Marks are to be displayed: "))
arr=[]
i=0
for i in range(n):
    item=float(input("Enter Percentage of student: "))
    arr.append(item)

print("Pecentage of Students are: ",arr)
while(True):
    print("\n\n******* Main Menu ******* \n\t1. Insertion Sort \n\t2. Shell Sort \n\t3.Exit")
    ch=int(input("\nEnter your Coice: "))

    if (ch==1):
        print("\nThe Sorted Scores using Insertion Sort are:")
        insert_sort(arr,n)

    elif (ch==2):
        print("\nThe Sorted Scores using Shell Sort are:")
        shell_sort(arr,n)

    else:
        print("Exit")
        exit()

"""
Output

Enter Number of Students whose Marks are to be displayed: 8
Enter Percentage of student: 89
Enter Percentage of student: 78
Enter Percentage of student: 58
Enter Percentage of student: 69
Enter Percentage of student: 48
Enter Percentage of student: 37
Enter Percentage of student: 52
Enter Percentage of student: 15
Pecentage of Students are:  [89.0, 78.0, 58.0, 69.0, 48.0, 37.0, 52.0, 15.0]


******* Main Menu *******
        1. Insertion Sort
        2. Shell Sort
        3.Exit

Enter your Coice: 1

The Sorted Scores using Insertion Sort are:
[15.0, 37.0, 48.0, 52.0, 58.0, 69.0, 78.0, 89.0]

Top 5 Scores are:
89.000000
78.000000
69.000000
58.000000
52.000000


******* Main Menu *******
        1. Insertion Sort
        2. Shell Sort
        3.Exit

Enter your Coice: 2

The Sorted Scores using Shell Sort are:
[15.0, 37.0, 89.0, 52.0, 58.0, 69.0, 78.0, 89.0]

Top 5 Scores are:
89.000000
78.000000
69.000000
58.000000
52.000000


******* Main Menu *******
        1. Insertion Sort
        2. Shell Sort
        3.Exit

Enter your Coice: 3
Exit

"""

