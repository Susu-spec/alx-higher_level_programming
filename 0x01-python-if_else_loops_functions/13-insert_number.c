#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: pointer to head of the list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *trav;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	trav = head;
	while (trav->next != NULL && trav->next->n < number)
	{
		trav = trav->next;
	}

	new_node->next = trav->next;
	trav->next = new_node;

	return (new_node);
}
