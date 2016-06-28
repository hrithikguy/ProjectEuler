//
//  main.c
//  Learning2
//
//  Created by Aditya Gudibanda on 8/28/14.
//  Copyright (c) 2014 Aditya Gudibanda. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

main()
{
    long long sum = 0;
    long fib[50];
    fib[0] = 0;
    fib[1] = 1;
    for(int i = 2; i <= 50; i++) {
        fib[i] = fib[i-1] + fib[i-2];
    }
    for (int i = 1; i < 50; ++i) {
        if (((fib[i] % 2) == 0) && (fib[i] <= 4000000)) {
            sum += fib[i];
        }
    }
    printf("%llu", sum);
}
