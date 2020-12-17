#include <stdio.h>

static int	g_map[15] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
static int	g_res = 0;

int		is_invalid(int buf_map[15], int count, int j)
{
	if (buf_map[count] == buf_map[j])
		return (1);
	if (count - j == buf_map[count] - buf_map[j])
		return (1);
	if (count - j == buf_map[j] - buf_map[count])
		return (1);
	return (0);
}

void		place_queen(int n, int map[15], int count)
{
	int	i;
	int	j;
	int	buf_map[15];

	if (count == n)
	{
        g_res++;
		return ;
	}
	i = -1;
	while (++i < n)
		buf_map[i] = map[i];
	i = -1;
	while (++i < n)
	{
		buf_map[count] = i;
		j = -1;
		while (++j < count)
		{
			if (is_invalid(buf_map, count, j))
				break ;
		}
		if (j == count)
			place_queen(n, buf_map, count + 1);
	}
}

int    main(void)
{
    int n;
    
    scanf("%d", &n);
    place_queen(n, g_map, 0);
    printf("%d", g_res);
}