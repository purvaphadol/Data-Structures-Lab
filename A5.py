"""
FDS Assignment-5

Que. Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
"""

arr=[]
arr1=[]

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range (0,n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


def selection_sort(arr1):
    for i in range(len(arr1)):      
        min_idx=1
        for j in range(i+1,len(arr1)):
            if (arr1[min_idx]>arr1[j]):
                min_idx=j
        arr1[i],arr1[min_idx]=arr1[min_idx],arr1[i]


print("Which Sorting Operation you want to Perform ")
print("\t1. Selection Sort \n\t2. Bubble Sort")
ch=int(input("\nEnter your choice: "))

if (ch==1):
    
    num=int(input("\nEnter the Number of Students for which you want to Enter thier Percentage: "))
    for i in range(num):
        per=float(input("Enter the Percentage of Student: "))
        arr.append(per)

    bubble_sort(arr)
    print("Sorted Array is:")
    for i in range(len(arr)):
        print("%f" %arr[i])

    arr2=arr[::-1]
    print("Top 5 Students Marks are: ")
    if (len(arr2))>5:
        for i in range (5):
            print("%f" %arr2[i])
    else:
        for i in range (len(arr2)):
            print("%f" %arr2[i])

elif (ch==2):
    
    num=int(input("\nEnter the Number of Students for which you want to Enter thier Percentage: "))
    for i in range(num):
        per=float(input("Enter the Percentage of Students: "))
        arr1.append(per)

    selection_sort(arr1)
    print("Sorted Array is:")
    for i in range (len(arr1)):
        print("%f" %arr1[i])
        
    arr2=arr1[::-1]
    print("Top 5 Students Marks are: ")
    if (len(arr2))>5:
        for i in range (5):
            print("%f" %arr2[i])
    else:
        for i in range (len(arr2)):
            print("%f" %arr2[i])

else:
    print("Invalid Choice.")


"""
Output

Which Sorting Operation you want to Perform 
        1. Selection Sort
        2. Bubble Sort

Enter your choice: 1

Enter the Number of Students for which you want to Enter thier Percentage: 8
Enter the Percentage of Student: 98
Enter the Percentage of Student: 65
Enter the Percentage of Student: 34
Enter the Percentage of Student: 57
Enter the Percentage of Student: 68
Enter the Percentage of Student: 48
Enter the Percentage of Student: 19
Enter the Percentage of Student: 56
Sorted Array is:
19.000000
34.000000
48.000000
56.000000
57.000000
65.000000
68.000000
98.000000
Top 5 Students Marks are:
98.000000
68.000000
65.000000
57.000000
56.000000




Which Sorting Operation you want to Perform 
        1. Selection Sort
        2. Bubble Sort

Enter your choice: 2

Enter the Number of Students for which you want to Enter thier Percentage: 7
Enter the Percentage of Students: 45
Enter the Percentage of Students: 68
Enter the Percentage of Students: 97
Enter the Percentage of Students: 63
Enter the Percentage of Students: 53
Enter the Percentage of Students: 84
Enter the Percentage of Students: 75
Sorted Array is:
53.000000
84.000000
45.000000
68.000000
75.000000
63.000000
97.000000
Top 5 Students Marks are:
97.000000
63.000000
75.000000
68.000000
45.000000



Which Sorting Operation you want to Perform 
        1. Selection Sort
        2. Bubble Sort

Enter your choice: 5
Invalid Choice.

"""




