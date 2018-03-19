#include <stdio.h>
#include <string.h>
#define MAX 127

char str[3 * MAX];

struct frame {
    char text[3];
    int seq_no;
}fr[MAX], shuf[MAX];

int assign_seq() {
    int i, j, k = 0;
    for (i = 0; i<strlen(str); k++) {
        fr[k].seq_no = k;
        for (j = 0; j<3 && str[i]!='\n'; j++) {
            fr[k].text[j] = str[i++];
        }
    }
    printf("After assigning sequencing numbers\n");
    for (i=0; i<k; i++) {
        printf("%d : %s\t", i, fr[i].text);
    }
    return k;
}

void generate(int *random_ary, int limit) {
    int r, i=0;
    int j;
    while(i < limit) {
        r = random()%limit;
        for (j=0; j<i; j++) {
            if (random_ary[j] == r) {
                break;
            }
        }
        if (i == j)
            random_ary[i++] = r;
    }
}

void shuffle(const int no_frames) {
    int i, k=0, random_ary[no_frames];
    generate(random_ary, no_frames);
    for (i=0; i<no_frames; i++) {
        shuf[i] = fr[random_ary[i]];
    }
    printf("\n After shuffling \n");
    for (i=0; i<no_frames; i++) {
        printf("%d : %s\t", shuf[i].seq_no, shuf[i].text);
    }
}

void sort(int no_frames) {
    int i,j, flag = 1;
    struct frame hold;
    for (i=0; i<no_frames-1; i++) {
        flag = 0;
        for (j=0; j<no_frames-1-i; j++) {
            if (shuf[j].seq_no > shuf[j+1].seq_no) {
                hold = shuf[j];
                shuf[j] = shuf[j+1];
                shuf[j+1] = shuf[j];
                flag = 1;
            }
        }
    }
}

int main() {
    int no_frames, i;
    printf("Enter the message: ");
    scanf("%s", &str);
    no_frames = assign_seq();
    shuffle(no_frames);
    sort(no_frames);
    printf("After sorting: \n");
    for (i=0; i<no_frames; i++) {
        printf("%s", shuf[i].text);
    }
    printf('\n');
    return 0;
}