#include <stdio.h>

int n, m;
int min_cnt = __INT_MAX__;

void dfs(int i, int j, int cnt, int map[n][m]) {
    int buff_map[n][m];
    
    if (i == n - 1 && j == m - 1) {
        if (cnt < min_cnt)
            min_cnt = cnt;
        return ;
    }
    if (map[i][j] == 1) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                buff_map[i][j] = map[i][j];
            }
        }
        buff_map[i][j] = 0;
        if (i > 0)
            dfs(i - 1, j, cnt + 1, buff_map);
        if (i < n - 1)
            dfs(i + 1, j, cnt + 1, buff_map);
        if (j > 0)
            dfs(i, j - 1, cnt + 1, buff_map);
        if (j < m - 1)
            dfs(i, j + 1, cnt + 1, buff_map);
    }
    return ;
}

int main() {
    scanf("%d %d", &n, &m);
    int map[n][m];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%1d", &map[i][j]);
        }
    }
    dfs(0, 0, 1, map);
    printf("%d\n", min_cnt);
}