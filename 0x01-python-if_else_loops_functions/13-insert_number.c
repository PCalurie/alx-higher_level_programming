#include "lists.h"
/**
 * insert_node - inserts a num into a sorted singly linked list
 * @head: parameter pointer to pointer to the head of the linked list
 * @number: num to insert
 * Return: the address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	/* allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* assign data to the new node */
	new_node->n = number;

	/*insert new node at beginning if the list empty or number is smaller than head*/
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* find the position to insert the new node */
	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	/* insert the new node after current */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
