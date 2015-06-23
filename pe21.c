//
//  main.c
//  Learning2
//
//  Created by Aditya Gudibanda on 8/28/14.
//  Copyright (c) 2014 Aditya Gudibanda. All rights reserved.
//
int sumofdivisors(int n);



main()
{
    long int answer;
    int sums[10000];
    for (int i = 0; i < 10000; ++i) {
        sums[i] = sumofdivisors(i);
    }
    for (int j = 1; j <= 9999; ++j) {
        for (int k = 1; k <= 9999; ++k) {
            if (sums[j] == k && sums[k] == j && j != k) {
                printf("%d \t %d \n", j, k);
                answer = answer +j +k;
            }
        }
    }
    printf("%lu\n", answer/2);
}

int sumofdivisors(int n)
{
    int sum = 0;
    for (int i = 1; i <= n/2; ++i) {
        if (n % i == 0) {
            sum = sum + i;
        }
    }
    return sum;
}
