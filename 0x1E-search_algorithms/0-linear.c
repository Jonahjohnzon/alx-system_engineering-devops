#include "search_algos.h"

/**
 * linear_search - search for a value in an array
 * integers using the Linear search algorithm
 *
 * @array: input array
 * @size: size of the array
 * @value: value to search in
 * Return: Always EXIT_SUCCESS
 */
int linear_search(int *array, size_t size, int value)
{
	int e;

	if (array == NULL)
		return (-1);
	for (e = 0; e < (int)size; e++)
	{
		printf("Value checked array[%u] = [%d]\n", e, array[e]);
		if (value == array[e])
			return (e);
	}
	return (-1);
}
