#include <stdio.h>
#include <string.h>

int main() {
    char keyword[32][10]={
        "auto","double","int","struct","break","else","long",
        "switch","case","enum","register","typedef","char",
        "extern","return","union","const","float","short",
        "unsigned","continue","for","signed","void","default",
        "goto","sizeof","voltile","do","if","static","while"
    } ;

    FILE *file = fopen("ques1.c", "r"); 
    // Open the file in read mode
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1; 
        // Exit with an error code
    }

    char str[20]; 
    // Increase the size of the array to accommodate longer keywords
    int flag=0, i;

    while (fscanf(file, "%s", str) != EOF) { 
        // Read words until the end of the file
        flag = 0; 
        // Reset the flag for each word read from the file
        for (i = 0; i < 32; i++) {
            if (strcmp(str, keyword[i]) == 0) {
                flag = 1;
                break; 
                // Once a match is found, no need to continue the loop
            }
        }
        if (flag == 1)
            printf("%s is a keyword\n", str);
        else
            printf("%s is not a keyword\n", str);
    }

    fclose(file); 
    // Close the file

    return 0; 
    // Add a return statement to the main function
}
