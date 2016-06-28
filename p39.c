//
//  main.c
//  Learning2
//
//  Created by Aditya Gudibanda on 8/28/14.
//  Copyright (c) 2014 Aditya Gudibanda. All rights reserved.
//

#include <stdio.h>
#include <math.h>
int numberofpythags(int sum);

main()
{
    int max = 0;
    int maxindex;
    for (int i = 1; i <= 1000; ++i) {
        if (numberofpythags(i) > max) {
            max = numberofpythags(i);
            maxindex = i;
        }
    }
    printf("%d\n", maxindex);
}

int numberofpythags(int sum)
{
    float c;
    int answer = 0;
    for (int a = 1; a <= sum; ++a) {
        for (int b = a; b <= sum; ++b) {
            c = sqrt(a* a + b* b);
            if ((a + b > c) && (a+b+c == sum)) {
                ++answer;
            }
        }
    }
    return answer;
}
