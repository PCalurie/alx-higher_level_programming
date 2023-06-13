#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	/* Get the size of the list */
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	/* Get the allocated memory size for the list */
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	/* Print information about each element in the list */
	for (i = 0; i < size; i++)
	{
		/* Get the i-th item from the list */
		item = PyList_GetItem(p, i);

		/* Print the element index and its data type */
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
