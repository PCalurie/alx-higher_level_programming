#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	/* Obtain size and allocation information */
	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	/* Loop through the list elements */
	for (i = 0; i < size; i++)
	{
		/* Get the type name of the element */
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);

		/* If the element is of type "bytes", call print_python_bytes */
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}
/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	/* Check if the object is a valid bytes object */
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	/* Print size and try to print content as a string */
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	/* Determine the number of bytes to print (up to 10) */
	if (((PyVarObject *)p)->ob_size > 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}

	/* Print the first few bytes in hexadecimal format */
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}
