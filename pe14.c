//
//  main.c
//  Learning2
//
//  Created by Aditya Gudibanda on 8/28/14.
//  Copyright (c) 2014 Aditya Gudibanda. All rights reserved.
//

#include <stdio.h>
#include <math.h>
int lengthofcollatz(long number);

main()
{
    int max = 1;
    int maxindex =1;
    for (int i = 1; i <= 1000000; ++i) {
        if (lengthofcollatz(i) > max) {
            max = lengthofcollatz(i);
            maxindex = i;
        }
    }
    printf("%d\n", maxindex);
    printf("%d\n", lengthofcollatz(maxindex));
}

int lengthofcollatz(long number)
{
    int length = 1;
    
    if (number == 1){
        return 1;
    }
    while(number != 1) {
        if(number%2 == 0) {
            number = number/2;
            ++length;
        }
        else if (number %2 == 1) {
            number = 3 * number + 1;
            ++length;
        }
    }
    return length;
}
