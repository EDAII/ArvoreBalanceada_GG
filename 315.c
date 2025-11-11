#include <stdlib.h>
#include <string.h>

typedef struct {    
    int val;
    int index;
} Pair;

void merge(Pair* items, int left, int mid, int right, Pair* temp, int* counts) {

    memcpy(temp + left, items + left, (right - left + 1) * sizeof(Pair));

    int i = left;
    int j = mid + 1;
    int k = left;
    int rightCount = 0;

    while (i <= mid && j <= right) {

        if (temp[i].val > temp[j].val) {
            items[k++] = temp[j++];
            rightCount++;
        } else {

            counts[temp[i].index] += rightCount;
            items[k++] = temp[i++];
        }
    }

    while (i <= mid) {
        counts[temp[i].index] += rightCount;
        items[k++] = temp[i++];
    }

    while (j <= right) {
        items[k++] = temp[j++];
    }
}

void mergeSort(Pair* items, int left, int right, Pair* temp, int* counts) {
    if (left >= right) {
        return;
    }

    int mid = left + (right - left) / 2;
    mergeSort(items, left, mid, temp, counts);
    mergeSort(items, mid + 1, right, temp, counts);

    if (items[mid].val > items[mid + 1].val) {
        merge(items, left, mid, right, temp, counts);
    }
}

int* countSmaller(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    if (numsSize == 0) {
        return NULL;
    }

    int* counts = (int*)calloc(numsSize, sizeof(int));

    Pair* items = (Pair*)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; i++) {
        items[i].val = nums[i];
        items[i].index = i;
    }

    Pair* temp = (Pair*)malloc(numsSize * sizeof(Pair));

    mergeSort(items, 0, numsSize - 1, temp, counts);

    free(items);
    free(temp);

    return counts;
}