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
	listint_t *newnode;
	listint_t *trav;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;
	newnode->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	trav = *head;
	while (trav->next != NULL)
	{
		trav = trav->next;
	}

	newnode->next = trav->next;
	trav->next = new_node;

	return (new_node);
}
