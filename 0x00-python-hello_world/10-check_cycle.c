#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks for a cycle in a list
 * @list: start of the list
 * Return: 0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
