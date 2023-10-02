#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle.
* @list: head of a singly-linked list.
*
* Return: If there is no cycle - 0.
*	  If there is a cycle - 1.
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
